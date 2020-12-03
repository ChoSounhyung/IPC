import xlrd

from DB.db_connect import DbConnect

tumbler = xlrd.open_workbook("data/mypc_dummy.xlsx")
sheet = tumbler.sheet_by_name("Sheet1")

db_connect = DbConnect()

query = """INSERT INTO mypc_table (hakbun,this_month,score,reason) VALUES (%s,%s,%s,%s)"""

for r in range(1,sheet.nrows) :
    hakbun = sheet.cell(r,0).value
    this_month = sheet.cell(r,1).value
    score = sheet.cell(r,2).value
    reason = sheet.cell(r, 3).value

    values = (hakbun,this_month,score,reason)

    db_connect.cursor.execute(query,values)

db_connect.cursor.close()
db_connect.mydb.commit()
db_connect.mydb.close()