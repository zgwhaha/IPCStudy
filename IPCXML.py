import xml.etree.ElementTree as ET
import logging
import DataStruct as DS


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
                    symbol = DS.SymbolValue(symbolename, datatype, channelno, bitno, comment)
                    d[symbolename] = symbol
                break
        return d
    def getequipmentinfo(self):
        tree = ET.parse("SettingNew.xml")
        root = tree.getroot()
        info = {}
        for child in root.findall("EQUIPMENTLIST"):
            for grandchild in child.findall("EQUIPMENT"):
                #PLC 通讯接口是以太网
                equiptype = grandchild.attrib['EQUIPMENTTYPE']
                equipno = grandchild.attrib['EQUIPMENTNO']
                if(grandchild.attrib['PLCINTERFACE'] == 'TCP'):
                    for grandgrandchild in grandchild.findall('IPCLOCALIP'):
                        localip = grandgrandchild.attrib['IP']
                    p = {} # PLC列表
                    for grandgrandchild in grandchild.findall('PLC_SETTING'):
                        for grandgrandgrandchild in grandgrandchild.findall('PLC'):
                            plcport = grandgrandgrandchild.attrib['PORT']
                            plcip = grandgrandgrandchild.attrib['IP']
                            plctype=grandgrandgrandchild.attrib['TYPE']
                            plcno = grandgrandgrandchild.attrib['NO']
                            p[plcno] = DS.NetworkEquipmentSetting(plcport, plcip, plctype)
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
                        s[serialno]=DS.SerialEquipmentSetting(serialport,serialbaudrate, serialstopbit, serialparity, serialbytesize, serialno, '')
                info[equipno] = DS.EquipmentSetting(equiptype, localip, {}, p, s)
        return info







