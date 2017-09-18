import xml.etree.ElementTree as ET
import logging

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
        self.logger = logging.getLogger('main.IPCXML')


    def getsymbolvalue(self, plctype):
        tree = ET.parse("PLC1.xml")
        root = tree.getroot()
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
    def getequipmentinfo(self):
        tree = ET.parse("SettingNew.xml")
        root = tree.getroot()
        info = {}
        for child in root.findall("EQUIPMENTLIST"):
                fo = []#设备配置
                for grandchild in child.findall("EQUIPMENT"):
                    #PLC 通讯接口是以太网
                    equiptype = grandchild.attrib['EQUIPMENTTYPE']
                    equipno = grandchild.attrib['EQUIPMENTNO']
                    if(grandchild.attrib['PLCINTERFACE'] == 'TCP'):
                        p = {} # PLC列表
                        for grandgrandchild in grandchild.findall('PLC_SETTING'):
                            for grandgrandgrandchild in grandgrandchild.findall('PLC'):
                                plcport = grandgrandgrandchild.attrib['PORT']
                                plcip = grandgrandgrandchild.attrib['IP']
                                plctype=grandgrandgrandchild.attrib['TYPE']
                                plcno = grandgrandgrandchild.attrib['NO']
                                p[plcno]=(plcport, plcip, plctype)
                    #PLC 通讯接口是485
                    else:
                        pass
                    s = {}
                    for ggchild in grandchild.findall('COMM_SETTING'):
                        for gggchild in ggchild.findall('SERIAL_COMM'):
                            serialport = gggchild.attrib['PORT']
                            serialno = gggchild.attrib['NO']
                            serialstopbit = gggchild.attrib['STOPBIT']
                            serialbytesize = gggchild.attrib['BYTESIZE']
                            serialparity = gggchild.attrib['PARITY']
                            serialbaudrate = gggchild.attrib['BAUDRATE']
                            s[serialno]=(serialport, serialstopbit, serialbytesize, serialparity, serialbaudrate)
                    fo = [equiptype,  p, s]
                info[equipno] = fo
        return info







