# import requests
# import shutil
# import os
#
#
# path = "D:\dataset2\openimage"
#
# os.chdir(path)
#
#
#
# def read_text_file(file_path):
#     with open(file_path, 'r') as f:
#         classes=f.read()
#         classes=classes.split("\n")
#     for i in range(1,len(classes)):
#         k=classes[i].find("jpg")
#         classes[i]=classes[i][:k+3:]
#
#         file_name =url+str(i)+".jpg"
#
#         res = requests.get(classes[i], stream = True)
#
#         if res.status_code == 200:
#             shutil.copyfileobj(res.raw, open(file_name,'wb'))
#             print('Image sucessfully Downloaded: ',file_name)
#         else:
#             print('Image Couldn\'t be retrieved')
#
# url=""
# for file in os.listdir():
#     file_path = f"{path}/{file}"
#     print(file_path)
#     url = file[:-4:]
#     os.mkdir(url)
#     url=os.path.join(path,f"{url}/")
#     print(url)
#     print()
#     read_text_file(file_path)



# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
#
# gauth = GoogleAuth()
# drive = GoogleDrive(gauth)
#
# # upload_file_list = ['1.jpg', '2.jpg']
# # for upload_file in upload_file_list:
# gfile = drive.CreateFile({'parents': [{'id': '152yJRWavdVpC9SZl_G6iK18TY05WgZA1'}]})
# # Read file and set it as the content of this instance.
# gfile.SetContentFile("909.jpg")
# gfile.Upload() # Upload the file.

import pandas as pd

df = pd.read_excel('train_solution_bounding_boxes (1).csv')
print(df)


