# Krita Script Name: Display selected layers X and Y top left position in the console
# Instructions: Run.
# Author: X-Raym
# Author URI: https://www.extremraym.com
# Repository: X-Raym/Krita-Scripts
# Repository URI: https://github.com/X-Raym/Krita-Scripts/
# Licence: GPL v3
# Krita: 4.0.0
# Version: 1.0
# Notes: This doesn't work in Krita 4.0 for now.

from krita import *

w = Krita.instance().activeWindow()
v = w.activeView()

nodes = v.selectedNodes()
for i, node in enumerate( nodes ):
    pos = node.position()
    print( node.name() + "\t" + str( pos.x() ) + "\t" + str( pos.y() ) )
