from os import name
from numpy.core.fromnumeric import size
import pandas as pd
import numpy as np

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
    s = pd.Series(s,index=['a','b','c','d','e','f1'])
    s.name = 'temp' #对象名
    s.index.name = 'year' #对象索引名
    print(s.head())  #s.head() 默认输出前5行   s.tail()默认输出后5行

def kill_dframe():
    d = {'a':[1,2,3],'b':(4,5,6),'c':np.arange(7,10)} #列表、元组、数组 构成的字典
    print(d)
    frame = pd.dFrame(d) # 转换成daraframe
    print(frame)  
    print('='*50)
    print(frame.values) 
    print(frame.index) #查看行索引
    print(frame.columns) #查看列索引
    print('='*50)
    change_index = pd.dFrame(d,index=['A','B','C'],columns=['a','b','c','e']) #keys当作了列索引，不能更改，只能添加 
                                                                              #index第0层 columns第1层
    print(change_index)

    # series构成的字典，转换成dframe
    d1 = pd.dFrame({'a':pd.Series(np.arange(5)),
                          'b':pd.Series(np.arange(5,10))})
    print(d1)

    #嵌套字典，转换成dframe
    d2 = {'a':{'apple':3.5,'banana':3.8},
            'b':{'apple':3,'banana':5},
            'c':{'apple':2}}
    change_d2 = pd.dFrame(d2)
    print(change_d2)

    # 二维数组 转换成dframe
    double_list = np.arange(15).reshape(3,5)
    vary = pd.dFrame(double_list)
    print(vary)

    #字典构成的列表，转换成dframe
    dict_list = [{'apple':3.5,'banana':3.8},
                {'apple':3,'banana':5},
                {'apple':2}]
    vary = pd.dFrame(dict_list)
    print(vary)

    #series构成的列表，转换成dframe3
    series_list = [pd.Series(np.random.rand(3)),pd.Series(np.random.rand(2))]
    print(series_list)
    print('='*50)
    vary = pd.dFrame(series_list)
    print(vary)

    set_frame = pd.dFrame(np.arange(9).reshape(3,3),index=['a','c','b'],columns=['A','B','C'])
    set_frame['D'] = [1,2,3] #增加D列
    print(set_frame.T) #转置
    print('='*50)
    print(set_frame['A']) #索引A列 

    '''
    index索引不可更改，需要创建新索引：reindex来新增或者改变顺序
    '''
    f1 = np.arange(5)
    d_f = pd.dFrame(f1,index=['%s'%i for i in'abcde'])
    print(d_f)
    print('='*50)
    series_f = pd.Series(f1,index=['%s'%i for i in'abcde'])
    print(series_f)
    print('='*50)
    
    #插入数据
    d_f['g'] = 9 #添加dframe列，标签g，所有value是9 
    d_f.loc['f1'] = [9,6] #想要添加dframe行索引，需要loc 
    d_f.insert(1,'h',80) #在第1列之前添加索引‘h’，value是80 这些都会直接改变d_f 
    series_f['g'] = 9 #添加行标签index  会直接改变series_f 

    f2 = pd.Series({'h':100})
    d_series_f = series_f.append(f2)  #新建一个series 使用append添加到series_f，不改变series_f数据
    print(d_series_f)  

    addindex_f = d_f.reindex(['a','c','b','d','f1']) #不会改变d_f
    row = {0:3,'h':4,'g':4}
    d_d_f = d_f.append(row,ignore_index=True) #新建一个字典row添加到d_f中,不会影响d_f数据,是否忽略其index，恢复默认index
    print(d_d_f)

    #删除数据  用del drop删除列，del直接删除 drop传递删除  drop(,,axis,inplace=T/F) inplace是否对原对象删除
    d_l = pd.dFrame({'a':np.arange(1,5),'b':3,'c':4,'d':7},index=['%s'%i for i in 'ABCD'])
    print(d_l)
    del d_l['a']
    print(d_l)
    d_d_l = d_l.drop('b',axis=1) #默认删除行，指定axis=1删除第二层
    d_d_l = d_l.drop(['c','d'],axis=1) #可以删除多列
    print(d_d_l)
    print(d_l)

    #修改数据
    #dframe需要用到loc标签索引
    f1 = np.arange(1,16)
    d_f = pd.dFrame(f1.reshape(5,3),index=['%s'%i for i in'abcde'],columns=['A','B','C'])
    series_f = pd.Series(f1,index=['%s'%i for i in 'abcdefghijklmno'])
    series_f[0] = 99 #series只有一列，直接更改 位置索引
    series_f['b'] = 99 #直接索引更改
    d_f['A'] = 999 #会修改A整列数据[,,,,]  标签索引
    d_f.A = 888 #和上一步一样的效果    
    d_f['a'] = 999 #列索引没有a，虽然行索引有，但是没用，会直接添加a列，值全是999
    d_f.loc['a'] = 777 #a行全部更改为777
    d_f.loc['a','A'] = 666 #对a行A列修改
    print(series_f)
    print(d_f)

    #查看数据 切片索引 bool索引 series_f[0] series_f['a'] series_f[0:4]位置切片顾头不顾尾，series_f['a':'f1']标签切片顾头顾尾
    #不连续索引  series：[['a','f1']] [[1,5,8,0]] dframe 不能不连续位置索引：dframe[[1,4,5]]是无效的 :key
    v1 = d_f[['A','a']] #取这两列
    v2 = d_f.loc[['a','d']] #取这两行
    v3 = d_f['A']['a']  #先写列再写行 ： A列a行
    v4 = d_f[:2] #切片输出前2行
    V5 = d_f.loc['a':'d','A':'C'] #先切片行标签，后切片列标签

    #loc 标签索引 iloc 位置索引
    v1 = d_f.iloc[0:2,1:3]
    print(v1)

