#!/bin/bash

# Set up the 'bruh' command globally
setup_bruh_command() {
    # Locate the absolute path to brainrot.py relative to setup_linux.sh
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    BRAINROT_PATH="$SCRIPT_DIR/brainrot/src/brainrot.py"

    # Verify that brainrot.py exists at the detected path
    if [ ! -f "$BRAINROT_PATH" ]; then
        echo "Error: brainrot.py not found at $BRAINROT_PATH"
        exit 1
    fi

    # Create the /usr/local/bin/bruh script
    BRUH_PATH="/usr/local/bin/bruh"
    echo '#!/bin/bash' | sudo tee "$BRUH_PATH" > /dev/null
    echo "python3 \"$BRAINROT_PATH\" \"\$@\"" | sudo tee -a "$BRUH_PATH" > /dev/null

    # Make the 'bruh' script executable
    sudo chmod +x "$BRUH_PATH"
    echo "'bruh' command set up successfully! You can now use 'bruh <filename>' to run Brainrot scripts."
}

# Run the setup function
setup_bruh_command
