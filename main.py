# coding:utf-8
import sys, os
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
# from qfluentwidgets import setTheme
from src.widgets.main_window import Window
from src.config.config import cfg

# enable dpi scale
if cfg.get(cfg.dpiScale) != "Auto":
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
    os.environ["QT_SCALE_FACTOR"] = str(cfg.get(cfg.dpiScale))
    

if __name__ == "__main__":
    """_
    main app __main__ can use by module -m e.g `python -m main`
    """

    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)
    w = Window()
    w.show()
    app.exec()
