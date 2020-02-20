from glob import glob
import os
import shutil

train_data_dir = "E:\graduate\data\garbage_classify\\train_data"
image_dir = "E:\graduate\data\garbage_classify\image"
txt_dir = "E:\graduate\data\garbage_classify\\txt"
label_files = glob(os.path.join(train_data_dir, '*.txt'))
image_name = glob(os.path.join(train_data_dir, '*.jpg'))
imgnum = 0
txtnum = 0
for image_path in image_name:
    shutil.copy(image_path, image_dir)
    imgnum = imgnum + 1
print(imgnum)
for txt_path in label_files:
    shutil.copy(txt_path, txt_dir)
    txtnum = txtnum + 1
print(txtnum)

if imgnum == txtnum:
    print('本次复制成功')
else:
    print('本次复制失败')
