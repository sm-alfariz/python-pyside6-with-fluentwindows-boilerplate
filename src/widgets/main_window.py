# coding:utf-8

import sys

from PySide6.QtCore import QUrl
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
    InfoBadgePosition
)
from qfluentwidgets import FluentIcon as FIF
from src.widgets.blank_widget import BlankWidget as Widget 



class Window(FluentWindow):

    def __init__(self):
        super().__init__()
        # create sub interface
        self.homeInterface = Widget("Search Interface", self)
        self.musicInterface = Widget("Music Interface", self)
        self.videoInterface = Widget("Video Interface", self)
        self.folderInterface = Widget("Folder Interface", self)
        self.settingInterface = Widget("Setting Interface", self)
        self.albumInterface = Widget("Album Interface", self)
        self.albumInterface1 = Widget("Album Interface 1", self)
        self.albumInterface2 = Widget("Album Interface 2", self)
        self.albumInterface1_1 = Widget("Album Interface 1-1", self)

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, "Home")
        self.addSubInterface(self.musicInterface, FIF.MUSIC, "Music library")
        self.addSubInterface(self.videoInterface, FIF.VIDEO, "Video library")

        self.navigationInterface.addSeparator()

        self.addSubInterface(
            self.albumInterface, FIF.ALBUM, "Albums", NavigationItemPosition.SCROLL
        )
        self.addSubInterface(
            self.albumInterface1, FIF.ALBUM, "Album 1", parent=self.albumInterface
        )
        self.addSubInterface(
            self.albumInterface1_1, FIF.ALBUM, "Album 1.1", parent=self.albumInterface1
        )
        self.addSubInterface(
            self.albumInterface2, FIF.ALBUM, "Album 2", parent=self.albumInterface
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
        item = self.navigationInterface.widget(self.videoInterface.objectName())
        InfoBadge.attension(
            text=9,
            parent=item.parent(),
            target=item,
            position=InfoBadgePosition.NAVIGATION_ITEM,
        )

        item_home = self.navigationInterface.widget(self.homeInterface.objectName())
        InfoBadge.attension(
            text=11,
            parent=item_home.parent(),
            target=item_home,
            position=InfoBadgePosition.NAVIGATION_ITEM,
        )

        # NOTE: enable acrylic effect
        self.navigationInterface.setAcrylicEnabled(True)

        # disable pop animation
        # self.stackedWidget.setAnimationEnabled(False)

    def initWindow(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon("resource/img/icon.png"))
        self.setWindowTitle("PyQt-Fluent-Widgets")
        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.navigationInterface.setCollapsible(False)        
        # 2. (Optional but recommended) Force the sidebar to maintain a specific expanded width
        self.navigationInterface.setExpandWidth(280)  # Width in pixels
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


if __name__ == "__main__":
    setTheme(Theme.DARK)

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
