import numpy as np    #练习使用numpy库
import time

from numpy.random.mtrand import random

def compare(self):
    t1 = time.time()
    a = []
    for x in range(10):   #[0,10) = [0,9]
        a.append(x**2)    #在末尾添加元素
    t2 = time.time()
    print(t2-t1)

    t3 = time.time()
    b = np.arange(10)**2  # np.arange和range类似用法
    t4 = time.time()
    print(t4-t3)          # 可以看出 使用numpy库，比纯python代码快很多'''

#数组
def arry():
    A1 = np.array([0,1,2,3,4,5,6,7,8,9,10],dtype='f2')     
    '''
    array数组,规定类型为i1:int8，可以是i2,i4,i8. 
    b:bool 
    u1,u2,u4,u8:无符号整数
    f2,f4,f8:float类型
    O:python对象
    S:string
    U:unicode类型
    VA1 = A1.astype('U') 
    用astype函数改变A1的数据格式
    VA1 = A1[1:9:2]  #从A1[1]到A1[9],步长是2
    切片，用冒号进行,多维数组同样操作
    索引：
    a[[2,3]]二维数组第3、4行的两行元素
    a[2,3]二维数组第3行第4列的一个元素
    a[[1,2],[4,5]]二维数组第2行第5列、第3行第6列的两个元素
    a[1:3,4:6]二维数组第2到第4行(不包括4)、第5到第7(不包括7)的所有元素  （4个元素）
    a[:,1]二维数组第2列全部元素 a[:,1:4]第2到第4列 a[:,[1,4]]第2列和第5列
    bool索引：
    直接 a<10 即可 eg：a=np.arange(24).reshape(4,6) print(a<5|a>10)
    '''
    #np.array创建数组
    A2 = np.arange(10)           #arange数组，取[0,9]
    VA2 = A2.reshape(2,5)
    print((VA2<3)|(VA2>7))       #bool索引
    A3 = np.arange(0,10,2)       #arange数组，每隔2个取[0,9]
    #np.arange创建数组
    A4 = np.random.random(2)     #随机取 0到1的数字两个组成数组
    A5 = np.random.random((2,2)) #随机取 0到1的数字，组成2行2列的数组，多维数组
    A6 = np.random.randint(0,10,size=(2,3)) #随机取0到10的整型数字，组成2行3列的多维数组
    #np.random创建数组
    A7 = np.zeros((2,2))         #都是0的2行2列多维数组
    A8 = np.ones((2,2))          #都是1的2行2列多维数组
    A9 = np.eye(2)               #2维单位矩阵
    A10 = np.full((2,3),9)       #full都是9的 2行3列
    #特殊函数创建数组
    '''print(A1,A2,A3,A4,'\n',A5,'\n',A6,'\n',A7,'\n',A8,'\n',A9,'\n',A10)
    print(A1.dtype) #
    dtype获取数据类型
    ndim获取维度
    shape获取形状（几行几列）
    size获取元素个数
    itemsize获取数组中，单个元素所占字节大小
    reshape函数可以改变np数组的形状，保持数字数量不变 eg：A1.reshape((2,2))  
    flatten函数可以直接吧np数组变为一维数组'''
    

arry()