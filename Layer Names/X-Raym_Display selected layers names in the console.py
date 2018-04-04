# Krita Script Name: Add prefix and suffix to all layers names
# Instructions: Run.
# Author: X-Raym
# Author URI: https://www.extremraym.com
# Repository: X-Raym/Krita-Scripts
# Repository URI: https://github.com/X-Raym/Krita-Scripts/
# Licence: GPL v3
# Krita: 4.0.0
# Version: 1.0

# Based on https://api.kde.org/extragear-api/graphics-apidocs/krita/libs/libkis/html/classView.html#a6e31fa37bb4115f40431c3c7352bc763
# https://forum.kde.org/viewtopic.php?f=139&t=151732

from krita import *

w = Krita.instance().activeWindow()
v = w.activeView()

nodes = v.selectedNodes()
for i, node in enumerate( nodes ):
    print( node.name() )
