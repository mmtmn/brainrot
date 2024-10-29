#!/bin/bash

# Helper function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Define Brainrot command setup for Linux and MacOS
setup_bruh_unix() {
    echo "Setting up 'bruh' on Linux/MacOS..."

    # Check if python3 is installed, install if necessary
    if ! command_exists python3; then
        echo "'python3' is not installed. Installing Python 3..."
        sudo apt update && sudo apt install -y python3 || brew install python3
    fi

    # Write the 'bruh' command
    BRUH_PATH="/usr/local/bin/bruh"
    echo '#!/bin/bash' > "$BRUH_PATH"
    echo "python3 \"$(pwd)/src/brainrot.py\" \"\$@\"" >> "$BRUH_PATH"

    # Make it executable
    chmod +x "$BRUH_PATH"
    echo "'bruh' command set up successfully! Use 'bruh <filename>' to run Brainrot scripts."
}

# Run setup for Unix-based systems
setup_bruh_unix
