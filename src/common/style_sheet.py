# coding: utf-8
from enum import Enum

from qfluentwidgets import StyleSheetBase, Theme, qconfig


class StyleSheet(StyleSheetBase, Enum):
    """ Style sheet  """

    LINK_CARD = "link_card"
    SAMPLE_CARD = "sample_card"
    HOME_WIDGET_STYLE = "home_interface"
    SETTING_INTRFACE_STYLE = "setting_interface"

    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return f"./resource/styles/{theme.value.lower()}/{self.value}.qss"
