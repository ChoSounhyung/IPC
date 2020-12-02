import datetime

#월 - 0
#화 - 1
#수 -2

#1/1 금 -  5  1/6 수   - 2
this_year = datetime.datetime.today().year
this_month = datetime.datetime.today().month
now = datetime.datetime.now()
print(now)

a = datetime.date(this_year,this_month,1).weekday()
print(a)
minus = 0
minus = (2-a)+8

print(minus)
