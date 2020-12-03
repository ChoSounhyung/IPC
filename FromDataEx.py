import pymysql as MySQLdb
import xlrd

from DB.db_connect import DbConnect

tumbler = xlrd.open_workbook("data/real_ip.xlsx")
sheet = tumbler.sheet_by_name("Sheet1")

db_connect = DbConnect()
query = """INSERT INTO ip_table (hakbun,pc,phone) VALUES (%s,%s,%s)"""

for r in range(1,sheet.nrows) :
    hakbun = sheet.cell(r,0).value
    pc = sheet.cell(r,1).value
    phone = sheet.cell(r,2).value

    values = (hakbun,pc,phone)

    db_connect.cursor.execute(query,values)

db_connect.cursor.close()
db_connect.mydb.commit()
db_connect.mydb.close()