import tkinter
from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()
root.geometry("250x400+500+300")
root.resizable(0, 0)
root.title("Calculator")

data = StringVar()

l1 = Label(
    root,
    text="display",
    anchor=SE,
    font=("verdana", 20),
    background="#ffffff",
    fg="#000000",
    textvariable=data
)

l1.pack(expand=True, fill="both")

val = ""
A = 0
operator = ''


def c_clicked():
    global val
    global A
    global operator

    A = 0
    operator = ""
    val = ""

    data.set(val)


def add_clicked():
    global val
    global A
    global operator

    A = int(val)
    operator = "+"
    val = val + "+"

    data.set(val)


def sub_clicked():
    global val
    global A
    global operator

    A = int(val)
    operator = "-"
    val = val + "-"

    data.set(val)


def mul_clicked():
    global val
    global A
    global operator

    A = int(val)
    operator = "*"
    val = val + "*"

    data.set(val)


def div_clicked():
    global val
    global A
    global operator

    A = int(val)
    operator = "/"
    val = val + "/"

    data.set(val)


def result():
    global val
    global A
    global operator

    val2 = val

    if operator == "+":
        x = int(val2.split("+")[1])
        y = A + x
        data.set(y)
        val = str(y)

    elif operator == "-":
        x = int(val2.split("-")[1])
        y = A - x
        data.set(y)
        val = str(y)

    elif operator == "*":
        x = int(val2.split("*")[1])
        y = A * x
        data.set(y)
        val = str(y)

    elif operator == "/":
        x = int(val2.split("/")[1])

        if x == 0:
            messagebox.showerror("Error", "Division by 0 is not allowed")
            A = 0
            val = ""
            data.set(val)
        else:
            y = A / x
            data.set(y)
            val = str(y)



def btn1_is_clicked():
    global val
    val = val + "1"
    data.set(val)


def btn2_is_clicked():
    global val
    val = val + "2"
    data.set(val)


def btn3_is_clicked():
    global val
    val = val + "3"
    data.set(val)


def btn4_is_clicked():
    global val
    val = val + "4"
    data.set(val)


def btn5_is_clicked():
    global val
    val = val + "5"
    data.set(val)


def btn6_is_clicked():
    global val
    val = val + "6"
    data.set(val)


def btn7_is_clicked():
    global val
    val = val + "7"
    data.set(val)


def btn8_is_clicked():
    global val
    val = val + "8"
    data.set(val)


def btn9_is_clicked():
    global val
    val = val + "9"
    data.set(val)


def btn0_is_clicked():
    global val
    val = val + "0"
    data.set(val)


row1 = Frame(root, bg="#000000")
row1.pack(expand=True, fill="both")

row2 = Frame(root, bg="red")
row2.pack(expand=True, fill="both")

row3 = Frame(root, bg="green")
row3.pack(expand=True, fill="both")

row4 = Frame(root)
row4.pack(expand=True, fill="both")

btn1 = Button(
    row1,
    text='7',
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="black",
    fg="white",
    command=btn7_is_clicked
)

btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(
    row1,
    text="8",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="black",
    fg="white",
    command=btn8_is_clicked
)

btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(
    row1,
    text="9",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="black",
    fg="white",
    command=btn9_is_clicked
)

btn3.pack(side=LEFT, expand=True, fill="both")

btn_add = Button(
    row1,
    text="+",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="black",
    fg="white",
    command=add_clicked
)

btn_add.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(
    row2,
    text='4',
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="black",
    fg="white",
    command=btn4_is_clicked
)

btn4.pack(side=LEFT, expand=True, fill="both")

btn5 = Button(
    row2,
    text="5",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="black",
    fg="white",
    command=btn5_is_clicked
)

btn5.pack(side=LEFT, expand=True, fill="both")

btn6 = Button(
    row2,
    text="6",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="black",
    fg="white",
    command=btn6_is_clicked
)

btn6.pack(side=LEFT, expand=True, fill="both")

btn_sub = Button(
    row2,
    text="-",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="black",
    fg="white",
    command=sub_clicked
)

btn_sub.pack(side=LEFT, expand=True, fill="both")

btn7 = Button(
    row3,
    text='1',
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="black",
    fg="white",
    command=btn1_is_clicked
)

btn7.pack(side=LEFT, expand=True, fill="both")

btn8 = Button(
    row3,
    text="2",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="black",
    fg="white",
    command=btn2_is_clicked
)

btn8.pack(side=LEFT, expand=True, fill="both")

btn9 = Button(
    row3,
    text="3",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="black",
    fg="white",
    command=btn3_is_clicked
)

btn9.pack(side=LEFT, expand=True, fill="both")

btn_mul = Button(
    row3,
    text="*",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="black",
    fg="white",
    command=mul_clicked
)

btn_mul.pack(side=LEFT, expand=True, fill="both")

btn10 = Button(
    row4,
    text='C',
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="black",
    fg="white",
    command=c_clicked
)

btn10.pack(side=LEFT, expand=True, fill="both")

btn11 = Button(
    row4,
    text="0",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="black",
    fg="white",
    command=btn0_is_clicked
)

btn11.pack(side=LEFT, expand=True, fill="both")

btn12 = Button(
    row4,
    text="=",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="black",
    fg="white",
    command=result
)

btn12.pack(side=LEFT, expand=True, fill="both")

btn_div = Button(
    row4,
    text="/",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    bg="black",
    fg="white",
    command=div_clicked
)

btn_div.pack(side=LEFT, expand=True, fill="both")

root.mainloop()
