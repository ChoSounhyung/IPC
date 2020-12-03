import pymysql

class DbConnect :
    def __init__(self):
        self.mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="123456",
            db="ipc"
        )
        self.cursor = self.mydb.cursor()
