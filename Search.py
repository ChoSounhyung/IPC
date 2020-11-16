import pandas as pd

csv_file = pd.read_csv('./data/real_ip.csv', index_col=False)


classof = input('학번을 입력하세요(ex.1101) : ')
index = int(classof[2:])-1
class_num = int(classof[1])

if class_num <= 6 and int(classof[2:]) <= 20:
    if class_num == 1:
        index += 0
    elif class_num == 2:
        index += 20
    elif class_num == 3:
        index += 40
    elif class_num == 4:
        index += 60
    elif class_num == 5:
        index += 80
    elif class_num == 6:
        index += 100
else :
    print('학번이 잘못되었습니다.')

row_num = csv_file.loc[[index], ['pc', 'phone']]
print(row_num)
