import os
import subprocess
from git import Repo
from config import (repo_server_url, repo_project_url, server_clone_path, project_clone_path, YELLOW, BLUE, GREEN, RED, RESET)

def is_tool_installed(name):
    try:
        subprocess.run([name, '--version'], stdout=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False

def install_composer():
    print(f"{YELLOW}Installing Composer...{RESET}")
    subprocess.run(['curl', '-sS', 'https://getcomposer.org/installer', '-o', 'composer-setup.php'])
    subprocess.run(['php', 'composer-setup.php', '--install-dir=/usr/local/bin', '--filename=composer'])
    os.remove('composer-setup.php')

# Create the directories if they don't exist
os.makedirs(server_clone_path, exist_ok=True)
os.makedirs(project_clone_path, exist_ok=True)

# Clone the server repository
print(f"{YELLOW}Cloning server repository...{RESET}")
Repo.clone_from(repo_server_url, server_clone_path)
print(f"{GREEN}Successfully cloned server repository to {server_clone_path}{RESET}")

# Ask the user for the project folder name
project_name = input(f"{YELLOW}Enter the name for the project folder: {RESET}").strip()
actual_project_path = os.path.join(project_clone_path, project_name)

# Create the project directory and clone the project repository
os.makedirs(actual_project_path, exist_ok=True)
print(f"{YELLOW}Cloning project repository...{RESET}")
Repo.clone_from(repo_project_url, actual_project_path)
print(f"{GREEN}Successfully cloned project repository to {actual_project_path}{RESET}")

# Create a new 'src' folder in the actual project directory
src_path = os.path.join(actual_project_path, 'src')
os.makedirs(src_path, exist_ok=True)
print(f"{GREEN}Successfully created src folder at {src_path}{RESET}")

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
        print(f"{YELLOW}Composer not found. Installing...{RESET}")
        install_composer()

    # Install the chosen framework
    frameworks[choice]['install']()

    print(f"{GREEN}Successfully installed {frameworks[choice]['name']} at {src_path}{RESET}")
else:
    print(f"{RED}Invalid choice. No framework installed.{RESET}")
