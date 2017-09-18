from PLC import *
import logging

#TODO
class IFast:
    def __init__(self):
        self.logger = logging.getlogger('main.IFast')
        self.PLCList = {}




    def IFastInit(self,eqinfo):
        for eq in eqinfo:
            if isinstance(eq, str):
                self.logger.info('equipment type is'+eq)
            if isinstance(eq,dict):
                for subeq in eq.items():
                    if subeq is 'PLC':#need to rewrite
                        p=PLC()
                        p.plcconnect()
        pass



