# TMACC-Manim

Install [Python 3.11+](https://www.python.org/downloads/) and set up a [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments). Inside it, install Manim and its dependencies with the following command:
```sh
pip install -r requirements.txt
```

To render and preview, either use the Manim Sideview Extension in VS Code, or run the following command:
```sh
cd TMACC && manim render -pql main.py
```

See Code in main.py and tmacc_anim.py

## Development

Install and use [pip-tools](https://pip-tools.readthedocs.io/en/stable/) to synchronize the pinned requirements files.
