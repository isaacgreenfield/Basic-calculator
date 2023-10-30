from tkinter import *
from tkinter import ttk
import tkinter

number = ""
number1 = ""
number2 = ""

def input_number(widget):
    global number 
    number += widget
    Label_s.config(text = number)

def minus():
    global number
    global number1
    global number2
    if number1 == "":
        number1 = number
        number = ""
        Label_s.config(text = number)
        button_equals.config(command=lambda: minus())
    else:
        number2 = number
        number = (str)((int)(number1) - (int)(number2))
        number1 = ""
        number2 = ""
        Label_s.config(text = number)
        button_equals.config(command=None)

def plus():
    global number
    global number1
    global number2
    if number1 == "":
        number1 = number
        number = ""
        Label_s.config(text = number)
        button_equals.config(command=lambda: plus())
    else:
        number2 = number
        number = (str)((int)(number1) + (int)(number2))
        number1 = ""
        number2 = ""
        Label_s.config(text = number)
        button_equals.config(command=None)

def multiplicate():
    global number
    global number1
    global number2  
    if number1 == "":
        number1 = number
        number = ""
        Label_s.config(text = number)
        button_equals.config(command=lambda: multiplicate())
    else:
       number2 = number
       number = (str)((int)(number1) * (int)(number2))
       number1 = ""
       number2 = ""
       Label_s.config(text = number)
       button_equals.config(command=None)

def divide():
    global number
    global number1
    global number2
    if number1 == "":
        number1 = number
        number = ""
        Label_s.config(text = number)
        button_equals.config(command=lambda: divide())
    else:
       number2 = number
       number = (str)((int)(number1) / (int)(number2))
       number1 = ""
       number2 = ""
       Label_s.config(text = number)
       button_equals.config(command=None)

def power():
    global number
    global number1
    global number2
    if number1 == "":
        number1 = number
        number = ""
        Label_s.config(text = number)
        button_equals.config(command=lambda: power())
    else:
       number2 = number
       number = (str)((int)(number1) ** (int)(number2))
       number1 = ""
       number2 = ""
       Label_s.config(text = number)
       button_equals.config(command=None)          

def CE():
    global number
    number = ""
    Label_s.config(text = number)
    
    
root = Tk()
root.title("Basic caclulator")
frm = ttk.Frame(root, padding=10)
frm.grid()

Label_s = tkinter.Label(root, borderwidth= 30)
button_equals = ttk.Button(text="=")

button_one = ttk.Button(text="1", command = lambda: input_number("1")).grid(column=0,row=1)
button_two = ttk.Button(text="2", command = lambda: input_number("2")).grid(column=1,row=1)
button_three = ttk.Button(text="3", command = lambda: input_number("3")).grid(column=2,row=1)
button_four = ttk.Button(text="4", command = lambda: input_number("4")).grid(column=0,row=2)
button_five = ttk.Button(text="5", command = lambda: input_number("5")).grid(column=1,row=2)
button_six = ttk.Button(text="6", command = lambda: input_number("6")).grid(column=2,row=2)
button_seven = ttk.Button(text="7", command = lambda: input_number("7")).grid(column=0,row=3)
button_eight = ttk.Button(text="8", command = lambda: input_number("8")).grid(column=1,row=3)
button_nine = ttk.Button(text="9", command = lambda: input_number("9")).grid(column=2,row=3)
Label_x = ttk.Label(text="").grid(column=0, row=4)
Label_x2 = ttk.Label(text="").grid(column=2, row=4)
button_zero = ttk.Button(text="0", command = lambda: input_number("0")).grid(column=1,row=4)

button_plus = ttk.Button(text="+", command= lambda: plus()).grid(row=1, column=3)
button_minus = ttk.Button(text="-", command= lambda: minus ()).grid(row=2, column=3)
button_c = ttk.Button(text="C", command= lambda: CE()).grid(row=0, column=3)
button_multiplicate = ttk.Button(text="X", command= lambda: multiplicate()).grid(row=1, column=4)
button_divide = ttk.Button(text="/", command= lambda: divide()).grid(row=2, column=4)
button_power = ttk.Button(text="P", command= lambda: power()).grid(row=0, column=4)

#button_one.place(height = 15, width = 15) #и так далее прописать + заменить .grid на .place(x = ..., y = ..., height = ..., width = ...)

Label_s.grid(column=0, row=0, columnspan= 3)
button_equals.grid(row=3, column=3, columnspan=2)
root.mainloop()