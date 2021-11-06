import pandas as pd
import numpy as np

def kill_index():
    s = np.arange(1,6)
    s1 = pd.Series(s) #输出数值及对应索引
    s2 = pd.Series(s,index=['a','b','c','d','e'])  #指定索引
    print(s2.index)  #查看索引
    print(s2.values) #查看值
    #用字典创建
    dict = {'name':'Jack','age':18,'sex':'male'}
    s3 = pd.Series(dict)
    print(s3)
kill_index()