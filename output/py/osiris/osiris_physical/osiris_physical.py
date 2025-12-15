from osirisPORIS import *

class osiris_physical(osirisPORIS):
    # Go to ARCGengIIIPORIS.py, navigate to the ##### Action triggers ##### section
    # which is normally at the bottom of the class, and copy here the methods 
    # to start overriding them, in order to convert the virtual device into a physical one
    # Once this class has any content, remove the pass clause

    pass


thismodel = osiris_physical(1)

print("Let's test our model ",thismodel.getRoot().getName())
print("Current mode is ",thismodel.getRoot().getSelectedMode().getName())

print("")

print("----- BEGIN --------- XML dump of the model ------------------")
print("")

dom = thismodel.toXML()
pretty_xml_as_string = dom.toprettyxml(encoding="utf-8")
print(pretty_xml_as_string)
print("")
print("-----  END  --------- XML dump of the model ------------------")

print("")