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

    #학생 - 점수 저장하기
    def input_data(self):
        pass

    #100점이 아닐경우, 이유 적는 창 띄우기
    def add_reason(self):

        pass

    #선생님 - 점수 보여주기
    def show_data(self):
        #선생님 화면
        #100점이 아닐 경우, 행의 색(노란색)으로 표현
        pass

    #100점 미만인 학생만 보여주기
    def under_100(self):
        pass

    #내 PC 지키미를 안 한 학생만 보여주기
    #초기화한 상태에서 0점인 애들만
    def do_not_myPc(self):
        pass

    #반별로 통계 보여주기
    def show_class_statistics(self):
        pass



