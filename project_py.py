from tkinter import *
import tkinter as tk
import math
root = tk.Tk()
root.title("calculator")
root.geometry("400*360")
root.resizeable(0, 0)
font = ('Arial Bold', 17)
equation = " "

def button_press(value):
    global equation
    user = entry_result.get()
    equation += value
    if value=='x2':
        result == eval(equation)**2

    entry_result.config(text=equation)

def clear():
    global equation
    equation = " "
    entry_result.config(text=0)

def calculate():
    global equation
    result = ""
    if equation != " ":
        try:
            result = eval(equation)
        except:
            result = "Error"
            equation = " "

        entry_result.config(text=result)


entry_result = Entry(root, text="", font=font, bg="#21618C", bd=12,
                     fg="#FBFCFC", relief=SUNKEN, width=26)
entry_result.grid(columnspan=5)
clear_result = Button(root, text="C", font=font, background="red", relief=SUNKEN,
                      fg="blue", height=2, width=2, command=lambda: clear())
clear_result.grid(row=1, column=1, sticky='w')
square = Button(root, text="x2", font=font, bg="#21618C", relief=SUNKEN,
                fg="blue", height=2, width=2, command=lambda: button_press("x2"))
square.grid(row=1, column=2, sticky='w')
cube = Button(root, text="x3", font=font, bg="red", relief=SUNKEN,
              fg="blue", height=2, width=2, command=lambda: button_press("x3"))
cube.grid(row=1, column=3, sticky='w')
division = Button(root, text="/", font=font, bg="red", relief=SUNKEN,
                  fg="blue", height=2, width=2, command=lambda: button_press("/"))
division.grid(row=1, column=4, sticky='w')
multiply = Button(root, text="*", font=font, bg="orange", relief=SUNKEN,
                  fg="blue",  height=2, width=2, command=lambda: button_press("*"))
multiply.grid(row=2, column=4, sticky='w')
num_9 = Button(root, text="9", font=font, bg="blue", relief=SUNKEN,
               fg="blue", height=2, width=2, command=lambda: button_press("9"))
num_9.grid(row=2, column=3, sticky='w')
num_8 = Button(root, text="8", font=font, bg="#21618C", relief=SUNKEN,
               fg="blue", height=2, width=2, command=lambda: button_press("8"))
num_8.grid(row=2, column=2, sticky='w')
num_7 = Button(root, text="7", font=font, bg="#21618C", relief=SUNKEN,
               fg="blue", height=2, width=2, command=lambda: button_press("7"))
num_7.grid(row=2, column=1, sticky='w')
num_4 = Button(root, text="4", font=font, bg="#21618C", relief=SUNKEN,
               fg="blue", height=2, width=2, command=lambda: button_press("4"))
num_4.grid(row=3, column=1, sticky='w')
num_5 = Button(root, text="5", font=font, bg="#21618C", relief=SUNKEN,
               fg="blue", height=2, width=2, command=lambda: button_press("5"))
num_5.grid(row=3, column=2, sticky='w')
num_6 = Button(root, text="6", font=font, bg="#21618C", relief=SUNKEN,
               fg="blue", height=2, width=2, command=lambda: button_press("6"))
num_6.grid(row=3, column=3, sticky='w')
plus = Button(root, text="+", font=font, bg="#21618C", relief=SUNKEN,
              fg="blue", height=2, width=2, command=lambda: button_press("+"))
plus.grid(row=3, column=4, sticky='w')
num_1 = Button(root, text="1", font=font, bg="#21618C", relief=SUNKEN,
               fg="blue", height=2, width=2, command=lambda: button_press("1"))
num_1.grid(row=4, column=1, sticky='w')
num_2 = Button(root, text="2", font=font, bg="#21618C", relief=SUNKEN,
               fg="blue", height=2, width=2, command=lambda: button_press("2"))
num_2.grid(row=4, column=2, sticky='w')
num_3 = Button(root, text="3", font=font, bg="#21618C", relief=SUNKEN,
               fg="blue", height=2, width=2, command=lambda: button_press("3"))
num_3.grid(row=4, column=3, sticky='w')
minus = Button(root, text="-", font=font, bg="#21618C", relief=SUNKEN,
               fg="blue", height=2, width=2, command=lambda: button_press("-"))
minus.grid(row=4, column=4, sticky='w')
zero = Button(root, text="0", font=font, bg="#21618C", relief=SUNKEN,
              fg="blue", height=2, width=2, command=lambda: button_press("0"))
zero.grid(row=5, column=1, sticky='w')
equal_to = Button(root, text="=", font=font, bg="#21618C", relief=SUNKEN,
                  fg="blue", height=2, width=2, command=lambda: calculate())
equal_to.grid(row=5, column=4, sticky='w')
point = Button(root, text=".", font=font, bg="#21618C", relief=SUNKEN,
               fg="blue", height=2, width=2, command=lambda: button_press("."))
point.grid(row=5, column=2, sticky='w')
log_value = Button(root, text="log10", font=font, bg="#21618C", relief=SUNKEN,
                   fg="blue", height=2, width=2, bd=5, command=lambda: button_press("log10"))
log_value.grid(row=5, column=3, sticky='w')


root.mainloop()

