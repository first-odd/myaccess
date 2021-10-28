from tkinter import *

full = Tk()
full.geometry('400x200+600+20')
vary = StringVar()
vary.set('')
init = Label(full,textvariable=vary,bg='lightblue',width=5,height=1)
init.place(x=10,y=10)
num = Button(full,text='1',width=5,height=2,command=lambda:getnum('1'))
num.place(x=10,y=40)
num0 = Button(full,text='0',width=5,height=2,command=lambda:getnum('0'))
num0.place(x=10,y=70)

def getnum(num):
    temp = vary.get()
    if temp=='0':
        temp=''
    temp = temp + num
    vary.set(temp)
full.mainloop()