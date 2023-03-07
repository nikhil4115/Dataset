import pandas as pd
import os
from datbase3 import convert
import shutil

dataset_folder_path=r"D:\dataset2\planes detection\archive\Airplanes_Annotations\Airplanes_Annotations"
image_folder_path=r"D:\dataset2\planes detection\archive\Images\Images"
txt_folder_path=r"D:\dataset2\planes detection\archive\txt"

for (root,dirs,files) in os.walk(dataset_folder_path, topdown=True):
    for file in files:
        if file.endswith('.csv') and os.path.exists(f"{image_folder_path}\{file[:-4:]}.jpg"):
            all_annotation = []
            csvfile=pd.read_csv(f"{dataset_folder_path}\{file}")
            for collem in csvfile:
                for row in csvfile[collem]:
                    annotation=row.split(" ")
                    all_annotation.append(convert(int(annotation[0]),
                                           int(annotation[1]),
                            int(annotation[2]),int(annotation[3]),
                            f"{image_folder_path}\{file[:-4:]}.jpg"))
            if len(all_annotation)>1:
                file1=open(f"{txt_folder_path}\{file[:-4:]}.txt","w")
                file1.write("".join(all_annotation))
                file1.close()
                shutil.copy(f"{image_folder_path}\{file[:-4:]}.jpg", txt_folder_path)
                print(f"{txt_folder_path}\{file[:-4:]}.txt")