import pymysql as MySQLdb
import xlrd

tumbler = xlrd.open_workbook("data/mypc_student.xlsx")
sheet = tumbler.sheet_by_name("Sheet1")
database = MySQLdb.connect(host="localhost",user="root",password="123456",db="ipc")

cursor = database.cursor()

query = """INSERT INTO student_table (hakbun,check_mypc) VALUES (%s,%s)"""

for r in range(1,sheet.nrows) :
    hakbun = sheet.cell(r,0).value
    check_mypc = sheet.cell(r,1).value

    values = (hakbun,check_mypc)

    cursor.execute(query,values)

cursor.close()
database.commit()
database.close()