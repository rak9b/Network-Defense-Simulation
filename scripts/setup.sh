#!/bin/bash

# Setup Script for Network Defense Simulation
# Author: Your Name
# Version: 1.0.0

# Constants
LOG_DIR="logs"
CONFIG_DIR="config"
VENV_DIR="venv"
REQUIREMENTS_FILE="requirements.txt"

# Functions
setup_virtualenv() {
    echo "Setting up Python virtual environment..."
    python3 -m venv $VENV_DIR
    source $VENV_DIR/bin/activate
    pip install --upgrade pip
    if [ -f "$REQUIREMENTS_FILE" ]; then
        pip install -r $REQUIREMENTS_FILE
    else
        echo "ERROR: $REQUIREMENTS_FILE not found."
        exit 1
    fi
}

create_directories() {
    echo "Creating necessary directories..."
    mkdir -p $LOG_DIR
    mkdir -p $CONFIG_DIR
}

generate_sample_configs() {
    echo "Generating sample configuration files..."
    FIREWALL_CONFIG="$CONFIG_DIR/firewall_rules.conf"
    IDS_CONFIG="$CONFIG_DIR/ids_rules.conf"

    if [ ! -f $FIREWALL_CONFIG ]; then
        cat > $FIREWALL_CONFIG <<EOL
[
    {"source": "192.168.1.0/24", "destination": "10.0.0.0/24", "protocol": "tcp"}
]
EOL
    fi

    if [ ! -f $IDS_CONFIG ]; then
        cat > $IDS_CONFIG <<EOL
[
    {"name": "BlockSSH", "protocol": "tcp", "port": 22}
]
EOL
    fi
}

cleanup() {
    echo "Cleaning up temporary files..."
    find . -type f -name '*.pyc' -delete
    find . -type d -name '__pycache__' -exec rm -rf {} +
}

# Main
echo "Starting setup for Network Defense Simulation..."
create_directories
setup_virtualenv
generate_sample_configs
cleanup
echo "Setup complete. Use 'source $VENV_DIR/bin/activate' to activate the virtual environment."
