import sqlite3




class SqlLiteDB:
    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)
        self.cursor = self.conn.cursor()


    def DBClose(self):
        self.cursor.close()
        self.conn.close()

    def VerifyUser(self,user,password):
        sqlstr = "select * from USER where username = '"+user+"' and password ='"+password+"'"
        self.cursor.execute(sqlstr)
        values = self.cursor.fetchall()
        self.DBClose()
        if values:
            return True
        else:
            return  False