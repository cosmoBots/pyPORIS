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
padre.addPORISItem(prueba)
xmlDocument = minidom.Document()
xmlInstr = xmlDocument.createElement('poris')
xmlDocument.appendChild(xmlInstr)
e = prueba.toXML(xmlDocument,False)
h = hijo.toXML(xmlDocument, False)
p = padre.toXML(xmlDocument)
xmlInstr.appendChild(h)
xmlInstr.appendChild(e)
#xmlInstr.appendChild(p)
pretty_xml_as_string = xmlDocument.toprettyxml()
print(pretty_xml_as_string)
