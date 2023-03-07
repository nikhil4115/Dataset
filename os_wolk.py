import os
from datbase3 import convert

for (root,dirs,files) in os.walk(r"D:\dataset2\WiderPerson\WiderPerson\test", topdown=True):
    for i in files:
        if i.endswith(".txt") and i!="classes.txt":
            file=open(f"{root}\{i}","r+")
            rfile=file.readlines()
            for j in range(len(rfile)):
                rfile[j]=rfile[j].split(" ")
                if len(rfile[j]) > 1:
                    rfile[j][0]="0"
                    rfile[j]=convert(int(rfile[j][1]),int(rfile[j][3]),int(rfile[j][2]),int(rfile[j][4][:-2:]),f"{root}\{i[:-4:]}.jpg")
                    rfile[j]="".join(rfile[j])
                    rfile[j]=rfile[j]
                else:
                    rfile[j]=""
            rfile="".join(rfile)
            file.seek(0,0)
            file.write(rfile)
            file.close()