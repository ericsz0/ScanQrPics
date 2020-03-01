# -*- coding:utf-8 -*-
# @Author:EricL
# https://www.cnblogs.com/xushengming/archive/2018/10/29/9872061.html
# pip install Pillow,pyzbar,
# pip install opencv-python
# 缺少 Python38\site-packages\pyzbar\libzbar-64.dll'，安装 vcredist_x64_2013

import pyzbar.pyzbar as pyzbar
from PIL import Image # ,ImageEnhance

image = "1.PNG"
img = Image.open(image)

#img = ImageEnhance.Brightness(img).enhance(2.0)#增加亮度
#img = ImageEnhance.Sharpness(img).enhance(17.0)#锐利化
#img = ImageEnhance.Contrast(img).enhance(4.0)#增加对比度
#img = img.convert('L')#灰度化
# img.show()

barcodes = pyzbar.decode(img)
for barcode in barcodes:
    barcodeData = barcode.data.decode("utf-8")
    print(barcodeData)