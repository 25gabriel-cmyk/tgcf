import subprocess
import os
import getpass


def run_command(command):
    """Run a command in the terminal."""
    subprocess.run(command, shell=True)


if __name__ == "__main__":
    # Create a virtual environment
    run_command("python3 -m venv .venv")

    # Prompt for password
    password = getpass.getpass("Enter your password: ")
    command = f'echo "PASSWORD={password}" >> .env'
    os.system(command)

    # Activate the virtual environment
    activate_command = os.path.join(".venv", "bin", "activate")
    run_command(f"source {activate_command}")

    # Install 'tgcf' package
    run_command("pip install tgcf")

    # Check 'tgcf' version
    run_command("tgcf --version")

    # Run TGCF Web
    run_command("tgcf-web")
