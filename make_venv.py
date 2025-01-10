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
    print(f"To install the package, please activate the virtual environment '{env_name}'.")
    print("On Windows, run:")
    print(f"    .\\{env_name}\\Scripts\\activate")
    print("On Unix or MacOS, run:")
    print(f"    source {env_name}/bin/activate")
    print("\nAfter activating, run:")
    print(f"    sudo python setup.py install")
    
if __name__ == "__main__":
    env_name = "venv"  # Change the name of the virtual environment here if needed
    create_virtual_env(env_name)
    install_package(env_name)
