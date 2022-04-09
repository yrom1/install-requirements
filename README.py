with open("install.sh", "r") as f:
    INSTALL = f.read()
with open("test.py", "r") as f:
    TEST_FILE = f.read()
README = f"""\
# install_requirements

A module for automatically installing the `requirements.txt` file at runtime. So when prototyping, you don't have to type `python3 -m pip install -r requirements.txt` all the time.

```py
{TEST_FILE}\
```

Outputs:

```
Collecting numpy
  Using cached numpy-1.22.3-cp310-cp310-macosx_11_0_arm64.whl (12.8 MB)
Installing collected packages: numpy
Successfully installed numpy-1.22.3
[0 1 2]
```

## Installation

```
{INSTALL}\
```
"""

with open("README.md", "w") as f:
    f.write(README)
