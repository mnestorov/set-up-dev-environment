# Set Up PHP Development Environment

This script **automates the process of setting up a PHP development environment** and is build with Python. It clones the specified Docker server container and Docker project container repositories, creates a project folder with a name defined by the user, and installs the desired PHP framework in a 'src' (this is required by the Docker project container package) folder within the project directory.

## Prerequisite

- Python 3.6 or higher
- Git

## Installation

1. **Clone this repository to your local machine:** `git clone https://github.com/your-repo-url`
2. **Change into the cloned repository directory:** `cd SetUpPhpDevelopmentEnvironment`
3. **Install the required Python packages:** `pip install gitpython`

## Configuration

1. Open the `config.py` file and set the following variables according to your preferences:

- **repo_server_url** - `https://github.com/mnestorov/laravel-docker-web-server` - This is the required package [Docker Web Server for Ubuntu 22.04](https://github.com/mnestorov/laravel-docker-web-server)
- **repo_project_url** - `https://github.com/mnestorov/laravel-project-container` - This is the required package [Docker Container for Laravel 8+ and PHP 8.0 With Apache Web Server](https://github.com/mnestorov/laravel-project-container)
- **server_clone_path** - '/path/to/custom/location/server_repo'
- **project_clone_path** - '/path/to/custom/location/project_repo'

2. Replace the placeholders with the appropriate values for your repositories and desired clone paths.

## Usage

- **Make the bash script executable:** `chmod +x run_dev_environment.sh`
- **Run the script:** `./run_dev_environment.sh`
- Follow the prompts to set up your PHP development environment.

## Docker Server and Project Container Repositories

- [Docker Web Server for Ubuntu 22.04](https://github.com/mnestorov/laravel-docker-web-server)
- [Docker Container for Laravel 8+ and PHP 8.0 With Apache Web Server](https://github.com/mnestorov/laravel-project-container)