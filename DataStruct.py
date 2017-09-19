



#PLC symbol value
class SymbolValue:
    __slots__=('symbolname', 'datatype', 'channelno', 'bitno', 'comment')

    def __init__(self,symbolname, datatype, channelno, bitno, comment):
        self.symbolname = symbolname
        self.datatype = datatype
        self.channelno = channelno
        self.bitno = bitno
        self.comment = comment


#serial port setting
class SerialEquipmentSetting:
    __slots__ = ('port', 'baudrate', 'stopbit', 'parity', 'bytesize', 'Name', 'Comment')

    def __init__(self, port, baudrate, stopbit, parity, bytesize, name, comment):
        self.port = port
        self.baudrate = baudrate
        self.stopbit = stopbit
        self.parity = parity
        self.bytesize = bytesize
        self.Name = name
        self.Comment = comment


class NetworkEquipmentSetting:

    __slots__ = ('Port', 'IP', 'Comment')

    def __init__(self, port, ip, comment):
        self.Port = port
        self.IP = ip
        self.Comment = comment



class EquipmentSetting:

    __slots__ = ('EquipNO', 'EquipType', 'LocalIP', 'PLCSerialList', 'PLCNetworkList', 'SerialEquipmentList')

    def __init__(self,equiptye, localip, plcseriallist, plcnetworklist, serialequipmentlist):
        self.EquipType= equiptye
        self.PLCSerialList = plcseriallist
        self.PLCNetworkList = plcnetworklist
        self.SerialEquipmentList = serialequipmentlist
        self.LocalIP = localip