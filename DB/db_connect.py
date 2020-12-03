import pymysql

class DbConnect :
    def __init__(self):
        self.mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="s2019w36",
            db="ipc"
        )
        self.cursor = self.mydb.cursor()
