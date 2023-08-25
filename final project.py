from tkinter import *
import math
root = Tk()
root.title("calculator")
root.geometry("680x356+100+100")
root.config(bg="black")
font = ("Arial black", 15)
# FUNCTIONAL PART:-


def calculate():
    ex = entry_result.get()
    try:
        result = eval(ex)
        ans = round(result, 1)
        entry_result.delete(0, END)
        entry_result.insert(0, ans)

    except ZeroDivisionError:
        entry_result.delete(0, END)
        entry_result.insert(0, 'ZeroDivisionError')


def button_press(value):
    ex = entry_result.get()
    if value == "x2":
        ans = eval(ex) ** 2

    elif value == "x3":
        ans = eval(ex) ** 3

    elif value == "log10":
        ans = math.log10(eval(ex))

    elif value == "√":
        ans = math.sqrt(eval(ex))

    elif value == "∛":
        ans = math.cbrt(eval(ex))

    elif value == "𝞹":
        ans = math.pi

    elif value == "ln":
        ans = math.log2(eval(ex))

    elif value == "e":
        ans = math.e

    else:
        entry_result.insert(END, value)
        return
    entry_result.delete(0, END)
    entry_result.insert(0, ans)


def clear():
    entry_result.delete(0, END)


# GUI part
entry_result = Entry(root, font=font, bg="#21618C", bd=12,
                     fg="#FBFCFC", relief=SUNKEN, width=58)
entry_result.grid(row=0, column=0, columnspan=5)
clear_result = Button(root, text="C", font=font, bg="white", relief=GROOVE,
                      fg="blue", height=2, width=1, command=lambda: clear())
clear_result.grid(row=1, column=0, sticky="news")
square = Button(root, text="x2", font=font, bg="white", relief=SUNKEN,
                fg="blue", height=2, width=1, command=lambda: button_press("x2"))
square.grid(row=1, column=1, sticky="news")
cube = Button(root, text="x3", font=font, bg="white", relief=SUNKEN,
              fg="blue", height=2, width=1, command=lambda: button_press("x3"))
cube.grid(row=1, column=2, sticky="news")
square_root = Button(root, text="√", font=font, bg="white", relief=SUNKEN,
                     fg="blue", height=2, width=1, command=lambda: button_press("√"))
square_root.grid(row=1, column=3, sticky="news")
division = Button(root, text="/", font=font, bg="white", relief=SUNKEN,
                  fg="blue", height=2, width=1, command=lambda: button_press("/"))
division.grid(row=1, column=4, sticky="news")
multiply = Button(root, text="*", font=font, bg="white", relief=SUNKEN,
                  fg="blue",  height=2, width=1, command=lambda: button_press("*"))
multiply.grid(row=2, column=4, sticky="news")
cube_root = Button(root, text="∛", font=font, bg="white", relief=SUNKEN,
                   fg="blue",  height=2, width=1, command=lambda: button_press("∛"))
cube_root.grid(row=2, column=3, sticky="news")
num_9 = Button(root, text="9", font=font, bg="white", relief=SUNKEN,
               fg="blue", height=2, width=1, command=lambda: button_press("9"))
num_9.grid(row=2, column=2, sticky="news")
num_8 = Button(root, text="8", font=font, bg="white", relief=SUNKEN,
               fg="blue", height=2, width=1, command=lambda: button_press("8"))
num_8.grid(row=2, column=1, sticky="news")
num_7 = Button(root, text="7", font=font, bg="white", relief=SUNKEN,
               fg="blue", height=2, width=1, command=lambda: button_press("7"))
num_7.grid(row=2, column=0, sticky="news")
num_4 = Button(root, text="4", font=font, bg="white", relief=SUNKEN,
               fg="blue", height=2, width=1, command=lambda: button_press("4"))
num_4.grid(row=3, column=0, sticky="news")
num_5 = Button(root, text="5", font=font, bg="white", relief=SUNKEN,
               fg="blue", height=2, width=1, command=lambda: button_press("5"))
num_5.grid(row=3, column=1, sticky="news")
num_6 = Button(root, text="6", font=font, bg="white", relief=SUNKEN,
               fg="blue", height=2, width=1, command=lambda: button_press("6"))
num_6.grid(row=3, column=2, sticky="news")
pie_val = Button(root, text="𝞹", font=font, bg="white", relief=SUNKEN,
                 fg="blue", height=2, width=1, command=lambda: button_press("𝞹"))
pie_val.grid(row=3, column=3, sticky="news")
plus = Button(root, text="+", font=font, bg="white", relief=SUNKEN,
              fg="blue", height=2, width=1, command=lambda: button_press("+"))
plus.grid(row=3, column=4, sticky="news")
num_1 = Button(root, text="1", font=font, bg="white", relief=SUNKEN,
               fg="blue", height=2, width=1, command=lambda: button_press("1"))
num_1.grid(row=4, column=0, sticky="news")
num_2 = Button(root, text="2", font=font, bg="white", relief=SUNKEN,
               fg="blue", height=2, width=1, command=lambda: button_press("2"))
num_2.grid(row=4, column=1, sticky="news")
num_3 = Button(root, text="3", font=font, bg="white", relief=SUNKEN,
               fg="blue", height=2, width=1, command=lambda: button_press("3"))
num_3.grid(row=4, column=2, sticky="news")
ln_value = Button(root, text="ln", font=font, bg="white", relief=SUNKEN,
                  fg="blue", height=2, width=1, command=lambda: button_press("ln"))
ln_value.grid(row=4, column=3, sticky="news")
minus = Button(root, text="-", font=font, bg="white", relief=SUNKEN,
               fg="blue", height=2, width=1, command=lambda: button_press("-"))
minus.grid(row=4, column=4, sticky="news")
zero = Button(root, text="0", font=font, bg="white", relief=SUNKEN,
              fg="blue", height=2, width=1, command=lambda: button_press("0"))
zero.grid(row=5, column=0, sticky="news")
point = Button(root, text=".", font=font, bg="white", relief=SUNKEN,
               fg="blue", height=2, width=1, command=lambda: button_press("."))
point.grid(row=5, column=1, sticky="news")
log_value = Button(root, text="log10", font=("Arial black", 12), bg="white", relief=SUNKEN,
                   fg="blue", height=2, width=1, command=lambda: button_press("log10"))
log_value.grid(row=5, column=2, sticky="news")
e_value = Button(root, text="e", font=font, bg="white", relief=SUNKEN,
                 fg="blue", height=2, width=1, command=lambda: button_press("e"))
e_value.grid(row=5, column=3, sticky="news")
equal_to = Button(root, text="=", font=font, bg="white", relief=SUNKEN,
                  fg="blue", height=2, width=1, command=lambda: calculate())
equal_to.grid(row=5, column=4, sticky="news")
root.mainloop()
