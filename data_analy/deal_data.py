import json
import numpy as np
import pandas as pd


def json_loads():
    #json数据
    obj = """
    {"data": {
            "bar": 1,
            "logo": 1,
            "entr": 1,
            "act": [{
                "name": "Major",
                "en_type": 1,
                "en_word": "Major",
                "en_pic": "",
                "start_time": 1636287660,
                "end_time": 1636324200,
                "course_open": 0}]
            }
    }
    """
    res = json.loads(obj) #将json字符串转换成python
    res1 = json.dumps(res) #将python转换成json
    sib = pd.DataFrame(res['data'],index=['a'],columns=['logo','entr']) #转换其中的一部分为dataframe
    print(sib)

dict_data = [np.random.randint(1,100,size=(100)),np.random.randn(100),np.arange(1,101)]
d_data = pd.DataFrame(dict_data).T
d_data.to_csv('hugef.csv')
def huge_file():
    #分块读取大文件
    agg1 = pd.read_csv(r'hugef.csv') #读取文件
    '''文件过大时，会占用很大内存,打开困难'''
    #使用迭代对象读取
    agg1 = pd.read_csv(r'hugef.csv',chunksize=5) #迭代读取前5行
    print(agg1.get_chunk()) #默认读取chunksize=5
    agg1 = pd.read_csv(r'hugef.csv',iterator=True)
    print(agg1.get_chunk(5))

    #移除重复数据
    data = pd.DataFrame({'k1':['one','two']*3+['two'],'k2':[1,1,2,3,3,4,4]})
    print(data)
    chick = data.duplicated() #检查出现的重复数据,重复的返回True
    print(chick)
    chick2 = data.drop_duplicates(['k1'],keep='last') #丢弃k1列出现的重复值 默认保留第一个值:keep='first'
    print(chick2)

    #利用函数、映射进行数据转换
    data = pd.DataFrame({'food':['apple','banana','Mango','orange','tomato','Apple'],
                        'price':[3.2,2.4,5.3,4.6,1.2,2.4]})
    print(data)
    #插入一列映射‘food’的值的‘kind‘
    fun = {'apple':'fruit','banana':'fruit','mango':'fruit','orange':'fruit','tomato':'vegetable'}
    data['kind'] = data[('food')].str.lower().map(fun) # 不区分大小写地映射
    print(data)

    #替换更改index
    data.index=data['food']
    data1 = data.drop('food',axis=1)
    print(data1)
    data2 = data1.rename(index=str.title,columns=str.upper) #title 首字母大写
    print(data2)
    data2.rename(index={'Apple':"苹果"},columns={'PRICE':'价格'},inplace=True)
    print(data2)

'''
ending to jupyter
'''