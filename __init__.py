import subprocess
import sys
from pathlib import Path

def find_requirements() -> str:
    current_directory = "."
    count = 1
    while not (
        requirements := list(
            map(
                lambda x: str(x.resolve()),
                Path(current_directory).glob("requirements.txt"),
            )
        )
    ):
        current_directory = "../"
        current_directory = current_directory * count
        count += 1
        # TODO real exception handling if hit end of file system
        #      just prevent the inf loop for now
        if count == 20:
            raise RuntimeError('Cannot find requirements.txt file in parent directories of import statement!')
    return requirements[0]

def run_install_subprocess() -> None:
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", f"{find_requirements()}"])

def main() -> None:
    run_install_subprocess()

main()
