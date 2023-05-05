# Set Up PHP Development Environment

## Overview

This script **automates the process of setting up a PHP development environment** and is built with Python. 

It clones the specified Docker server container and Docker project container repositories, creates a project folder with a name defined by the user, and installs the desired PHP framework in a **src** (this is required by the Docker project container package) folder within the project directory. 

Additionally, the script now includes error handling and logging functionality.

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

## TODO

- **_Database setup_**: Add support for automatically creating and configuring databases for the chosen framework (MySQL, PostgreSQL, SQLite, etc.).

- **_Virtual environment setup_**: Integrate the creation and activation of virtual environments (using tools like Docker, Vagrant, or virtualenv) to isolate dependencies and make the development process more consistent across different systems.

- **_Custom configuration_**: Allow users to provide a custom configuration file (e.g., JSON or YAML) to set up their preferred settings, such as repository URLs, clone paths, or database configurations.

- **_Front-end frameworks_**: Add support for popular front-end frameworks such as Vue.js, React, or Angular. The script could install the necessary dependencies and set up a basic template for the chosen framework.

- **_Automated testing setup_**: Integrate testing frameworks like PHPUnit, Behat, or Codeception, and automatically configure them for the chosen PHP framework.

- **_Code linting and formatting_**: Integrate code linters and formatters like PHP_CodeSniffer, PHP-CS-Fixer, or ESLint to enforce coding standards and style guides.

- **_Continuous Integration/Continuous Deployment (CI/CD) setup_**: Add support for configuring CI/CD tools like Jenkins, Travis CI, or GitHub Actions to automate building, testing, and deploying the project.

- **_Git hooks_**: Set up useful Git hooks to automatically run tests, linting, or formatting before committing or pushing code.

- **_Interactive command-line interface (CLI)_**: Enhance the user experience by creating an interactive CLI using a library like Click or argparse, which allows users to navigate through the available options more easily.

- [x] **_Error handling and logging_**: ~~Improve error handling and add logging capabilities to help users identify and resolve issues during the setup process~~.

## Docker Server and Project Container Repositories

- [Docker Local Web Server](https://github.com/mnestorov/docker-local-web-server)
- [Docker Project Container with PHP 8+ and Apache](https://github.com/mnestorov/docker-poject-container)

## License

This project is licensed under the MIT License.