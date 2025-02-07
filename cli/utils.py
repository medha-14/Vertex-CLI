import itertools
import sys
import time


def spin_loader(stop_event):
    """
    Displays a spinning loader in the console until the stop_event is set.

    Args:
        stop_event (threading.Event): An event object used to signal the loader to stop.
    """
    spinner = itertools.cycle(["-", "/", "|", "\\"])
    while not stop_event.is_set():
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\b")
    sys.stdout.write(" ")
    sys.stdout.flush()


def install_requirements(requirements_file="requirements.txt"):
    """
    Installs dependencies from a given requirements.txt file.
    Works across different OS environments.
    """
    import subprocess
    import sys
    import os

    if not os.path.exists(requirements_file):
        print(f"Error: {requirements_file} not found!")
        return

    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", requirements_file],
            check=True,
        )
        print(f"Successfully installed dependencies from {requirements_file}.")

        from cli.ai_models import create_json_file

        create_json_file()
    except subprocess.CalledProcessError as e:
        print(f"Installation failed: {e}")