def cal_pandas():
    s1 = pd.Series(np.arange(5),index=list('ABCDE'))
    s2 = pd.Series(np.arange(6),index=list('ABCDEF')) 
    print(s1+s2)  # pandas的对齐运算，一方没有标签的值补充NAN
    result = s2.add(s1,fill_value=0) #让一方不存在的标签值=0，双方都没有的值才为nan
    print(result)
    arr1 = np.arange(1,13).reshape(3,4)
    print(arr1)
    print(arr1+arr1[0])  # numpy广播性质

    d_a = pd.DataFrame(arr1,index=list('ABC'),columns=list('abcd'))
    print(d_a)
    print(d_a.iloc[0])
    print(d_a.add(d_a.iloc[0])) #pandas广播性质,默认列方向：所有行加上d_a.iloc[0]
    print(d_a.add(d_a.iloc[0],axis=1)) #等同于上一步 或者 axis='columns'

def apply_pandas():
    df = pd.DataFrame(np.random.randn(4,5),index=list('ABCD'),columns=list('abcde'))
    ab = np.abs(df)
    f1 = lambda x:x.max(axis=0)
    vf1 = df.apply(f1)
    f2 = lambda x:'%.2f'%x
    vf2 = df.applymap(f2)
    print(df)
    print(vf1)
    print(vf2)

#pandas排序
def sort_pandas():
    df = pd.DataFrame(np.random.randint(-5,10,size=(6,6)),index=list('FEDBCA'),columns=list('fcbade'))
    print(df)
    #排序标签 sort_index
    vf = df.sort_index(axis=1) #排序columns，默认升序:ascending=True
    vf = df.sort_index(ascending=False,axis=0) #降序

    #排序values
    vf = df.sort_values(by='a') # a列 升序
    print('*'*80)
    print(vf)
    jf = df.value_counts('c') #计数
    bf = df.isin([2,5]) #是否是2或5
    print(jf)
    print(bf)
 

'''
处理缺失值
#判断是否存在缺失值
#丢弃缺失值 dropna()
'''
def nan_pandas():
    df = pd.DataFrame([np.random.randn(3),[1,2,np.nan],[1,2,3],[np.nan,2,np.nan]])
    print(df)
    vf1 = df.isnull() #判断是否存在缺失值
    print(vf1)
    vf2 = df.dropna() #默认丢弃掉存在nan的行
    print(vf2)
    vf2 = df.dropna(axis=1)
    #填充缺失值
    vf3 = df.fillna(999)
    print(vf3)

def multi_index():
    f = np.random.randint(1,10,6)
    df = pd.Series(f,index=[['a','a','b','b','c','c'],[0,1,0,1,0,1]]) #层级索引
    print(df)
    print(df['a']) #外层索引
    print(df[:,0]) #内层索引
    print(df['a',0]) #双层索引
    cf = df.swaplevel()
    print(cf)

def deal_dataframe():
    f = pd.DataFrame([[1,np.nan,2],np.random.randint(-1,3,size=3),np.random.randn(3)])
    f.index=['a','b','c'];f.columns=list('ABC')
    print(f)
    vf1 = f.sum(skipna=False) #默认axis=0求和：每列求和 不要跳过nan
    #与numpy不同，pandas会默认skipna=True:跳过nan，假设为0.0
    print('*'*80)
    print(vf1)
    vf2 = f.idxmax(axis=0) #输出最大值的标签
    print(vf2)
    vf3 = f.cumsum() #累计和 
    print(vf3)
    '''
    count:非nan值数量
    describe：汇总（最大值、四分位25%、中位数50%、平均数、标准差等）
    median：算术中位数
    mad：平均绝对离差
    var：方差
    std：标准差
    skew：偏度（三阶距）
    kurt：峰度（四阶距）
    cumsum：累计和 cumprod：累计积
    diff：一阶差分
    '''
def data_base():
    df = pd.DataFrame([[2,3,4,5],
                    [1,3,4,5],
                    [2,4,1,3],
                    [5,7,3,5]])
    df.to_csv('es.csv') #逗号分隔开
    f = pd.read_csv('es.csv',names=['a','b','c','d'])
    print(f)
data_base() 