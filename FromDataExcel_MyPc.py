import pymysql as MySQLdb
import xlrd

tumbler = xlrd.open_workbook("data/mypc_dummy.xlsx")
sheet = tumbler.sheet_by_name("Sheet3")
database = MySQLdb.connect(host="localhost",user="root",password="s2019w36",db="ipc")

cursor = database.cursor()

query = """INSERT INTO mypc_table (hakbun,this_month,score,reason) VALUES (%s,%s,%s,%s)"""

for r in range(1,sheet.nrows) :
    hakbun = sheet.cell(r,0).value
    this_month = sheet.cell(r,1).value
    score = sheet.cell(r,2).value
    reason = sheet.cell(r, 3).value

    values = (hakbun,this_month,score,reason)

    cursor.execute(query,values)

cursor.close()
database.commit()
database.close()