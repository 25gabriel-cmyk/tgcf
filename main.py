import subprocess


def run_command(command):
  """Run a command in the terminal."""
  subprocess.run(command, shell=True)


if __name__ == "__main__":
  # Create a virtual environment
  run_command("python3 -m venv .venv")

  # Activate the virtual environment
  run_command("source .venv/bin/activate")

  # Install 'tgcf' package
  run_command("pip install tgcf")

  # Check 'tgcf' version
  run_command("tgcf --version")

  # Run TGCF Web
  run_command("tgcf-web")
