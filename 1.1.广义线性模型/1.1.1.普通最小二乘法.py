# -*- coding: UTF-8 -*-

#使数据集实际观测数据和预测数据之间的残差平方和最小

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit ([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

print reg.coef_