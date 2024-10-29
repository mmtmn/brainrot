# to run on windows make sure to run this on powershell: powershell -ExecutionPolicy Bypass -File setup_bruh.ps1

# Check if a command exists
function CommandExists($cmd) {
    return Get-Command $cmd -ErrorAction SilentlyContinue -ne $null
}

# Define Brainrot command setup for Windows
function Setup-BruhWindows {
    Write-Output "Setting up 'bruh' on Windows..."

    # Check if python is installed, install if necessary
    if (-not (CommandExists "python")) {
        Write-Output "'python' is not installed. Installing Python..."

        # Install Python using Chocolatey if available
        if (CommandExists "choco") {
            choco install -y python
        } else {
            Write-Output "Please install Python manually from https://www.python.org/downloads/ and re-run this script."
            exit 1
        }
    }

    # Write the 'bruh' command as a .bat file in the user's home directory
    $BruhPath = "$HOME\bruh.bat"
    "@echo off
    python `"$PSScriptRoot\src\brainrot.py`" %*" | Out-File -Encoding ASCII -FilePath $BruhPath

    # Add user's home directory to PATH if not already present
    if (-not ($Env:Path -match [regex]::Escape($HOME))) {
        Write-Output "Adding $HOME to PATH..."
        [Environment]::SetEnvironmentVariable("Path", "$Env:Path;$HOME", [EnvironmentVariableTarget]::User)
    }

    Write-Output "'bruh' command set up successfully! Use 'bruh <filename>' to run Brainrot scripts."
}

# Run setup for Windows
Setup-BruhWindows
