# hello lixiang 
import re
import csv

x = str(input())

def data():
    res = list(filter(None,str.split(x)))
    print(res)
    select_col = re.findall('第(\d+?)行',res[1])
    select_row = re.findall('第(\d+?)列',res[1])
    get_address = re.findall("'(.*?)'",x)[0]
    print(get_address)
    with open (get_address,'r') as fp :
        reader = csv.reader(fp)
        for a in reader :
            print(a)
if ".csv' 删除" in x :
    data()
