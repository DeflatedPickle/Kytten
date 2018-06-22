#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import kytten

classic = kytten.Theme("kytten/themes/classic")

classic_blue = kytten.Theme("kytten/themes/classic", override={
    "gui_color": [64, 128, 255, 255],
    "font_size": 14
})

classic = kytten.Theme(classic, override={
    "gui_color": [255, 235, 128, 255],
    "font_size": 12
})

felyne_light = kytten.Theme("kytten/themes/felyne", override={
    "text_color": [0, 0, 0, 255],
    "gui_color_light": [70, 70, 72, 255],
    "font_size": 12
})

felyne_dark = kytten.Theme(felyne_light, override={
    "text_color": [255, 255, 255, 255],
    "gui_color": [70, 70, 72, 255],
    "gui_color_light": [255, 255, 255, 255],
    "highlight_color": [100, 100, 102, 64],
    "font_size": 12
})
