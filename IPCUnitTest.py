import unittest
from IPCXML import *
from SqlLiteDB import  *
from PLC import *


class TESTIPCXML(unittest.TestCase):
    def test_Init(self):
        pass
    def test_getsymbolvalue(self):
        plctypes=('IFAST_CY','IFAST_TS', 'IFAST_SY', 'IPACK_JXS', 'IPACK_FB', 'ITRANS_DG1', 'ITRANSDG2')
        for plctype in plctypes:
            I=IPCXML();
            d=I.getsymbolvalue(plctype)

class TESTPLC(unittest.TestCase):
    def test_Init(self):
        pass


class TESTSqliteDB(unittest.TestCase):
    def test_Init(self):
        s=SqlLiteDB('IPC.db')
        pass


if __name__ == '__main__':
    unittest.main()