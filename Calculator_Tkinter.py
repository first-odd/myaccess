from tkinter import *

#设置窗口    
x = Tk()
x.title("Calculator")            
x.geometry('305x460+1200+20')
x.resizable(0,0)                
#self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
vary = StringVar()
vary.set('')
#标签
result = Label(x, textvariable=vary,font=('',20,),width=22,height=1,anchor=W)
result.grid(row=0, column=0)

#功能代码部分
def getnum(num):
    global temp
    temp = vary.get()
    if temp=='0':
        temp=''
    temp = temp + num
    vary.set(temp)

def clear(self):
    vary.set('')

def run(self):
    temp = vary.get()
    temp.replace('X','*')
    temp.replace('/','/')
    answer = calculator(temp)
    if temp == '520':
        vary.set("我爱你")
    else: vary.set(str(answer))

def calculator(fuck):
    s = fuck.split('+')
    fuck = int(s[0]) + int(s[1])
    return fuck

#第一行
ACbutton = Button(x, text="AC", bg="lightblue",width=8,height=5,command=lambda:clear('AC')).place(x=0,y=150)
button_ = Button(x, text="一", bg="lightblue", width=8,height=5,command=lambda:getnum('-')).place(x=76,y=150)
buttonx = Button(x, text="X", bg="lightblue", width=8,height=5,command=lambda:getnum('X')).place(x=152,y=150)
buttond = Button(x, text="/", bg="lightblue", width=8,height=5,command=lambda:getnum('/')).place(x=228,y=150)
#第二行
button1 = Button(x, text="1", bg="lightblue", width=8,height=5,command=lambda:getnum('1')).place(x=0,y=225)
button2 = Button(x, text="2", bg="lightblue", width=8,height=5,command=lambda:getnum('2')).place(x=76,y=225)
button3 = Button(x, text="3", bg="lightblue", width=8,height=5,command=lambda:getnum('3')).place(x=152,y=225)
button4 = Button(x, text="4", bg="lightblue", width=8,height=5,command=lambda:getnum('4')).place(x=228,y=225)
#第三行
button5 = Button(x, text="5", bg="lightblue", width=8,height=5,command=lambda:getnum('5')).place(x=0,y=300)
button6 = Button(x, text="6", bg="lightblue", width=8,height=5,command=lambda:getnum('6')).place(x=76,y=300)
button7 = Button(x, text="7", bg="lightblue", width=8,height=5,command=lambda:getnum('7')).place(x=152,y=300)
button8 = Button(x, text="8", bg="lightblue", width=8,height=5,command=lambda:getnum('8')).place(x=228,y=300)
#第四行
button9 = Button(x, text="9", bg="lightblue", width=8,height=5,command=lambda:getnum('9')).place(x=0,y=375)
button0 = Button(x, text="0", bg="lightblue", width=8,height=5,command=lambda:getnum('0')).place(x=76,y=375)
buttonp = Button(x, text="+", bg="lightblue", width=8,height=5,command=lambda:getnum('+')).place(x=152,y=375)
buttone = Button(x, text="=", bg="lightblue", width=8,height=5,command=lambda:run('=')).place(x=228,y=375)

x.mainloop()
