import pymysql as MySQLdb
import xlrd

tumbler = xlrd.open_workbook("data/real_ip.xlsx")
sheet = tumbler.sheet_by_name("Sheet1")
database = MySQLdb.connect(host="localhost",user="root",password="123456",db="ipc")

cursor = database.cursor()

query = """INSERT INTO ip_table (hakbun,pc,phone) VALUES (%s,%s,%s)"""

for r in range(1,sheet.nrows) :
    hakbun = sheet.cell(r,0).value
    pc = sheet.cell(r,1).value
    phone = sheet.cell(r,2).value

    values = (hakbun,pc,phone)

    cursor.execute(query,values)

cursor.close()
database.commit()
database.close()