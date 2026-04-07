import pandas as pd

# CSV 파일 로드 (예: 'data.csv')
df = pd.read_csv('./labels/gz2_edited2-1.csv')

# 'label' 컬럼이 존재하는지 확인
if 'label' not in df.columns:
    raise ValueError("The CSV has no 'label' column.")

# 각 label별 20,000개 샘플링
sampled_df = df.groupby('label', group_keys=False).apply(lambda x: x.sample(n=min(20000, len(x)), random_state=42))

# 새로운 CSV 파일로 저장 (예: 'sampled_data.csv')
sampled_df.to_csv('./labels/gz2_edited3-1.csv', index=False)

print("Sampling completed! The file is saved as 'gz2_edited3-1.csv'.")
