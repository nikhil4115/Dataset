import os
import shutil

path = "../train"

os.chdir(path)

txt=[]
photos=[]

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())

for file in os.listdir():

    if file.endswith(".txt"):

        file_path = f"{path}/{file}"
        txt.append(file_path)

    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):

        file_path = f"{path}/{file}"
        photos.append(file_path)


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
for i in txt:
    s=i[:-4:1]+".jpg"
    s1 = i[:-4:1] + ".jpeg"

    if s in photos or s1 in photos:

        txt1=[]
        txt0=[]
        file1=open("{}".format(i),"r")
        k=file1.readlines()

        for j in k:

            if j[0]=="0":
                txt0.append(j)

            elif j[0]=="1":
                txt1.append(j)

        txt0 = "".join(txt0)

        if len(txt0) > 1:
            p=i[8::]
            file2=open("{}".format("../dataset_for_mask/no_mask"+p),"w")
            file2.write(txt0)
            file2.close()

            if s in photos:
                shutil.copy(s,"../dataset_for_mask/no_mask"+p[:-4:1]+".jpg")

            if s1 in photos:
                shutil.copy(s1,"../dataset_for_mask/no_mask"+p[:-4:1]+".jpeg")


            for t in range(len(txt1)):
                txt1[t]="0"+txt1[t][1::]

            txt1 = "".join(txt1)

            if len(txt1) > 1:
                p = i[8::]
                file2 = open("{}".format("../dataset_for_mask/mask" + p), "w")
                file2.write(txt1)
                file2.close()

                if s in photos:
                    shutil.copy(s, "../dataset_for_mask/mask" + p[
                                                                   :-4:1] + ".jpg")

                if s1 in photos:
                    shutil.copy(s1, "../dataset_for_mask/mask" + p[
                                                                    :-4:1] + ".jpeg")

        file1.close()