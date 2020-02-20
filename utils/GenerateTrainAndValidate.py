# 用来生成训练集、验证集和测试集
from glob import glob
import os
import shutil
import random

image = "E:\graduate\data\garbage_classify\\image"
train_image = "E:\graduate\data\garbage_classify\\train_image"
val_image = "E:\graduate\data\garbage_classify\\val_image"

image_name = glob(os.path.join(image, '*.jpg'))
random.shuffle(image_name)
train_num = len(image_name) * ( 6 / 7)
train = 0
val = 0
print(int(train_num))
for image_path in image_name:
    if train <= int(train_num):
        shutil.copy(image_path, train_image)
        train = train + 1
    else:
        shutil.copy(image_path, val_image)
        val = val + 1
if (val + train) == len(image_name):
    print("success !!! ")
    print(f"训练集 {train} 张图片， 测试集 {val} 张图片")
else:
    print("error !!!")

