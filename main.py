from PLC import *
from IPCXML import *
import logging
from SqlLiteDB import *



logger=logging.getLogger('main')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.warning("log init")
if __name__ == '__main__':
    # p = PLC()
    # p.plcconnect('192.168.250.209', '192.168.250.4', 9600)
    # s=p.plcreadhrbit(1,1)
    # print(s)
    # p.plcwritehrbit(1 ,1, 1)
    # s=p.plcreadhrbit(1, 1)
    # print(s)
    # p.plcwritehrbit(0, 1, 1)
    # time.sleep(1)
    # p.plcclose()
    p=IPCXML()
    d=p.getsymbolvalue('IFAST_CY')
    logger.info(d.get('L4PdStep01').symbolname)
    s=SqlLiteDB('IPC.db')
    m=s.VerifyUser('zgw','123456')
    if m:
        logger.info('user passed')
    else:
        logger.info('user denied')