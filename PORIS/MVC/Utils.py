from xml.dom import minidom

def setTextContent(doc: minidom.Document, e: minidom.Element, text: str):
    childList = e.childNodes
    nodeFound = None
    for child in childList:
        if child.getNodeType() == minidom.Node.TEXT_NODE:
            nodeFound = child

    if nodeFound is not None:
        nodeFound.setNodeValue(text)
    
    else:
        e.appendChild(doc.createTextNode(text))

