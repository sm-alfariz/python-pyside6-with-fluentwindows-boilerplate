# coding:utf-8
import sys

from PySide6.QtWidgets import QApplication
from qfluentwidgets import setTheme, Theme
from src.widgets.main_window import Window


if __name__ == "__main__":
    """_
    main app __main__ can use by module -m e.g python -m main
    """
    setTheme(Theme.DARK)
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
