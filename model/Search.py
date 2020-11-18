from model.Student import Student
import pymysql

class Search :

    def __init__(self,num,ip,phone):
        self.ip_address = ip
        self.phone_address = phone
        self.internet_use = False
        self.student_num = Student(num).student_num

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
        conn = pymysql.connect(host="localhost",user="root",password="123456",db="ip")
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
        conn = pymysql.connect(host="localhost", user="root", password="123456", db="ip")
        try:
            with conn.cursor() as curs:
                sql = "INSERT INTO ip_table VALUES (%s, %s, %s)"
                curs.execute(sql, (self.student_num, self.ip_address, self.phone_address))
            conn.commit()
        finally:
            conn.close()


if __name__ == '__main__':
    s = Search(2410,'10.96.122.139','10.96.122.140')
    s.select_all()



