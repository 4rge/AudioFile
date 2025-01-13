import os
import subprocess
import sys

def create_virtual_env(env_name):
    """Create a virtual environment."""
    print(f"Creating virtual environment: {env_name}...")
    subprocess.check_call([sys.executable, '-m', 'venv', env_name])
    print("Virtual environment created.")

def install_package(env_name):
    """Installs the package using setup.py in the activated virtual environment."""
    print(f"Installing the package in the virtual environment '{env_name}'...")
    
    # Construct the command to run setup.py within the virtual environment
    activate_script = os.path.join(env_name, 'Scripts', 'activate_this.py') if os.name == 'nt' else os.path.join(env_name, 'bin', 'activate_this.py')
    
    with open(activate_script) as f:
        exec(f.read(), dict(__file__=activate_script))
    
    # Run the setup.py installation
    setup_script = 'setup.py'  # Ensure this is the correct path to your setup.py
    subprocess.check_call([sys.executable, setup_script, 'install'])

if __name__ == "__main__":
    env_name = "venv"  # Change the name of the virtual environment here if needed
    create_virtual_env(env_name)
    install_package(env_name)
