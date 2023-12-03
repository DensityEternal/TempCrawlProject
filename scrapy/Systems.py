# 导入tkinter模块
import tkinter as tk
import tkinter.messagebox
from tkinter import *


# 定义事件处理函数
def show_room_number():
    # 在文本框中显示包间号
    text.delete(0, tk.END)  # 清空文本框
    text.insert(0, "包间号：101")  # 插入文本


def show_amount():
    # 在文本框中显示消费金额
    text.delete(0, tk.END)  # 清空文本框
    text.insert(0, "消费金额：1000元")  # 插入文本


def show_card_number():
    # 在文本框中显示会员卡号
    text.delete(0, tk.END)  # 清空文本框
    text.insert(0, "会员卡号：123456789")  # 插入文本


def show_card_settlement():
    # 在文本框中显示会员卡结算
    text.delete(0, tk.END)  # 清空文本框
    text.insert(0, "会员卡结算：900元")  # 插入文本


def show_settlement():
    # 在文本框中显示结算
    text.delete(0, tk.END)  # 清空文本框
    text.insert(0, "结算：100元")  # 插入文本


# 创建主窗口对象
root = tk.Tk()

root.geometry('')
# 创建四个按钮对象，并设置文字和事件处理函数
frame1 = Frame(root, relief=RAISED, borderwidth=2)
frame1.pack(side=RIGHT, fill=Y, ipadx='50p', ipady='50p', expand=0)
button1 = tk.Button(root, text="包间号", command=show_room_number)
button2 = tk.Button(root, text="消费金额", command=show_amount)
button3 = tk.Button(root, text="会员卡号", command=show_card_number)
button4 = tk.Button(root, text="会员卡结算", command=show_card_settlement)
frame2 = Frame(root, relief=RAISED, borderwidth=2)
button5 = tk.Button(root, text="结算", command=show_settlement)


def handleProtocol():
    if tkinter.messagebox.askokcancel('提示', '请确定结帐金额'):
        root.destroy()


# 创建一个文本框对象，并设置初始文字
text = tk.Entry(root)
text.insert(0, "欢迎使用饭店管理系统")

# 布局控件，让它们在主窗口上显示出来
button1.pack(side=tk.RIGHT, padx='0.1i', pady='0.1i')
button2.pack(side=tk.RIGHT, padx='0.1i', pady='0.1i')
button3.pack(side=tk.RIGHT, padx='0.1i', pady='0.1i')
button4.pack(side=tk.RIGHT, padx='0.1i', pady='0.1i')
button5.pack(side=tk.LEFT)
text.pack()

# 启动主循环，让GUI程序运行起来，并且响应用户的操作
root.protocol("WM_DELETE_WINDOW", handleProtocol())
root.mainloop()
