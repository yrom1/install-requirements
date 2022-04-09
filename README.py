with open("install.sh", "r") as f:
    INSTALL = f.read()
with open("test.py", "r") as f:
    TEST_FILE = f.read()
with open('TEST_OUTPUT.txt', 'r') as f:
    TEST_OUTPUT = f.read()
README = f"""\
# install-requirements

A module for automatically installing the `requirements.txt` file at runtime. So when prototyping, you don't have to type `python3 -m pip install -r requirements.txt` all the time.

```py
{TEST_FILE}\
```

Outputs:

```
{TEST_OUTPUT}\
```

## Installation

```
{INSTALL}\
```
"""

with open("README.md", "w") as f:
    f.write(README)
