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
        # TODO real exception handling if hit end of file system :P
        #      just prevent the inf loop for now
        if count == 20: return ''
    return requirements[0]


subprocess.run([sys.executable, "-m", "pip", "install", "-r", f"{find_requirements()}"])
