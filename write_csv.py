
#input date
date = input('날짜를 입력하세요 : ')


myCsRow = "20.11.12,2302,강채현,100,null\n"
with open('mypc_dummy.csv','a',encoding='utf-8') as fd :
  fd.write(myCsRow)