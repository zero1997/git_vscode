# -*-  coding: UTF-8 -*-

#加载标准数据集, iris和digits
from sklearn import datasets
from sklearn import svm
iris = datasets.load_iris()
digits = datasets.load_digits()
#在这个例子中，我们手动设置 gamma 值。不过，通过使用 网格搜索 及 交叉验证 等工具，可以自动找到参数的良好值。
clf = svm.SVC(gamma = 0.001, C = 100)
#作为一个训练集，让我们使用数据集中除最后一张以外的所有图像。 我们用 [:-1] Python 语法选择这个训练集
#从后往前数的话，最后一个位置为-1, 因此下面是从位置0到位置-1之前的数
clf.fit(digits.data[:-1], digits.target[:-1]) 
#向分类器询问 digits 数据集中最后一个图像（没有用来训练的一条实例）的数字是什么
print(clf.predict(digits.data[-1:]))


