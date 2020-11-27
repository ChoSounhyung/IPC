from model.Student import Student
import pymysql
import datetime

class MyPc :

    def __init__(self,num,score):
        self.student_num = Student(num).student_num
        self.this_month = ""  #오늘 날짜
        self.score = score
        self.reason = "empty"


    def __str__(self):
        return f'{self.date}의 {self.student_num}번 학생의 내 PC 지키미 점수는 {self.score}입니다.'

    def set_date(self):
        #날짜 업데이트 - 1달에 한번씩
        conn = pymysql.connect(host="localhost", user="root", password="123456", db="ipc")
        try:
            with conn.cursor() as curs:
                sql = "UPDATE mypc_table SET this_month=%s"
                this_month = datetime.date.today().month
                curs.execute(sql, (this_month))
            conn.commit()
        finally:
            conn.close()

    #학생 - 점수 저장하기
    def update_data(self,score):
        if score < 100 :
            reason = "처음 초기값 (나중에 입력받은 변수로 바꾸기)"
            self.add_reason(reason)
        conn = pymysql.connect(host="localhost", user="root", password="123456", db="ipc")
        try:
            with conn.cursor() as curs:
                sql = "UPDATE mypc_table SET score=%s where hakbun = %s"
                curs.execute(sql, (score,self.student_num))
            conn.commit()
        finally:
            conn.close()

    #100점이 아닐경우, 이유 적는 창 띄우기
    def add_reason(self,reason):
        #reason 입력받기
        conn = pymysql.connect(host="localhost", user="root", password="123456", db="ipc")
        try:
            with conn.cursor() as curs:
                sql = "UPDATE mypc_table SET reason=%s where hakbun = %s"
                this_month = datetime.date.today().month
                curs.execute(sql, (reason, self.student_num))
            conn.commit()
        finally:
            conn.close()

    #선생님 - 점수 보여주기
    def show_data(self):
        #선생님 화면
        #100점이 아닐 경우, 행의 색(노란색)으로 표현
        pass

    #100점 미만인 학생만 보여주기
    def under_100(self):
        conn = pymysql.connect(host="localhost", user="root", password="123456", db="ipc")
        try:
            with conn.cursor() as curs:
                sql = "SELECT * FROM mypc_table where score<100"
                curs.execute(sql)
                rs = curs.fetchall()

                for row in rs:
                    print(f'학번 : {row[0]}  오늘 : {row[1]}  score : {row[2]}  reason : {row[3]}')
        finally:
            conn.close()


    #내 PC 지키미를 안 한 학생만 보여주기
    #초기화한 상태에서 0점인 애들만
    def do_not_myPc(self):
        conn = pymysql.connect(host="localhost", user="root", password="123456", db="ipc")
        try:
            with conn.cursor() as curs:
                sql = "SELECT * FROM mypc_table where score=0"
                curs.execute(sql)
                rs = curs.fetchall()

                print("---------내 PC 지킴이를 아직 하지 않은 학생---------")
                for row in rs:
                    print(f'학번 : {row[0]}  오늘 : {row[1]}  score : {row[2]}  reason : {row[3]}')
        finally:
            conn.close()

    #반별로 통계 보여주기
    def show_class_statistics(self):
        pass

if __name__ == '__main__':
    a = MyPc(2401,0)
    a.set_date()




