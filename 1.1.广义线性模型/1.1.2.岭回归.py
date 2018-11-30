# -*- coding: UTF-8 -*-

#Ridge回归通过对系数的大小施加惩罚来解决 普通最小二乘法 的一些问题。 岭系数最小化的是带罚项的残差平方和.

from sklearn import linear_model
reg = linear_model.Ridge(alpha= 0.5)
reg.fit ([[0, 0], [0, 0], [1, 1]], [0, .1, 1]) 
#是否需要计算截距
#Ridge(alpha=0.5, copy_X=True, fit_intercept=True, max_iter=None,normalize=False, random_state=None, solver='auto', tol=0.001)
print reg.coef_
print reg.intercept_