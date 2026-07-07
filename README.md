## this is python Desktop App boilerplate UI FrameWork use PySide6 + [Fluent-Widgets](https://qfluentwidgets.com/)


### Boilerplate Project Directory Structure
For a robust PySide6 desktop application, you should separate your logic from your User Interface files. Here is a scalable project tree example

```shell
├── resource              #your resource like icon and image
│   ├── img
│   │   └── icon.png
│   └── styles
│       └── styles.qss
├── src
│   ├── components
│   │   ├── __init__.py
│   │   └── sample_card.py
│   ├── config
│   │   └── __init__.py
│   ├── controllers
│   │   └── __init__.py
│   ├── models
│   │   └── __init__.py
│   ├── utils
│   │   └── __init__.py
│   └── widgets
│       ├── __init__.py
│       ├── blank_widget.py
│       └── main_window.py
├── main.py
└── requirements.txt

```
### install instruction
create your virtual envirotmen `python3 -m venv .venv` will be create virtual env at .venv folder on current project
after succesfully then activate virtual env with ` source .venv/bin/activate ` then install library with `pip install -r requirements.txt`