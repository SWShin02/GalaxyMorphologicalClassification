import pandas as pd

df = pd.read_csv('./labels/gz2_edited3.csv', header=0)
print(df['label'].value_counts())