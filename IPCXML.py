import xml.etree.ElementTree as ET


class IPCXML:

    def __init__(self):
        pass

    def getsymbolvalue(self,plctype):
        tree = ET.ElementTree("PLC1.xml")
        root = tree.getroot();
        print(root)
        return 0
