# Set Up PHP Development Environment

This script **automates the process of setting up a PHP development environment** and is built with Python. It clones the specified Docker server container and Docker project container repositories, creates a project folder with a name defined by the user, and installs the desired PHP framework in a 'src' (this is required by the Docker project container package) folder within the project directory. Additionally, the script now includes error handling and logging functionality.

## Prerequisite

- Python 3.6 or higher
- Git

## Installation

1. **Clone this repository to your local machine** `git clone https://github.com/mnestorov/set-up-dev-environment`
2. **Change into the cloned repository directory:** `cd SetUpPhpDevelopmentEnvironment`
3. **Install the required Python packages:** `pip install gitpython`

## Configuration

1. Open the `config.py` file and set the following variables according to your preferences:

- **repo_server_url** - `https://github.com/mnestorov/docker-local-web-server` - This is the required package [Docker Local Web Server](https://github.com/mnestorov/docker-local-web-server)
- **repo_project_url** - `https://github.com/mnestorov/docker-poject-container` - This is the required package [Docker Project Container with PHP 8+ and Apache](https://github.com/mnestorov/docker-poject-container)
- **server_clone_path** - '/path/to/custom/location/server_repo'
- **project_clone_path** - '/path/to/custom/location/project_repo'
- **log_filename** - 'app.log'

2. Replace the placeholders with the appropriate values for your repositories, desired clone paths, and log file name.

## Usage

- **Make the bash script executable:** `chmod +x run_dev_environment.sh`
- **Run the script:** `./run_dev_environment.sh`
- Follow the prompts to set up your PHP development environment.

## New Functionalities

- **Error handling:** The script now includes error handling for better stability.
- **Logging:** All the important events and errors are logged into a log file named 'app.log' (or any other name specified in config.py), providing useful information for troubleshooting.

## Docker Server and Project Container Repositories

- [Docker Local Web Server](https://github.com/mnestorov/docker-local-web-server)
- [Docker Project Container with PHP 8+ and Apache](https://github.com/mnestorov/docker-poject-container)
