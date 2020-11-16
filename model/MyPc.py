from model.Student import Student
class MyPc :

    def __init__(self,num,score):
        self.student_num = Student(num).student_num
        self.date = ""  #오늘 날짜
        self.score = score


    def __str__(self):
        return f'{self.date}의 {self.student_num}번 학생의 내 PC 지키미 점수는 {self.score}입니다.'

    def set_date(self):
        #날짜 바꿀 경우
        pass

    def set_score(self):
        pass

    def add_reason(self):
        #100점이 아닐 경우, 이유를 적고 데이터 전송
        #commit test
        pass

    def show_data(self):
        #선생님 화면
        #1-1, 1-2, 1-3, 2 (기획서)
        pass

