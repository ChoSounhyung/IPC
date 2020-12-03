import xlrd

from DB.db_connect import DbConnect

tumbler = xlrd.open_workbook("data/mypc_student.xlsx")
sheet = tumbler.sheet_by_name("Sheet1")

db_connect = DbConnect()

query = """INSERT INTO student_table (hakbun,check_mypc) VALUES (%s,%s)"""

for r in range(1,sheet.nrows) :
    hakbun = sheet.cell(r,0).value
    check_mypc = sheet.cell(r,1).value

    values = (hakbun,check_mypc)

    db_connect.cursor.execute(query,values)

db_connect.cursor.close()
db_connect.mydb.commit()
db_connect.mydb.close()