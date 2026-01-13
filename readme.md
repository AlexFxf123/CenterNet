# CenterNet：目标检测
 
参考第十三章目标检测的配套代码。
 
## 1 环境准备
 
- 本程序需要安装[PyTorch](https://pytorch.org/)
- 还需要通过`pip install -r requirements.txt` 安装其它依赖
 
## 2 数据准备
 
本实验使用的内容图片数据集来自[COCO](http://cocodataset.org/#download)，点[此](http://images.cocodataset.org/zips/train2017.zip)下载训练集，点[此](http://images.cocodataset.org/zips/val2017.zip)下载验证集，点[此]下载对应的标注信息(http://images.cocodataset.org/annotations/annotations_trainval2017.zip)。
 
数据的组织形式如下：
```bash
    ├── data/ 			# 无代码，用来保存数据集
    │  ├──train2017/ 	# 训练数据集图像
    │  ├──val2017/ 		# 验证数据集图像
    │  └──annotations/ 	# 标注信息
```
 
## 用法
如果想要使用visdom可视化，请先运行`python -m visdom.server`启动visdom服务
 
- 训练
```bash
# 训练，使用GPU
train_set = true python ./main.py
```
 
- 测试
```bash
# 测试，使用GPU
train_set = false python ./main.py
```
 