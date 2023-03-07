import os
import shutil

# C:\Users\DELL\Downloads\archive\dataset\images\train\classes.txt
# C:\Users\DELL\Downloads\archive\dataset\images\train\
# D:\dataset2\example\

classes_path=r"D:\dataset2\aerial satellite\archive (1)\validate\anotaciones_validate\classes.txt"
dataset_path=r"D:\dataset2\aerial satellite\archive (1)\validate\imagenes_val"
after_path=r"D:\dataset2\aerial satellite\archive (1)\train"


def read_text_file(file_path):
    with open(file_path, 'r') as f:
        classes=f.read()
        classes=classes.split("\n")
        return classes

def sepret_classes(dataset_path,folder_path,classes_index):
    path = dataset_path
    os.chdir(path)
    txt=[]
    photos=[]
    for file in os.listdir():

        if file.endswith(".txt"):
            file_path = f"{path}/{file}"
            txt.append(file_path)

        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(
                ".png"):
            file_path = f"{path}/{file}"
            photos.append(file_path)

    for i in txt:
        s = i[:-4:1] + ".jpg"
        s1 = i[:-4:1] + ".jpeg"

        if s in photos or s1 in photos:

            txt0 = []
            file1 = open("{}".format(i), "r")
            k = file1.readlines()

            for l in k:
                l=l.split()
                if l[0] == "{}".format(classes_index):
                    # l=" ".join(l)
                    txt0.append(l)
            for t in range(len(txt0)):
                txt0[t][0]="0"
                txt0[t]=" ".join(txt0[t])
            print(txt0)
            txt0 = "".join(txt0)
            print(">>>>>>>>>>>>>>")
            i=i.split("/")
            if folder_path.find(" "):
                print(folder_path)
            folder_path1=os.path.join(folder_path, i[-1])
            if len(txt0)>1:
                file2 = open("{}".format(folder_path1),
                             "w")
                file2.write(txt0)
                file2.close()

                if s in photos:
                    shutil.copy(s,folder_path1[:-4:]+ ".jpg")

                if s1 in photos:
                    shutil.copy(s1, folder_path1[:-4:] + ".jpeg")
            file1.close()

classes=read_text_file(classes_path)
j=0
print(classes)
for i in classes:
    after_path2 = os.path.join(after_path, i)
    os.makedirs(after_path2,exist_ok=True)
    sepret_classes(dataset_path,after_path2,j)
    j += 1