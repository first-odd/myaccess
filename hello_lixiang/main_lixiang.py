# hello lixiang 
import re
import csv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

x = str(input())

def data():
    res = list(filter(None,str.split(x)))
    select_row = re.findall('第(\d+?)行',res[1])[0]
    select_col = re.findall('第(\d+?)列',res[1])[0]
    l = int(select_col) - 1
    h = int(select_row) - 1
    get_address = re.findall("'(.*?)'",x)[0]
    with open (get_address,'r',encoding='utf-8') as fp :
        reader = csv.reader(fp)
        c = list(reader)
        c = np.array(c)
    c[h][l] = ""
    
    header = c[0]
    values = []
    for i in np.arange(1,c.shape[0]) :
        values.append(c[i])
    with open (get_address,'w',encoding='utf-8') as fp1:
        abc = csv.writer(fp1)
        abc.writerow(header)
        abc.writerows(values)
    print('ok')

if ".csv' 删除" in x :
    data()
