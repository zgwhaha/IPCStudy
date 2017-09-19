import socket

class PLC:
    def __init__(self, symbolvaluelist):
        self.finsheadersa1=0
        self.finsheaderda1=0
        self.s=0
        self.symbolvaluelist = symbolvaluelist



    def plcconnect(self, localip, desip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((localip, 0))
        self.s.connect((desip, 9600))
        a = [0x46, 0x49, 0x4e, 0x53, 0x00, 0x00, 0x00, 0x0c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00]
        b = bytes(a)
        print(b)
        self.s.send(b)
        c=self.s.recv(24)
        print(c)
        if(c[15]!=0):
            print("error")
            return 1
        else:
            self.finsheadersa1=c[19]
            print(self.finsheadersa1)
            self.finsheaderda1=c[23]
            print(self.finsheaderda1)
            print("connect ok")
            return 0
    def plcclose(self):
        self.s.close()

    def plcwritehrbit(self,value, addr, bitno):
        t0 = 0x46
        t1 = 0x49
        t2 = 0x4e
        t3 = 0x53
        t4 = 0
        t5 = 0
        t6 = 0
        t7 = 27
        t8 = 0
        t9 = 0
        t10 = 0
        t11 = 2
        t12 = 0
        t13 = 0
        t14 = 0
        t15 = 0
        #header
        t16 = 0x80
        t17 = 0
        t18 = 0x02
        t19 = 0
        t20 = self.finsheaderda1
        t21 = 0
        t22 = 0
        t23 = self.finsheadersa1
        t24 = 0
        t25 = 0x15
        #cmd
        t26 = 0x01
        t27 = 0x02
        #position
        t28 = 0x32
        t29 = ((addr & 0xFF00) >> 8)
        t30 = (addr & 0xFF)
        t31 = (bitno & 0xFF)
        t32 = 0x00
        t33 = 0x01
        t34 = value
        temp1=bytes([t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21,
                    t22, t23, t24, t25, t26, t27, t28, t29, t30, t31, t32, t33, t34] )
        print(temp1)
        self.s.send(temp1)
        recvdata=self.s.recv(100)
        print(recvdata)
        if(recvdata[28]!=0):
            print("write error")
            return -1
        else:
            print("write success")
            return 0

    def plcwritehrword(self, beginaddr, num):
        pass

    def plcreadhrbit(self, addr, bitno):
        t0 = 0x46
        t1 = 0x49
        t2 = 0x4e
        t3 = 0x53
        t4 = 0
        t5 = 0
        t6 = 0
        t7 = 26
        t8 = 0
        t9 = 0
        t10 = 0
        t11 = 2
        t12 = 0
        t13 = 0
        t14 = 0
        t15 = 0
        #header
        t16 = 0x80
        t17 = 0
        t18 = 0x02
        t19 = 0
        t20 = self.finsheaderda1
        t21 = 0
        t22 = 0
        t23 = self.finsheadersa1
        t24 = 0
        t25 = 0x15
        #cmd
        t26 = 0x01
        t27 = 0x01
        #position
        t28 = 0x32
        t29 = ((addr & 0xFF00) >> 8)
        t30 = (addr & 0xFF)
        t31 = (bitno & 0xFF)
        t32 = 0x00
        t33 = 0x01
        temp=bytes([t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21,
                    t22, t23, t24, t25, t26, t27, t28, t29, t30, t31, t32, t33] )
        print(temp)
        self.s.send(temp)
        recvdata=self.s.recv(100)
        print(recvdata)
        if(recvdata[28]!=0):
            print("get error")
            return -1
        else:
            print("get success")
            return recvdata[30]
    def plcreadhrword(self,beginaddr,num):
        pass
