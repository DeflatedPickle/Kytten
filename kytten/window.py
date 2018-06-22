#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

from .dialog import Dialog
from .frame import Frame
from .layout import HorizontalLayout, VerticalLayout, VALIGN_BOTTOM, ANCHOR_TOP_RIGHT
from .widgets import Graphic, Label
from .button import Button


class Window(Dialog):
    def __init__(self, title, content, **kwargs):
        Dialog.__init__(self, content=
            VerticalLayout([
                HorizontalLayout([
                    Graphic(path=["titlebar", "left"], is_expandable=True),
                    Frame(Label(title, path=["titlebar"]),
                          path=["titlebar", "center"]),
                    Frame(HorizontalLayout([Button("x", on_click=self.teardown)], padding=0), path=["titlebar", "right"],
                          is_expandable=True, anchor=ANCHOR_TOP_RIGHT),
                ], align=VALIGN_BOTTOM, padding=0),
                Frame(content, path=["titlebar", "frame"], is_expandable=True),
            ], padding=0), **kwargs)
