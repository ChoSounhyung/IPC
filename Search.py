import pandas as pd

csv_file = pd.read_csv('./data/real_ip.csv', index_col=False)

a = csv_file[csv_file['hakbun'] == 1401]
print(csv_file.loc[[1], ['pc', 'phone']])