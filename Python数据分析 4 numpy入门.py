# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:24:32 2020

@author: Administrator
"""


import numpy as np


#转化产生数组——array
data1 = [6,7.5,8,0,1]
arr1 = np.array(data1)
print(arr1)

#数组的行数——ndim；形状——shape
data2 =	[[1,2,3,4],	[5,	6,7,8]]
arr2 =np.array(data2)
print(arr2.ndim,'\n',arr2.shape)

#数据类型——dtype；类型转换——astype
arr = np.array([1,2,3,4,5])
print(arr.dtype)
float_arr = arr.astype(np.float64)
print(float_arr.dtype)

#将相同规模数组进行大小比较，将产生一个布尔值数组
a1 = np.array([[1,2,3],[4,5,6]])
a2 = np.array([[0,4,1],[7,2,12]])
b = a1>a2
print(b)

#对切片赋值，同时也会赋给原数组
arr = np.array([1,2,3,4,5,6])
arr_slice = arr[2:4]
arr_slice[:] = 7
print(arr_slice)
print(arr)

#自动产生数组——arange；指定形状——reshape
#复制数组——copy()
arr3d = np.arange(12).reshape(2,2,3)
print(arr3d,'\n')
old_value = arr3d.copy()
arr3d[0] = 99
print(arr3d,'\n')
arr3d = old_value
print(arr3d)

#切片与索引
arr2d = np.arange(1,10).reshape(3,3) #创建一个3x3矩阵
a1 = arr2d[:,0] #生成一维数组
a2 = arr2d[:,:1] #生成二维数组
print(a1,'\n')
print(a2)

#神奇索引——使用整数列表索引
arr = np.empty((8,4))
for i in range(0,8):
    arr[i]=i
print(arr,'\n')
a = arr[[4,3,0,6]]
print(a,'\n')
#记得用2个中括号才是神奇索引。一个中括号的话是普通索引，传唤第几行几列
#所以写成下面这样的话会报错，因为矩阵才2个维度，维度数不够
try:
    b = arr[4,3,0,6]
except IndexError:
    print('维度数不够\n')
c = arr[4,3]
print(c)

#矩阵转置——.T；换轴——transpose和swapaxes
arr = np.arange(1,7).reshape(3,2)
b = arr.T
print(arr,'\n',b)
c = arr.transpose(0,1) #本来的顺序就是0,1，所以等于没换，c和arr相同
d = arr.transpose() #相当于transpose(1,0)
print(c,'\n')
print(d)
#注意1：3维及以上数组不适合用.T，因为说不清楚怎么转
#注意2：transpose要把新的轴顺序完整地输入进去；swapaxes只要输入需要对换的轴编号

#对数组进行算数运算——以np.sqrt()为例
arr = np.arange(1,7).reshape(3,2)
b = np.sqrt(arr)
print(b)


#np.where的使用
rand = np.random.randn(4,4)
print(rand)
#将正值换成'+'，负值换成'-'
a = np.where(rand>0,'+','-')
print(a)


#平均值——mean
arr = np.arange(1,21).reshape(5,4)
print(arr,'\n')
print(arr.mean(),'\n') #所有数字的平均值
print(arr.mean(0),'\n') #各列的平均值
print(arr.mean(1)) #各行的平均值
#累加——cumsum
print(arr.cumsum(),'\n') #遍历所有数字累加
print(arr.cumsum(0),'\n') #在列方向上累加
print(arr.cumsum(1)) #在行方向上累加

#排序——sort
a = np.array([[2,3,1],[6,4,5]])
a.sort() #默认为sort(1)
print(a,'\n')
a = np.array([[2,3,1],[6,4,5]])
a.sort(0) #列方向排序
print(a,'\n')
a = np.array([[2,3,1],[6,4,5]])
a.sort(1) #行方向排序
print(a)

#两种乘法
arr1 = np.array([[1,2,3],[4,5,6]])
b = arr1* arr1 #对应元素相乘
print(b,'\n')
c = np.dot(arr1.T,arr1) #真正的矩阵点乘
print(c)
