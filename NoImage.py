import os
import pandas as pd

def get_jpg_filenames(directory):
    return [f for f in os.listdir(directory) if f.lower().endswith(".jpg")]

def get_jpg_filenames_without_extension(filenames, directory=None):
    if filenames is None:
        return [os.path.splitext(f)[0] for f in os.listdir(directory) if f.lower().endswith(".jpg")]
    else:
        return [os.path.splitext(f)[0] for f in filenames if f.lower().endswith(".jpg")]

# 사용 예시
directory = "images"  # 실제 경로 입력
jpg_files = get_jpg_filenames(directory)
jpg_files_without_extension = get_jpg_filenames_without_extension(jpg_files)

n_data = len(jpg_files)

new_df = pd.DataFrame(
    {
        "image_name": jpg_files,
        "label": ''
    }
)

old_df = pd.read_csv(
    "./labels/gz2_edited1.csv", header=0,
    dtype={"asset_id":str, "class_id":str})

one_percent = n_data // 100

print(old_df)

##############################################
print("Dataset is ready")
for i in range(n_data):
    label = old_df.loc[old_df['asset_id'] == jpg_files_without_extension[i], 'class_id']
    if not label.empty:
        new_df.loc[i, 'label'] = label.values[0]
        # print(f"{jpg_files[i]} is added")
    else:
        if new_df.loc[i, 'image_name'] == jpg_files[i]:
            new_df.drop(i, inplace=True)
            print(f"{jpg_files[i]} is removed")
        else:
            print(f"Error: {jpg_files[i]} is not found")
            exit()
    
    if i % one_percent == 0:
        print(f"Progress: {i // one_percent}%")

# Save the new dataset
new_df.to_csv("./labels/gz2_edited2.csv", index=False)