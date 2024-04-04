#!/bin/bash

# The directory where the virtual environment will be created, inside the server directory
VENV_DIR="server/venv"

# The requirements file inside the server directory
REQUIREMENTS_FILE="server/requirements.txt"

# Exit in case of error
set -e

# Check for Python 3 and exit if not found
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Please install Python 3."
    exit 1
fi

# Create a virtual environment
echo "Creating virtual environment inside server directory..."
python3 -m venv $VENV_DIR

# Activate the virtual environment
source $VENV_DIR/bin/activate

# Upgrade pip to the latest version
pip install --upgrade pip

# Check for requirements.txt file and install if exists
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Installing requirements from $REQUIREMENTS_FILE..."
    pip install -r $REQUIREMENTS_FILE
else
    echo "No requirements.txt found. Skipping dependency installation."
fi

# Deactivate the environment
deactivate

echo "Setup complete. Use 'source $VENV_DIR/bin/activate' to activate the virtual environment."
