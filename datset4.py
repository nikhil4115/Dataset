from datbase3 import convert
import os
path=r"D:\dataset2\guns\archive\repository\SasankYadati-Guns-Dataset-0eb7329\Labels"
os.chdir(path)
for i in os.listdir():
    file=open(f"{path}/{i}","r+")
    lines=file.readlines()
    after_line=""
    for j in range(len(lines)):
        lines[j]=lines[j].replace("\n","")
        lines[j]=lines[j].split(" ")
        if len(lines[j])>1:
            image_path=os.path.join(f"{path[:-6:]}Images",f"{i[:-4:]}.jpeg")
            n=convert(int(lines[j][0]),int(lines[j][1]),int(lines[j][2]),int(lines[j][3]),
                      image_path)
            after_line=after_line+n
    print(after_line)
    print(i)
    file.seek(0)
    file.write(after_line)
    file.close()
    print("\n\n\n")