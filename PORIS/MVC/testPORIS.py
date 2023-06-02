from PORIS import PORIS
from PORISValue import PORISValue
from PORISLib import PORISLib
from ValueFormatter import ValueFormatter
from xml.dom import minidom


prueba = PORIS("prueba")
hijo = PORISValue("hijo")
formatter = ValueFormatter("text", 1)
hijo.setFormatter(formatter)
padre = PORISLib("padre")
print(prueba.toString())
print("adding destination",hijo.toString())
prueba.addDestination(hijo)
prueba.addSource(padre)
rootInstr = minidom.Document()
xmlInstr = rootInstr.createElement('poris')
rootInstr.appendChild(xmlInstr)
e = prueba.toXML(rootInstr,False)
h = hijo.toXML(rootInstr, False)
p = padre.toXML(rootInstr, False)
xmlInstr.appendChild(h)
xmlInstr.appendChild(e)
#xmlInstr.appendChild(p)
pretty_xml_as_string = rootInstr.toprettyxml()
print(pretty_xml_as_string)
