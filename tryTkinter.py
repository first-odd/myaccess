from tkinter import *
from tkinter.messagebox import *

a = Tk()
a.title('Try')
a.geometry('800x600+400+400')
    #root.iconbitmap('/Users/jacksonandrew/Downloads/favicon.ico')  插入一个icon
a.resizable(0,0)  #固定

#设置结果窗口
root = StringVar()
root.set('0')   #初始值
#Label
result = Label(a,text='结果', width=20,height=1,bd=10,anchor=NW,font=('',30,'bold'),bg='lightblue',fg='red',cursor='plus',textvariable='root')  #cursor 光标变化 arrow、circle、cross、plus
result.grid(row=0,column=0,sticky=W,padx=2) #紧贴左边，外边距2
#功能函数
def getnum(num):
    temp = root.get()
    root.set(temp)
    print(root)

'''#entry
word = Entry(a,bg='yellow')
word.grid(row=1,column=0,sticky=W)'''

#Button
n1 = Button(a,text='1',width=4,bd=10,height=2,anchor=NW,command=lambda:getnum('1'))
n1.grid(row=2,column=0,sticky=W)
n2 = Button(a,text='+',width=4,bd=10,height=2,anchor=NW,command=lambda:getnum('+'))
n2.grid(row=3,column=0,sticky=W)
n3 = Button(a,text='=',width=4,bd=10,height=2,command=lambda:getnum('='))
n3.grid(row=4,column=0,sticky=W)


a.mainloop()