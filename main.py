from PLC import *
from IPCXML import *


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
    c=p.getsymbolvalue("IFAST_CY")
    print(c)