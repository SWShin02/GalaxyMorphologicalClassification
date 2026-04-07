import pandas as pd
"""Unify the labels Spiral(1) and Barred spiral(2) into Spiral(1)"""

df = pd.read_csv('./labels/gz2_edited2.csv', header=0)
for i in range(3):
    df.loc[df['label']==i+2, 'label'] = i+1

df.to_csv('./labels/gz2_edited2-1.csv', index=False)