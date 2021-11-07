from numpy.core.fromnumeric import size, var
from numpy.lib.function_base import append
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
    print('='*50)
    series_f = pd.Series(f,index=['%s'%i for i in'abcde'])
    print(series_f)
    print('='*50)
    
    #插入数据
    data_f['g'] = 9 #添加dataframe列，标签g，所有value是9 
    data_f.loc['f'] = [9,6] #想要添加dataframe行索引，需要loc 
    data_f.insert(1,'h',80) #在第1列之前添加索引‘h’，value是80 这些都会直接改变data_f 
    series_f['g'] = 9 #添加行标签index  会直接改变series_f 

    f2 = pd.Series({'h':100})
    varied_series_f = series_f.append(f2)  #新建一个series 使用append添加到series_f，不改变series_f数据
    print(varied_series_f)  

    addindex_f = data_f.reindex(['a','c','b','d','f']) #不会改变data_f
    row = {0:3,'h':4,'g':4}
    varied_data_f = data_f.append(row,ignore_index=True) #新建一个字典row添加到data_f中,不会影响data_f数据,是否忽略其index，恢复默认index
    print(varied_data_f)

    #删除数据  用del drop删除列，del直接删除 drop传递删除  drop(,,axis,inplace=T/F) inplace是否对原对象删除
    data_l = pd.DataFrame({'a':np.arange(1,5),'b':3,'c':4,'d':7},index=['%s'%i for i in 'ABCD'])
    print(data_l)
    del data_l['a']
    print(data_l)
    varied_data_l = data_l.drop('b',axis=1) #默认删除行，指定axis=1删除第二层
    varied_data_l = data_l.drop(['c','d'],axis=1) #可以删除多列
    print(varied_data_l)
    print(data_l)

    #修改数据
    #dataframe需要用到loc标签索引
    f = np.arange(1,16)
    data_f = pd.DataFrame(f.reshape(5,3),index=['%s'%i for i in'abcde'],columns=['A','B','C'])
    series_f = pd.Series(f,index=['%s'%i for i in 'abcdefghijklmno'])
    series_f[0] = 99 #series只有一列，直接更改 位置索引
    series_f['b'] = 99 #直接索引更改
    data_f['A'] = 999 #会修改A整列数据[,,,,]  标签索引
    data_f.A = 888 #和上一步一样的效果    
    data_f['a'] = 999 #列索引没有a，虽然行索引有，但是没用，会直接添加a列，值全是999
    data_f.loc['a'] = 777 #a行全部更改为777
    data_f.loc['a','A'] = 666 #对a行A列修改
    print(series_f)
    print(data_f)

    #查看数据 切片索引 bool索引 series_f[0] series_f['a'] series_f[0:4]位置切片顾头不顾尾，series_f['a':'f']标签切片顾头顾尾
    #不连续索引  series：[['a','f']] [[1,5,8,0]] dataframe 不能不连续位置索引：dataframe[[1,4,5]]是无效的 :key
    v1 = data_f[['A','a']] #取这两列
    v2 = data_f.loc[['a','d']] #取这两行
    v3 = data_f['A']['a']  #先写列再写行 ： A列a行
    v4 = data_f[:2] #切片输出前2行
    V5 = data_f.loc['a':'d','A':'C'] #先切片行标签，后切片列标签

    #loc 标签索引 iloc 位置索引
    v1 = data_f.iloc[0:2,1:3]
    print(v1)

def cal_pandas():

cal_pandas()