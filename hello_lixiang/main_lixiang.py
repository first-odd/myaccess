# hello lixiang 
import re
import csv

x = str(input())

def deal():
    print("你想让我打电话吗")
    y = str(input())
    if y == "是的":
        print("好的")
    else :print("尚未明确")

def data():
    res = list(filter(None,str.split(x)))
    select_col = re.findall('第(\d+?)行',res[1])
    select_row = re.findall('第(\d+?)列',res[1])
    print(select_col)
    print(select_row)

if "电话" in x :
    deal()

if ".csv' 删除" in x :
    data()
