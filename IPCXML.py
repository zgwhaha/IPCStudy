import xml.etree.ElementTree as ET

class SymbolValue:
    __slots__=('symbolname', 'datatype', 'channelno', 'bitno', 'comment')

    def __init__(self,symbolname, datatype, channelno, bitno, comment):
        self.symbolname = symbolname
        self.datatype = datatype
        self.channelno = channelno
        self.bitno = bitno
        self.comment = comment

class IPCXML:

    def __init__(self):
        pass

    def getsymbolvalue(self, plctype):
        tree = ET.parse("PLC1.xml")
        root = tree.getroot()
        print(root)
        print(root.tag)
        print(root.attrib)
        d = {}
        for child in root:
            if(plctype == child.tag):
                for grandchild in child.findall('PLCSYMBOL'):
                    symbolename = grandchild.attrib['SymbolName']
                    channelno = grandchild.attrib['ChannelNo']
                    bitno = grandchild.attrib['BitNo']
                    datatype = grandchild.attrib['DataType']
                    comment = grandchild.attrib['Comment']
                    symbol = SymbolValue(symbolename, datatype, channelno, bitno, comment)
                    d[symbolename] = symbol
                break
        return d
