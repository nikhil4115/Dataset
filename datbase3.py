from PIL import Image
import os
#
def convert(xmin, ymin, xmax, ymax,filepath):
    img = Image.open(filepath)
    dw = 1. / (img.width)
    dh = 1. / (img.height)
    x = (xmin + xmax) / 2.0 - 1
    y = (ymin + ymax) / 2.0 - 1
    w = xmax - xmin
    h = ymax - ymin
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return f"{0} {x} {y} {w} {h}\n"

# print(convert(15,69,40,96,r"D:\dataset2\planes detection\archive\test\42845.jpg"))
# filepath = r"D:\dataset2\guns\archive\nn\3.jpeg"
# img = Image.open(filepath)
#
# print(189,34,282,94)
# print(convert(189,34,282,94,img.width,img.height))

# clsses_txt= r"D:\train\classes.txt"
# with open(clsses_txt, 'r') as f:
#     classes = f.read()
# classes=classes.split(" ")
# print(classes)