import numpy as np    #练习使用numpy库
import time
import csv

from numpy.core.fromnumeric import size


def compare():
    t1 = time.time()
    a = []
    for x in range(1000000):   #[0,10) = [0,9]
        a.append(x**2)    #在末尾添加元素
    t2 = time.time()
    print(t2-t1)

    t3 = time.time()
    b = np.arange(1000000)**2  # np.arange和range类似用法
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
    dtype获取数据类型 用astype设定类型
    ndim获取维度
    shape获取形状（几行几列）
    size获取元素个数
    itemsize获取数组中，单个元素所占字节大小
    reshape函数可以改变np数组的形状，保持数字数量不变 eg：A1.reshape((2,2))  
    flatten函数可以直接吧np数组变为一维数组'''

def array_cal():
    '''
    数组和数字可以直接运算
    数组的shape相同，可以直接运算
    shape不同的数组运算，需要满足 广播原则:两个shape.维度从后往前数，相同或有一个是1，称为广播相融，
    shape。size=(3,8,2)和size=(8,3)不能运算，2和3不想等，且都不是1
    size=(3,8,2)可以和size=(8,1)运算,但是不能和size=(3,1)运算
    但是size=(3,8,1)可以和size=(1,8)运算,得到8行8列
    总结：行和列一定都要够，如果不够，只能为1
    '''
    a = np.arange(10)
    a = a*2 #所有元素*2
    print(a)
    b = np.arange(20)
    b.resize(4,5)           
    '''resize可以改变数组 b 的形状，b.resize(4,5) 相当于 b=np.arange(20).shape(4,5) 也相当于 b=b.reshape(4,5)'''
    c = np.random.randint(1,5,size=(4,5))
    d = np.eye(4,5)
    e = b+c*d
    f = np.random.randint(1,5,size=(3,8,8))
    g = np.random.randint(2,6,size=(8,1))
    print(c,'\n',"="*30,'\n',d,'\n',"="*30,'\n',e,'\n',"="*30,'\n',f+g,'\n',"="*30,'\n',b)
    '''flatten 和 ravel  都可以把数组转为一维，都不会改变原数组的形状，ravel可以直接修改原数组本身数据，flatten是副本，不能修改'''

#数组的叠加、切割
def vstack_array():
    '''
    行相等才能垂直方向拼接，列相等才能水平方向拼接
    '''
    c = np.random.randint(1,5,size=(4,5))
    d = np.random.randint(1,6,size=(2,5))
    e = np.vstack([c,d])    #vstack 在上下方向拼接，要求列相等   
    d = np.vsplit(e,2)      #vsplit 横切  2:平均分成两份，要保证能均分，不然报错
    f = np.vsplit(e,(1,2))  # e目前共有6行，从1行前、2行前切一刀,剩下4行不切
    print(e)
    print('='*40)
    print(f)
    print('='*40)
    print(d[0])
    print('='*40)
    print(d[1])
    print('='*40)
    c = np.random.randint(1,5,size=(4,5))
    d = np.random.randint(1,5,size=(4,3))
    e = np.hstack([c,d])    #hstack 在左右方向拼接，要求行相等   #hsplit 竖切
    f = np.hsplit(e,2)      #竖着平均成2份 ，不能平均会报错
    f = np.hsplit(e,(1,3))  #分别从1列、3列前切,剩余保留
    print(e)
    print('='*40)
    print(f)
    c = np.random.randint(1,5,size=(4,5))
    d = np.random.randint(1,5,size=(2,3))
    e = np.concatenate([c,d],axis=None) #axis=None，都变成一维数组再拼接        
    print(e)
    c = np.random.randint(1,5,size=(4,5))
    d = np.random.randint(1,5,size=(4,3))
    e = np.concatenate([c,d],axis=1)  #axis=1,左右拼接，axis=0，上下拼接
    f = np.split(e,2,axis=1)    #按左右平均分成2份
    g = np.array_split(e,2,axis=1)  #array_split和split一样的用法
    h = np.split(e,(1,2),axis=1)   #分别在1列、2列前切，剩下不切
    print(e)
    print('='*40)
    print(f)
    print('='*40)
    print(g)
    print('='*40)
    print(h)

    #数组的转置ndarray.T 和ndarray.transpose 一样的用法，都会修改原数组
    t1 = np.random.randint(1,3,size=(2,3))
    t2 = t1.T
    print(t1)
    print('='*40)
    print(t2)

    '''
    深拷贝 view & 浅拷贝 copy
    '''
def file():
    #CSV文件的保存和读取
    f1 = np.random.randint(1,100,size=(30,2))
    np.savetxt('scores.csv',f1,fmt='%d',delimiter=',',header='英语,数学',footer='',comments='')
    #np.savetxt只能存储 1维2维数组
    read_f1,f2 = np.loadtxt('scores.csv',dtype=int,delimiter=',',skiprows=1,unpack=True,usecols=(0,1)) 
    # usecols=(0,1) read_f1: 第0列   f2:第1列  unpack：是否转置  loadtext默认读取成float浮点类型，需要使用dtype
    '''print(f2)
    print(read_f1)'''
    '''
    np.save(fname,array) & np.savez(fname,array) 前者存储.npy文件，后者存储.npz压缩文件,都是非文本文件
    可以储存多维的数组
    读取的时候用np.load(fname.npy or fname.npz)
    '''
    with open('scores.csv','r',encoding='utf-8') as fp:
        reader = csv.reader(fp) #reader是一个迭代器,返回数组
        next(reader) #跳过一行
        for x in reader: #遍历reader 得到整个数据
            print(x)
            #subject = x[0]
            #score = x[1]
            #print({'英语':subject,'数学':score})
    #csv.reader来读取csv文件

    #csv.DictReader来读取文件 不会包含标题那一行 ，而是直接把header传入字典当作key值
    with open('scores.csv','r') as fp1:
        reader = csv.DictReader(fp1)  #reader直接返回一个字典
        for x in reader:
            #print(x)  
            print({'英语':x['英语']})   #迭代输出标题是英语的value，此外 由于没有了标题，x[0]也不存在了，直接从x[1]开始
            print({'数学':x['数学']})
            #print(x[1])

    #csv数据的写入 writer
    header = ['name','age','height']
    values = [
        ('张三',18,180),
        ('李四',13,180),
        ('王五',13,180)
    ]
    with open('scores.csv','w',encoding='utf-8',newline='') as fp2:
        abc = csv.writer(fp2)
        abc.writerow(header)
        abc.writerows(values)

    #csv数据的写入  DictWriter 字典写入
    headers = ['name','age','height']
    values = [
        {'name':'张三','age':18,'height':180},
        {'name':'李四','age':14,'height':180},
        {'name':'王五','age':15,'height':180}
    ]
    with open('scores.csv','w',encoding='utf-8') as fp3:
        writer = csv.DictWriter(fp3,headers)
        writer.writeheader()  # 需要调用 writeheader() 写一次表头
        writer.writerows(values)

'''
处理数据缺失值
'''
# NAN 和 INF 的认识 & 处理 np.inf:正无穷大 -np.inf :负无穷大
def spc_value():
    #NAN ：not a number
    data = np.random.randint(1,5,size=(3,4))
    '''data[0,1] = np.NAN # 此时会报错data，因为nan是浮点类型，要保持数组内类型一致'''
    data = data.astype(np.float64)
    data[0,1] = np.nan
    data[1,2] = np.nan
    print(data)
    '''可以用 np.isnan判断是否是nan值，不用用判断语句 np.nan == np.nan'''
    bool = np.isnan(data) ;print(bool)# 返回判断是否为nan，返回bool数组
    '''如果直接删除数组中的nan值，会直接输出一维数组'''
    judge = data[np.isnan(data)] # bool索引为True
    num= data[~np.isnan(data)]   # ~ :取反运算符
    print(num)  # 此时输出为一位数组

    #要删除nan所在行或者列 ：1.where 获取nan所在行/列   2. delete 删除这些行/列
    data = np.random.randint(1,5,size=(5,5)).astype(np.float32)
    data[[0,2],[1,3]] = np.nan
    print(data)
    lines = np.where(np.isnan(data))  
    # where(if,1,0) where返回满足条件if的设置为1,不满足的为0,不设置1,0就返回array行列数
    lines1 = np.where(np.isnan(data))[0] #二维数组，第一个是其行数，取其行数
    print(lines1)
    data1 = np.delete(data,lines1,axis=0) #删除所在行，delete用0表示行，其余用0表示列
    print(data1)

    '''
    因为没有合适数据库，创建：
    f1 = np.random.randint(10,90,size=(10,10))
    np.savetxt('test.csv',f1,fmt='%d',delimiter=',',comments='')
    人为去掉了其中的值'''
    #空数据无法用loadtext解析，先用str类型解析，根据需求值替换空值，再转换成浮点类型处理数据
    data = np.loadtxt('test.csv',encoding='utf-8',delimiter=',',dtype=str,skiprows=1,unpack=False)
    data[data==""] = np.nan #nan替代空值
    data1 = data.astype(np.float32)
    data1[np.isnan(data1)] = 0  #用0替换nan
    print(data1)
    data2 = data1.sum(axis=1) #对一行中的所有列求和
    print('='*80)
    mean_data = data.astype(np.float32)
    for x in range(mean_data.shape[1]):
        col = mean_data[:,x]   #取每列的值
        non_nan_col = col[~np.isnan(col)]
        mean = non_nan_col.mean()  # 求每列的平均值
        col[np.isnan(col)] = mean  # 把每列的平均值赋给每列的nan
    print(mean_data)

def learn_random():
    np.random.seed(1)  #给随机数传入seed，如果不指定，跟随时间戳
    print(np.random.rand())
    np.random.randn()  #生成标准正态分布的随机值 均值为0，标准差为1
    data = [1,2,2,3,4,4,5,1,2,3,]
    np.random.choice(data,7)          #随机选择7个属于data数组的值
    np.random.choice(data,size=(3,4)) #随机用data的值生成3行4列
    np.random.choice(5,size=(3,4))    #随机用0到5的数组成3行4列
    np.random.shuffle(data)           #随机打乱data数组

def learn_axis():
    a = [2,3];b = [3,4]
    print(a+b)  # 直接相加，意思是b在a后面进行拼接 其余运算符报错

    
learn_axis()