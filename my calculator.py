from tkinter import *
import math

root= Tk()
root.title("Simple Calculator")

e = Entry(root, width=63,borderwidth=10)
e.grid(row=0,column=0,columnspan=4)

def buttonclick(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))

def buttonclear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global calc
    calc = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equals():
    second_number = e.get()
    e.delete(0, END)

    if calc == "addition":
        add = f_num + int(second_number)
        e.insert(0, add)
    if calc == "subtraction":
        sub = f_num - int(second_number)
        e.insert(0, sub)
    if calc == "multiplication":
        mul = f_num * int(second_number)
        e.insert(0, mul)
    if calc == "division":
        div = f_num / int(second_number)
        e.insert(0, div)
    if calc == "sin":
        sin_res = math.sin((f_num)*(180/math.pi))
        e.insert(0, sin_res)
    if calc == "log":
        lg = math.log10(f_num)
        e.insert(0, lg)
    if calc == "exp":
        res = math.exp(f_num)
        e.insert(0, res)

    if calc == "sqrt":
        s=math.sqrt(f_num)
        e.insert(0, s)


def button_subtract():
    first_number = e.get()
    global f_num
    global calc
    calc = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global calc
    calc = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global calc
    calc = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_sin():
    first_number = e.get()
    global f_num
    global calc
    calc = "sin"
    f_num = int(first_number)
    e.delete(0, END)

def button_log():
    first_number = e.get()
    global f_num
    global calc
    calc = "log"
    f_num = int(first_number)
    e.delete(0, END)

def button_exp():
    first_number = e.get()
    global f_num
    global calc
    calc = "exp"
    f_num = int(first_number)
    e.delete(0, END)

def button_sqrt():
    first_number = e.get()
    global f_num
    global calc
    calc = "sqrt"
    f_num = int(first_number)
    e.delete(0, END)




button1= Button(root, text="1", padx=50, pady=22,command= lambda: buttonclick(1),bg="black",fg="white")
button2= Button(root, text="2", padx=54, pady=22,command= lambda: buttonclick(2),bg="black",fg="white")
button3= Button(root, text="3", padx=53, pady=22,command= lambda: buttonclick(3),bg="black",fg="white")
button4= Button(root, text="4", padx=50, pady=27,command= lambda: buttonclick(4),bg="black",fg="white")
button5= Button(root, text="5", padx=54, pady=27,command= lambda: buttonclick(5),bg="black",fg="white")
button6= Button(root, text="6", padx=53, pady=27,command= lambda: buttonclick(6),bg="black",fg="white")
button7= Button(root, text="7", padx=50, pady=20,command= lambda: buttonclick(7),bg="black",fg="white")
button8= Button(root, text="8", padx=54, pady=20,command= lambda: buttonclick(8),bg="black",fg="white")
button9= Button(root, text="9", padx=53, pady=20,command= lambda: buttonclick(9),bg="black",fg="white")
button0= Button(root, text="0", padx=111, pady=21,command= lambda: buttonclick(0),bg="black",fg="white")

buttonadd= Button(root, text="+", padx=53, pady=59,command= button_add,bg="green")
buttonmul= Button(root, text="*", padx=54, pady=20,command=button_multiply,bg="green")
buttondiv= Button(root, text="/", padx=54, pady=20,command=button_divide,bg="green")
buttonsub= Button(root, text="-", padx=54, pady=20,command=button_subtract,bg="green")

buttonequ= Button(root, text="=", padx=53, pady=55,command=button_equals)
buttonclear= Button(root, text="Clear", padx=42, pady=20,command=buttonclear,bg="blue")
buttondot= Button(root, text=".", padx=51, pady=20,command= lambda: buttonclick("."))

buttonsin= Button(root, text="sin", padx=45, pady=15,command=button_sin,bg="yellow")
buttonlog= Button(root, text="log", padx=47, pady=15,command=button_log,bg="yellow")
buttonexp= Button(root, text="exp", padx=47, pady=15,command=button_exp,bg="yellow")
buttonsqrt= Button(root, text="sqrt", padx=45, pady=15,command=button_sqrt,bg="yellow")



button1.grid(row=4,column=0)
button2.grid(row=4,column=1)
button3.grid(row=4,column=2)

button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)

button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)

button0.grid(row=5,column=0,columnspan=2)

buttonadd.grid(row=2,column=3,rowspan=2)
buttonmul.grid(row=1,column=2)
buttondiv.grid(row=1,column=1)
buttonsub.grid(row=1,column=3)
buttondot.grid(row=1,column=0)

buttonsin.grid(row=6,column=0)
buttonlog.grid(row=6,column=1)
buttonexp.grid(row=6,column=2)
buttonsqrt.grid(row=6,column=3)


buttonequ.grid(row=4,column=3,rowspan=2)
buttonclear.grid(row=5,column=2)









root.mainloop()