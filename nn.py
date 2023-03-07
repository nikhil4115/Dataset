import os
import shutil
import re

def separate_images(yolo_path, images_path, output_path):
    with open(yolo_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        # print(line[0])
        # print(yolo_path)
        lable = line.split(" ")
        print(f'{output_path}/{lable[0]}')
        os.makedirs(f'{output_path}/{lable[0]}', exist_ok=True)
        # print(os.path.exists(os.path.split(images_path)[1]),">>>>>>>>>>>>")
        # print(os.path.split(images_path)[1])
        # if os.path.exists(os.path.split(images_path)[1]):
        with open (f"{output_path}/{lable[0]}/{yolo_path.split('/')[-1].split('.')[0]}.txt", 'a') as file:
            file.write(line)
        # print(f"{output_path}/{line[0]}/{yolo_path.split('/')[-1].split('.')[0]}.txt")
            # print(f"{output_path}/{line[0]}/{yolo_path.split('/')[-1].split('.')[0]}.jpg")
        existing_image_path=f"{output_path}/{lable[0]}/{yolo_path.split('/')[-1].split('.')[0]}"
        # print(existing_image_path,">>>>>>>>>>>")
        if not os.path.exists(f"{existing_image_path}.jpg") or \
                os.path.exists(f"{existing_image_path}.jpeg") or \
                os.path.exists(f"{existing_image_path}.png"):
            shutil.copy(images_path, f"{output_path}/{lable[0]}/")


output_path =r"D:\gopal"
    # r"D:\dataset2\aerial satellite\archive (1)\train"
# os.makedirs(output_path, exist_ok=True)
images_path_1 = r"D:\gopal\test"
yolo_txt_path_1 = r"D:\gopal\test"
img=""
for txt in os.listdir(yolo_txt_path_1):
    if txt.endswith(".txt"):
        yolo_txt_path = f"{yolo_txt_path_1}/{txt}"
        if os.path.exists(f"{images_path_1}/{os.path.split(yolo_txt_path)[1][:-4:]}.jpg"):
            images_path = f"{images_path_1}/{os.path.split(yolo_txt_path)[1][:-4:]}.jpg"
            # print(f"{images_path_1}/{os.path.split(yolo_txt_path)[1][:-4:]}.jpg")
            separate_images(yolo_txt_path, images_path, output_path)

        if os.path.exists(f"{images_path_1}/{os.path.split(yolo_txt_path)[1][:-4:]}.jpeg"):
            images_path = f"{images_path_1}/{os.path.split(yolo_txt_path)[1][:-4:]}.jpeg"
            # print(f"{images_path_1}/{os.path.split(yolo_txt_path)[1][:-4:]}.jpg")
            separate_images(yolo_txt_path, images_path, output_path)

        if os.path.exists(f"{images_path_1}/{os.path.split(yolo_txt_path)[1][:-4:]}.png"):
            images_path = f"{images_path_1}/{os.path.split(yolo_txt_path)[1][:-4:]}.png"
            separate_images(yolo_txt_path, images_path, output_path)