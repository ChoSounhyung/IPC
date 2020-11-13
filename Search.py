import openpyxl
of = openpyxl.load_workbook('./data/ip_dummy.xlsx')
sheet = of.active

col_range = sheet['B:C']

a = int(input("번호 입력 : "))
print('pc\t\t\t\tphone')
for i in col_range:
    print(f'10.96.122.' + str(i[a-1].value) , end='\t')
