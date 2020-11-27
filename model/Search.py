from model.Student import Student
import pymysql

class Search :

    def __init__(self,num,ip,phone):
        self.ip_address = ip
        self.phone_address = phone
        self.internet_use = False
        self.student_num = num

    def __str__(self):
        return Student.__str__(self)+f'\n학생의 ip 주소는 {self.ip_address}이고,' \
                                 f' 핸드폰 ip 주소는 {self.phone_address}입니다.'

    def set_ip_address(self):
        pass

    def set_phone_address(self):
        pass

    def set_internet_use(self):
        #인터넷 사용여부
        pass

    #db select
    def select_all(self):
        conn = pymysql.connect(host="localhost",user="root",password="123456",db="ipc")
        try :
            with conn.cursor() as curs :
                sql = "SELECT * FROM ip_table"
                curs.execute(sql)
                rs = curs.fetchall()

                for row in rs :
                    print(row)
        finally:
            conn.close()

    #db insert
    def insert_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="123456", db="ipc")
        try:
            with conn.cursor() as curs:
                sql = "INSERT INTO ip_table VALUES (%s, %s, %s)"
                curs.execute(sql, (self.student_num, self.ip_address, self.phone_address))
            conn.commit()
        finally:
            conn.close()

    #db search (select)
    def search_ip(self,num):
        conn = pymysql.connect(host="localhost", user="root", password="123456", db="ipc")
        try:
            with conn.cursor() as curs:
                sql = "SELECT * FROM ip_table WHERE hakbun = %s"
                curs.execute(sql,num)
                rs = curs.fetchone()
                print(rs)
                print(f'학번 : {rs[0]}  ip : {rs[1]}  phone : {rs[2]}')
        finally:
            conn.close()

    #internet o or x
    def check_internet(self):
        import socket
        try :
            socket.gethostbyaddr(self.ip_address)
            print("connected")
        except socket.herror :
            print("Not connected")

        try :
            socket.gethostbyaddr(self.phone_address)
            print("connected")
        except socket.herror :
            print ("Unknown host")


if __name__ == '__main__':
    s = Search(1110,'10.96.122.139','10.96.122.140')
    s.select_all()



