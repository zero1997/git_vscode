# -*- coding: UTF-8 -*-

from sklearn import linear_model
#设置多组alpha值，选择其中最合适的
#将训练集分出一部分作为验证集
reg = linear_model.RidgeCV(alphas=[1.8, 1.0, 10.0])
reg.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1]) 
print reg.alpha_
