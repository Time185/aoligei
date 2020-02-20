import scipy.io as scio
label_array = scio.loadmat('E:\graduate\\resnext\ResNeXt-PyTorch\ImageNet\ILSVRC2012_devkit_t12\data\\meta.mat')['synsets']
print(len(label_array))
label_dic = {}
for i in  range(1000):
    label_dic[label_array[i][0][1][0]] = i
print(label_dic)
print(len(label_dic))