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

s = "2020-01-25 16:30"
print(s[0:4])
print(s[5:7])
print(s[8:10])
print(s[11:13])
print(s[14:])