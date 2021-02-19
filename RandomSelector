-*- coding: utf-8 -*-
from tkinter import Entry,Button,Label,StringVar,Tk 
'''
为缩减打包体积，均如此导入，正确是import tkinter as tk，在上述导入的包在下面的使用前面加tk.就行
'''
from random import randint as ran # 导入随机整数
# from time import sleep

window = Tk() # 初始化窗口
window.geometry('750x450') #设置窗口大小
window.title('随机抽号') # 设置窗口标题
window.resizable(width=False,height=False) # 设置窗口大小是否允许调整
# for i in range(20):
#     s=ran(1,100)
#     print(s)
#     sleep(0.01)

number = StringVar() #赋值数字为label的text内容

############## 输入开始数字部分 #######################
fromnum = Entry(window, show=None, font=('Arial', 14)) # 开始数字输入
fromnum.place(x=10, y=10) # 放置位置
startnum = 1 #默认值1


def commit_a():
    global number
    global startnum
    try:
        startnum = int(fromnum.get())
    except:
        number.set('开始数字请输入数字！')


commitfrom = Button(window, text='确定', font=(
    'Arial', 12), width=5, height=1, command=commit_a)
commitfrom.place(x=250, y=10)

################## 输入结束数字部分 #######################
toend=Entry(window,show=None,font=('Arial',14))
toend.place(x=330,y=10)
endnum=50

def commit_b():
    """
    docstring
    """
    global number
    global endnum
    try:
        endnum=int(toend.get())
    except:
        number.set('结束数字请输入数字！')

commitend=Button(window,text='确定',font=('Arial',12),width=5,height=1,command=commit_b)
commitend.place(x=580,y=10)


############### 显示部分 #######################
numberlabel = Label(window, textvariable=number,
                       fg='red', font=('Arial', 28), width=50, height=3,anchor='center')
numberlabel.place(x=-175,y=230)
number.set('第一框输入起始数字，第二个输入结束数字\n按键开始，默认1-50\n不开始或不结束，请按多几次按钮')


############### control部分 ####################
running = False


def randnum():
    global running
    global number
    global window
    global startnum
    global endnum
    while running == False:
        if startnum>endnum:
            number.set('开始数字（默认1）\n不得\n大于结束数字（默认50）！')
            break
        num = ran(startnum, endnum)
        number.set('Number: '+str(num))
        # sleep(0.3)
        try:
            window.update()
        except:
            pass
    else:
        running = False


def stoprand():
    global running
    running = True

    # running=True
startbutton = Button(window, text='开始', font=(
    'Arial', 14), width=10, height=2, command=randnum)
startbutton.place(x=320,y=100)
stopbutton = Button(window, text='停止', font=(
    'Arial', 14), width=10, height=2, command=stoprand)
stopbutton.place(x=320,y=170)

################## Using Guide ##################
# tips=
window.mainloop()
try:
    window.destroy()
except:
    pass
