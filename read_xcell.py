import pandas as pd
import os
from datbase3 import convert
import shutil


dir_path=r"D:\dataset2\car detection\Archive (1)\data"
file_name=r"train_solution_bounding_boxes (1).csv"
images_path=r"D:\dataset2\car detection\Archive (1)\data\training_images"
output_path=r"D:\dataset2\car detection\Archive (1)\data\testing_images"

s=pd.read_csv(f"{dir_path}\{file_name}")
all=[]
for i in s:
    collem=[]
    for j in s[i]:
        collem.append(j)
    all.append(collem)
# print(all)
all1=[]
for i in range(len(all[0])):
    collem = [all[0][i],all[1][i],all[2][i],all[3][i],all[4][i]]
    all1.append(collem)

images=[]
for i in os.listdir(images_path):
    images.append(i)

for i in all1:
    if i[0] in images:
        print(i[0].split(".")[0])

        if os.path.exists("{}\{}.txt".format(output_path,i[0].split(".")[0])) :
            file = open("{}\{}.txt".format(output_path, i[0].split(".")[0]), "r+")
            line=file.readlines()
            line="".join(line)
            file.write(line+convert(i[1], i[2], i[3], i[4], f"{images_path}\{i[0]}"))
            print(convert(i[1],i[2],i[3],i[4],f"{images_path}\{i[0]}"),i[0])
        else:
            file=open("{}\{}.txt".format(output_path,i[0].split(".")[0]),"w")
            file.write(convert(i[1], i[2], i[3], i[4], f"{images_path}\{i[0]}"))
            file.close()
            shutil.copy(f"{images_path}\{i[0]}",output_path)
            print(convert(i[1], i[2], i[3], i[4], f"{images_path}\{i[0]}"),
                  i[0],"not exxist")