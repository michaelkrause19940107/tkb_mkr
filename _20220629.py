import csv

# 読み込む CSV
with open('./train.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# ['11', '12', '13', '14']
# ['21', '22', '23', '24']
# ['31', '32', '33', '34']

import pandas as pd
from pathlib import Path
# ヘッダー行がある場合
filepath = 'train.csv'
print(Path(filepath).read_text())
#col0,col1,col2
#0.0,1.1,2.2
#3.3,4.4,5.5
#6.6,7.7,8.8

df = pd.read_csv(filepath)
print(df)
#   col0  col1  col2  # ヘッダー行から列名を推測してくれる
#0   0.0   1.1   2.2
#1   3.3   4.4   5.5
#2   6.6   7.7   8.8