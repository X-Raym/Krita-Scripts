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
