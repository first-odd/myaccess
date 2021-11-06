from numpy.core.fromnumeric import size, var
from numpy.random.mtrand import randint
import pandas as pd
import numpy as np
from pandas.core import series

def kill_series():
    s = np.arange(1,6)
    s1 = pd.Series(s) #输出数值及对应索引
    s2 = pd.Series(s,index=['a','b','c','d','e'])  #指定索引
    print(s2.index)  #查看索引
    print(s2.values) #查看值
    #用字典创建
    dict = {'name':'Jack','age':18,'sex':'male'}
    s3 = pd.Series(dict)
    print(s3)
    print('='*50)
    print(s3['name':'sex']) #包含‘sex’
    print('='*50)
    print(s3[1:2])  #不包含2

    #name属性
    s = np.random.randint(1,5,size=(6,))
    s = pd.Series(s,index=['a','b','c','d','e','f'])
    s.name = 'temp' #对象名
    s.index.name = 'year' #对象索引名
    print(s.head())  #s.head() 默认输出前5行   s.tail()默认输出后5行

def kill_dataframe():
    data = {'a':[1,2,3],'b':(4,5,6),'c':np.arange(7,10)} #列表、元组、数组 构成的字典
    print(data)
    frame = pd.DataFrame(data) # 转换成daraframe
    print(frame)  
    print('='*50)
    print(frame.values) 
    print(frame.index) #查看行索引
    print(frame.columns) #查看列索引
    print('='*50)
    change_index = pd.DataFrame(data,index=['A','B','C'],columns=['a','b','c','e']) #keys当作了列索引，不能更改，只能添加
    print(change_index)

    # series构成的字典，转换成dataframe
    data1 = pd.DataFrame({'a':pd.Series(np.arange(5)),
                          'b':pd.Series(np.arange(5,10))})
    print(data1)

    #嵌套字典，转换成dataframe
    data2 = {'a':{'apple':3.5,'banana':3.8},
            'b':{'apple':3,'banana':5},
            'c':{'apple':2}}
    change_data2 = pd.DataFrame(data2)
    print(change_data2)

    # 二维数组 转换成dataframe
    double_list = np.arange(15).reshape(3,5)
    vary = pd.DataFrame(double_list)
    print(vary)

    #字典构成的列表，转换成dataframe
    dict_list = [{'apple':3.5,'banana':3.8},
                {'apple':3,'banana':5},
                {'apple':2}]
    vary = pd.DataFrame(dict_list)
    print(vary)

    #series构成的列表，转换成dataframe3
    series_list = [pd.Series(np.random.rand(3)),pd.Series(np.random.rand(2))]
    print(series_list)
    print('='*50)
    vary = pd.DataFrame(series_list)
    print(vary)

    set_frame = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','c','b'],columns=['A','B','C'])
    set_frame['D'] = [1,2,3] #增加D列
    print(set_frame.T) #转置
    print('='*50)
    print(set_frame['A']) #索引A列 

    '''
    index索引不可更改，需要创建新索引：reindex来新增或者改变顺序
    '''
    f = np.arange(5)
    data_f = pd.DataFrame(f,index=['%s'%i for i in'abcde'])
    print(data_f)
    series_f = pd.Series(f,index=['%s'%i for i in'abcde'])
    print(series_f)
    data_f['g'] = 9 #添加列标签g，所有value是9 会直接改变data_f
    series_f['g'] = 9 #添加行标签index  会直接改变series_f
    print(data_f)
    print('='*50)
    print(series_f)
    addindex_f = data_f.reindex(['a','c','b','d','f']) #不会改变data_f
    print('='*50)
    print(addindex_f)
    print(data_f)
kill_dataframe() 