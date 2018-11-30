# -*- coding: UTF-8 -*-

#设定一些系数为零，是估计稀疏系数的线性模型

from sklearn import linear_model
reg = linear_model.Lasso(alpha = 0.1)
reg.fit([[0, 0], [1, 1]], [0, 1])

print reg.predict([[1, 1]])
