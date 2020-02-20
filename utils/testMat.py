from glob import glob
import  os
import shutil
# 将训练集的txt文件和验证集的txt文件放到相应的目录下
def copyTxt(image_dir, txt_dir):
    list = os.listdir(image_dir)
    txt_list = []
    for image_name in list:
        txt_list.append(image_name.replace('.jpg', '.txt'))
    for txt_name in txt_list:
        shutil.copy(os.path.join(txt_dir, txt_name), image_dir)
    print("奥利给！！！")

# 生成 图片名：类别的 字典
def generateLabelDic (image_dir):
    txt_name_list = glob(os.path.join(image_dir, '*.txt'))
    print(f"txt 文件数为: {len(txt_name_list)} 个")
    dic = {}
    for txt_name in txt_name_list:
        with open(txt_name, 'r') as f:
            str = f.readline()
            dic[os.path.join(image_dir, str.split(",")[0])] = str.split(", ")[1]
            f.close()
    return dic

# 根据路径生成图片路径数组和标签数组，并一一对应
def generateImagePathAndTxtArray(image_dir):
    txt_name_list = glob(os.path.join(image_dir, '*.txt'))
    img_path = []
    img_label = []
    for txt_name in txt_name_list:
        with open(txt_name, 'r') as f:
            str = f.readline()
            img_path.append(os.path.join(image_dir, str.split(",")[0]))
            img_label.append(str.split(",")[1])
            f.close()
    print(len(img_path))
    print(img_path[0])
    return img_path, img_label


#copyTxt(image_dir= 'E:\graduate\data\garbage_classify\\train_image', txt_dir= 'E:\graduate\data\garbage_classify\\txt')
#copyTxt(image_dir= 'E:\graduate\data\garbage_classify\\val_image', txt_dir= 'E:\graduate\data\garbage_classify\\txt')
#generateImagePathAndTxtArray(image_dir="E:\graduate\\resnext\ResNeXt-PyTorch\ImageNet\\val_image")