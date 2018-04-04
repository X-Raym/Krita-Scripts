# Krita Script Name: Add prefix and suffix to all layers names
# Instructions: Run.
# Author: X-Raym
# Author URI: https://www.extremraym.com
# Repository: X-Raym/Krita-Scripts
# Repository URI: https://github.com/X-Raym/Krita-Scripts/
# Licence: GPL v3
# Krita: 4.0.0
# Version: 1.0

import sys
from krita import *

# USER CONFIG AREA ##################

prefix = "prefix_"
suffix = "_suffix"

####################################

doc = Krita.instance().activeDocument()

root_node = doc.rootNode()
layers = root_node.childNodes()

for i, layer in enumerate( layers ):
    new_name = prefix + layer.name() + suffix
    print( layer.name() + " =>" + new_name )
    layer.setName( new_name )
