# install-requirements

A module for automatically installing the `requirements.txt` file at runtime. So when prototyping, you don't have to type `python3 -m pip install -r requirements.txt` all the time.

```py
import rinstall  # isort: skip

# ^^^ KEEP FIRST! ^^^

import numpy as np

print(np.array([0, 1, 2]))
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
git clone https://github.com/yrom1/install-requirements.git
cd install-requirements
pip install .
```
