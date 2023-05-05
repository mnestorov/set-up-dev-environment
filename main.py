import os
import subprocess
from git import Repo
from git.exc import GitCommandError
from config import (repo_server_url, repo_project_url, server_clone_path, project_clone_path, YELLOW, BLUE, GREEN, RED, RESET, log_filename)

import logging

# Configure logging
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_tool_installed(name):
    try:
        subprocess.run([name, '--version'], stdout=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        logging.warning(f"{name} not found.")
        return False

def install_composer():
    logging.info("Installing Composer...")
    try:
        subprocess.run(['curl', '-sS', 'https://getcomposer.org/installer', '-o', 'composer-setup.php'])
        subprocess.run(['php', 'composer-setup.php', '--install-dir=/usr/local/bin', '--filename=composer'])
        os.remove('composer-setup.php')
        logging.info("Composer installed successfully.")
    except Exception as e:
        logging.error(f"Error installing Composer: {e}")

# Create the directories if they don't exist
os.makedirs(server_clone_path, exist_ok=True)
os.makedirs(project_clone_path, exist_ok=True)

# Clone the server repository
logging.info("Cloning server repository...")
try:
    Repo.clone_from(repo_server_url, server_clone_path)
    logging.info(f"Successfully cloned server repository to {server_clone_path}")
except GitCommandError as e:
    logging.error(f"Error cloning server repository: {e}")

# Ask the user for the project folder name
project_name = input(f"{YELLOW}Enter the name for the project folder: {RESET}").strip()
actual_project_path = os.path.join(project_clone_path, project_name)

# Create the project directory and clone the project repository
os.makedirs(actual_project_path, exist_ok=True)
logging.info("Cloning project repository...")
try:
    Repo.clone_from(repo_project_url, actual_project_path)
    logging.info(f"Successfully cloned project repository to {actual_project_path}")
except GitCommandError as e:
    logging.error(f"Error cloning project repository: {e}")

# Create a new 'src' folder in the actual project directory
src_path = os.path.join(actual_project_path, 'src')
os.makedirs(src_path, exist_ok=True)
logging.info(f"Successfully created src folder at {src_path}")

frameworks = {
    '1': {
        'name': 'Laravel 9',
        'install': lambda: subprocess.run(['composer', 'create-project', '--prefer-dist', 'laravel/laravel', src_path, '9.*'])
    },
    '2': {
        'name': 'CodeIgniter 4',
        'install': lambda: subprocess.run(['composer', 'create-project', 'codeigniter4/appstarter', src_path])
    },
    '3': {
        'name': 'Phalcon',
        'install': lambda: print(f"{BLUE}Please follow the Phalcon installation guide at https://docs.phalcon.io/4.1/en/webserver-nginx{RESET}")
    },
    '4': {
        'name': 'OpenCart',
        'install': lambda: print(f"{BLUE}Please follow the OpenCart installation guide at https://github.com/opencart/opencart#installation{RESET}")
    },
    '5': {
        'name': 'WordPress',
        'install': lambda: print(f"{BLUE}Please follow the WordPress installation guide at https://wordpress.org/support/article/how-to-install-wordpress/{RESET}")
    }
}

# Ask the user which framework they want to install
print(f"{BLUE}\nChoose a framework to install in the 'src' folder:{RESET}")
for key, framework in frameworks.items():
    print(f"{key}. {framework['name']}")

choice = input(f"{YELLOW}Enter the number of your choice: {RESET}").strip()

if choice in frameworks:
    if not is_tool_installed('composer') and choice in ['1', '2']:
        logging.warning("Composer not found. Installing...")
        install_composer()

    # Install the chosen framework
    try:
        frameworks[choice]['install']()
        logging.info(f"Successfully installed {frameworks[choice]['name']} at {src_path}")
    except Exception as e:
        logging.error(f"Error installing {frameworks[choice]['name']}: {e}")
else:
    logging.error("Invalid choice. No framework installed.")