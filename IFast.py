from PLC import *
import logging
from IPCXML import *
import DataStruct as DS


class IFast:
    def __init__(self):
        self.logger = logging.getLogger('main.IFast')
        self.PLCList = {}




    def IFastInit(self,eqinfo):
        if isinstance(eqinfo, DS.EquipmentSetting):
            for plcname,plcsetting in eqinfo.PLCNetworkList.items():
                i=IPCXML()
                symbolvalue = i.getsymbolvalue(eqinfo.EquipType)
                p=PLC(symbolvalue)
                # p.plcconnect(eqinfo.LocalIP,plcsetting.IP, plcsetting.Port)
            self.logger.info("IFast Init Success")




