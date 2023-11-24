import shutil
import os
import pandas as pd

df = pd.read_csv("Train.csv")
df.head()
clean = df[df["Quality"] != 3]

print(df["Quality"].value_counts())

field_names = clean["Field_ID"].to_list()

FOLDER = "cleaned_train_images"
OLD_FOLDER = "image_arrays_train"
clean.to_csv("cleaned.csv")

"""
for field_name in field_names:
	source_path = os.path.join(OLD_FOLDER, f"{field_name}.npy")
	dest_path = os.path.join(FOLDER, f"{field_name}.npy")
	shutil.move(source_path, dest_path)

print("complete")
"""




