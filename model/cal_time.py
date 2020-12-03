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
        minus = (3 - first_index) + 15

        self.end_date = datetime.datetime(this_year, this_month, minus, 16, 30, 0)
        self.start_date = datetime.datetime(this_year, this_month, minus, 0, 0, 0)

    def calculate(self, query):
        self.db_connect.cursor.execute(query)
        rows = self.db_connect.cursor.fetchall()

        time_sum = 0

        for i in range(len(rows)):
            slice_year = int(rows[i][0][:4])
            slice_month = int(rows[i][0][5:7])
            slice_day = int(rows[i][0][8:10])
            slice_hour = int(rows[i][0][11:13])
            slice_minute = int(rows[i][0][14:])
            submit_time = datetime.datetime(slice_year, slice_month, slice_day, slice_hour, slice_minute)

            if self.start_date <= submit_time:
                time_sum += round((self.end_date - submit_time).microseconds / float(1000000)) + (
                        (self.end_date - submit_time).seconds + (self.end_date - submit_time).days * 24 * 3600)

        avg = time_sum // 990
        class_num = str(avg)

        return class_num