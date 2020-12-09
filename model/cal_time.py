from DB.db_connect import DbConnect
import datetime
import matplotlib

class CalTime:
    def __init__(self):
        self.db_connect = DbConnect()

        matplotlib.rcParams['font.family'] = 'Malgun Gothic'
        matplotlib.rcParams['axes.unicode_minus'] = False

        this_year = datetime.datetime.today().year
        this_month = datetime.datetime.today().month

        first_index = datetime.date(this_year, this_month, 1).weekday()  # 매달 1일의 인덱스
        third_week_index = (3 - first_index) + 15                       #셋째주 목요일
        pre_third_week_index = (2 - first_index) + 15                   # 셋째주 수요일

        self.end_date = datetime.datetime(this_year, this_month, third_week_index, 16, 30, 0)
        self.start_date = datetime.datetime(this_year, this_month, third_week_index, 0, 0, 0)
        #12월이면 년도와 월이 달라짐
        if this_month == 12:
            self.pre_after_month = datetime.datetime(this_year + 1, this_month - 11, pre_third_week_index, 23, 59, 59)
        else:
            self.pre_after_month = datetime.datetime(this_year, this_month + 1, pre_third_week_index, 23, 59, 59)

    def calculate(self, query):
        self.db_connect.cursor.execute(query)
        rows = self.db_connect.cursor.fetchall()

        time_sum = 0

        for i in range(len(rows)):
            # query문의 this_month에서 추출
            slice_year = int(rows[i][0][:4])
            slice_month = int(rows[i][0][5:7])
            slice_day = int(rows[i][0][8:10])
            slice_hour = int(rows[i][0][11:13])
            slice_minute = int(rows[i][0][14:])
            # 제출한 시간
            submit_time = datetime.datetime(slice_year, slice_month, slice_day, slice_hour, slice_minute)

            # 기한안에 제출 했으면(이번달 셋째주 목요일 00:00 ~ 16:30)
            if self.start_date < submit_time:
                # 시간을 숫자로 변환
                time_sum += round((self.end_date - submit_time).microseconds / float(1000000)) + (
                        (self.end_date - submit_time).seconds + (self.end_date - submit_time).days * 24 * 3600)

        # 제출 시간의 평균
        avg = time_sum // 990
        class_num = str(avg)

        return class_num