# -*- coding: UTF-8 -*-

#标准化，去均值和方差按比例缩放
from sklearn import preprocessing
import numpy as np


X_train = np.array([[1, -1, 2],
                    [2, 0, 0],
                    [0, 1, -1]])
X_scaled = preprocessing.scale(X_train);


print X_scaled;
#每一列的均值，axis=0代表列
X_scaled.mean(axis = 0);
#每一列的方差，axis=1
X_scaled.std(axis = 0);


scaler = preprocessing.StandardScaler().fit(X_train)
print scaler;
#训练集每一列的平均值
print scaler.mean_;
#训练集每一列的标准差
print scaler.scale_;
#将训练集应用变换
scaler.transform(X_train);
print(X_train)
#对测试集运用相同的变换
X_test = [[-1, 1, 0]];
print(scaler.transform(X_test));

'''
from sklearn import preprocessing
import numpy as np
X_train = np.array([[ 1., -1.,  2.],
                    [ 2.,  0.,  0.],
                    [ 0.,  1., -1.]])
X_scaled = preprocessing.scale(X_train)

X_scaled  

X_scaled.mean(axis=0)


X_scaled.std(axis=0)
scaler = preprocessing.StandardScaler().fit(X_train)
scaler


scaler.mean_                                      


scaler.scale_                                       


scaler.transform(X_train)     

X_test = [[-1., 1., 0.]]
print(scaler.transform(X_test))    

'''


