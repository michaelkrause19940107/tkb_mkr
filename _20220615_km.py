import csv


# 読み込む CSV
with open('./train.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# ['11', '12', '13', '14']
# ['21', '22', '23', '24']
# ['31', '32', '33', '34']
