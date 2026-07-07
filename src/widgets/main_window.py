# coding:utf-8

import sys

from PySide6.QtCore import QUrl, QTimer
from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtWidgets import QApplication
from qfluentwidgets import (
    NavigationItemPosition,
    MessageBox,
    setTheme,
    Theme,
    FluentWindow,
    NavigationAvatarWidget,
    InfoBadge,
    InfoBadgePosition,
    SystemThemeListener,
    isDarkTheme
)
from qfluentwidgets import FluentIcon as FIF
from src.widgets.blank_widget import BlankWidget as Widget 
from src.widgets.home_window import HomeInterface
from src.config.config import cfg


class Window(FluentWindow):

    def __init__(self):
        super().__init__()
        # create system theme listener
        self.themeListener = SystemThemeListener(self)
        # create sub interface
        self.homeInterface = HomeInterface(self)
        self.tasksInterface = Widget("Tasks", self)
        self.contactsInterface = Widget("Contacts", self)
        self.folderInterface = Widget("Folder", self)
        self.settingInterface = Widget("Setting", self)
        self.menu = Widget("Menu Item", self)
        self.menu1 = Widget("Menu Item 1", self)
        self.menu2 = Widget("Menu Item 2", self)
        self.menu1_1 = Widget("Menu Item 1-1", self)

        self.initNavigation()
        self.initWindow()
        
        # start theme listener
        self.themeListener.start()

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, "Home")
        self.addSubInterface(self.tasksInterface, FIF.CHECKBOX, "Tasks")
        self.addSubInterface(self.contactsInterface, FIF.PEOPLE, "Contatcs")

        self.navigationInterface.addSeparator()

        self.addSubInterface(
            self.menu, FIF.DOCUMENT, "Menu", NavigationItemPosition.SCROLL
        )
        self.addSubInterface(
            self.menu1, FIF.DOCUMENT, "Menu 1", parent=self.menu
        )
        self.addSubInterface(
            self.menu1_1, FIF.DOCUMENT, "Menu 1.1", parent=self.menu1
        )
        self.addSubInterface(
            self.menu2, FIF.DOCUMENT, "Menu 2", parent=self.menu
        )
        self.addSubInterface(
            self.folderInterface,
            FIF.FOLDER,
            "Folder library",
            NavigationItemPosition.SCROLL,
        )

        # add custom widget to bottom
        self.navigationInterface.addWidget(
            routeKey="avatar",
            widget=NavigationAvatarWidget("Fluent-Widgets", "resource/img/icon.png"),
            onClick=self.showMessageBox,
            position=NavigationItemPosition.BOTTOM,
        )

        self.addSubInterface(
            self.settingInterface,
            FIF.SETTING,
            "Settings",
            NavigationItemPosition.BOTTOM,
        )
        
        # add badge to navigation item
        item_tasks = self.navigationInterface.widget(self.tasksInterface.objectName())
        InfoBadge.info(
            text=9,
            parent=item_tasks.parent(),
            target=item_tasks,
            position=InfoBadgePosition.NAVIGATION_ITEM,
        )

        item_contacts = self.navigationInterface.widget(self.contactsInterface.objectName())
        InfoBadge.attension(
            text=11,
            parent=item_contacts.parent(),
            target=item_contacts,
            position=InfoBadgePosition.NAVIGATION_ITEM,
        )

        # NOTE: enable acrylic effect
        self.navigationInterface.setAcrylicEnabled(True)

        # disable pop animation
        # self.stackedWidget.setAnimationEnabled(False)

    def initWindow(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon("resource/img/icon.png"))
        self.setWindowTitle("PySide6 + FluentWidgets")
        self.setMicaEffectEnabled(cfg.get(cfg.micaEnabled))
        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.navigationInterface.setCollapsible(True)        
        # 2. (Optional but recommended) Force the sidebar to maintain a specific expanded width
        self.navigationInterface.setExpandWidth(220)  # Width in pixels
        # (This must be called after setExpandWidth)
        self.navigationInterface.setMinimumExpandWidth(800)
  
        self.navigationInterface.expand(useAni=True)

    def showMessageBox(self):
        w = MessageBox(
            "支持作者🥰",
            "个人开发不易，如果这个项目帮助到了您，可以考虑请作者喝一瓶快乐水🥤。您的支持就是作者开发和维护项目的动力🚀",
            self,
        )
        w.yesButton.setText("来啦老弟")
        w.cancelButton.setText("下次一定")

        if w.exec():
            QDesktopServices.openUrl(QUrl("https://afdian.net/a/zhiyiYo"))
    
    def closeEvent(self, e):
        self.themeListener.terminate()
        self.themeListener.deleteLater()
        super().closeEvent(e)

    def _onThemeChangedFinished(self):
        super()._onThemeChangedFinished()

        # retry
        if self.isMicaEffectEnabled():
            QTimer.singleShot(
                100,
                lambda: self.windowEffect.setMicaEffect(self.winId(), isDarkTheme()),
            )

if __name__ == "__main__":
    # setTheme(Theme.DARK)

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
