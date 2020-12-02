import datetime

#월 - 0
#화 - 1
#수 -2

#1/1 금 -  5  1/6 수   - 2
this_year = datetime.datetime.today().year
this_month = datetime.datetime.today().month
now = datetime.datetime.now()


a = datetime.date(this_year,this_month,1).weekday()
print(a)
minus = 0
minus = (2-a)+8
if minus < 10:
    print(str(this_year) + "-" + str(this_month) + "-0" + str(minus))
else:
    print(str(this_year) + "-" + str(this_month) + "-" + str(minus))

print(minus)
