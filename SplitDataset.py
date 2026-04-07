import pandas as pd
from sklearn.model_selection import train_test_split

# old data
old_df = pd.read_csv('./labels/gz2_edited3-1.csv', header=0)

train_df, test_df = train_test_split(old_df, test_size=0.05, random_state=42)

# Save the new data
train_df.to_csv('./labels/gz2_train.csv', index=False)
test_df.to_csv('./labels/gz2_test.csv', index=False)
