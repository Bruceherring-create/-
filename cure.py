# -*- coding: utf-8 -*-
# @File  : cure.py
# @Author: JavaMan
# @Date  : 2018/07/04
# @Desc  : 拟合艾宾浩斯曲线
#@license : Copyright(C), JavaMan
#@Contact : 2360838724@qq.com
#@Software : PyCharm

# _*_coding:utf-8_*_
__author__ = 'LXF'
# Python imports
#使用非线性最小二乘法拟合
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import math

#用指数形式来拟合
# x = np.arange(1, 17, 1)
x =  np.array([0.33, 1,8.8,24,48,248,744])
y = np.array([58.2,44.2,35.8,33.7,27.8,25.4,21.1])
def func(x,a,b,c,d):
    # return a*(x**(-b))
    # return  b/((math.log(x))**a+b)
    return a*np.exp(b*x/24.0)+c*np.exp(d*x/24.0)
popt, pcov = curve_fit(func, x, y)
a=popt[0]#popt里面是拟合系数，读者可以自己help其用法
b=popt[1]
c=popt[2]
d=popt[3]
yvals=func(x,a,b,c,d)
print('a=',a)
print('b=',b)
print('c=',c)
print('d=',d)
# yvals=func(x,a,b)
plot1=plt.plot(x, y, '*',label='original values')
plot2=plt.plot(x, yvals, 'r',label='fitting values')
plt.xlabel('x hour')
plt.ylabel('y %')
plt.legend(loc=4)#指定legend的位置,读者可以自己help它的用法
plt.title('Ebbinghaus fitting curve')
plt.show()