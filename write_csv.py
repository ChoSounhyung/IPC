import csv

#fields = ['날짜','학번','이름','점수','이유(100점 미만일 경우)']
myCsRow = "20.11.12,2302,강채현,100,null\n"
with open('mypc_dummy.csv','a',encoding='utf-8') as fd :
  fd.write(myCsRow)