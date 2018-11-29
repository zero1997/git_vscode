# -*- coding: UTF-8 -*-

#将特征缩放至特定范围内， 将特征缩放到给定的最小值和最大值之间

from sklearn import preprocessing
import numpy as np   

#创建矩阵
X_train = np.array([[ 1., -1.,  2.],
                    [ 2.,  0.,  0.],
                    [ 0.,  1., -1.]])
#函数复制
min_max_scaler = preprocessing.MinMaxScaler()
#按特征的最小值和最大值将每列特征都放缩到【0， 1】之间，默认0， 1
X_train_minmax = min_max_scaler.fit_transform(X_train)
#训练集
X_test = np.array([[-3, -1, 4]])
X_test_minmax = min_max_scaler.transform(X_test)

