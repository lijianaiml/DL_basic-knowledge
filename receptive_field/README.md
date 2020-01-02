### CNN感受野及其计算
在CNN中感受野的概念非常重要，表征了CNN中每层的特征图（Feature Map）上的像素点在原始图像中映射的区域大小。感受野的概念完整来说其实包含两部分，感受野大小及其映射在原图的中心坐标。
一般计算感受野大小的方式分两种，第一种是从底向上算（Down-top），另一种是自顶向下的计算方法（Top-down）。详见calculate_receptive_field2.py.

计算感受野大小及其中心坐标详见calculate_receptive_field.py.

以下便以Darknet-53为例，计算scale1的每层感受野的大小及其中心坐标信息。

### usage
python calculate_receptive_field.py

python calculate_receptive_field2.py


### 参考
特征图尺寸和感受野计算详解
<br>https://zhuanlan.zhihu.com/p/56940729</br>

A guide to receptive field arithmetic for Convolutional Neural Networks
https://medium.com/mlreview/a-guide-to-receptive-field-arithmetic-for-convolutional-neural-networks-e0f514068807

如何计算感受野(Receptive Field)——原理
https://zhuanlan.zhihu.com/p/31004121
