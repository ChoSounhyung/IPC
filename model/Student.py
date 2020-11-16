class Student :

    def __init__(self, student_num):
        self.student_num = student_num

    def __str__(self):
        return f'학생의 학번은 {self.student_num}입니다.'

    def set_studentNum(self):
        pass