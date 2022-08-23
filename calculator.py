from tkinter import *
root = Tk()
root.resizable(0, 0)
root.title("Calculator")


operation = ""


def equals():
    # now we know what is second number
    # we separated second number from first number
    # so now you only need to calculate and define "def equals():"
    global second_num
    secondNum_plus_firstNum = Calculator_box.get()

    if operation == "+":
        toBeDeletedto = secondNum_plus_firstNum.find("+") + 1
        firstnum_and_plus = secondNum_plus_firstNum[0:toBeDeletedto]
        second_num = secondNum_plus_firstNum.replace(firstnum_and_plus, "")
        answer = float(first_num) + float(second_num)
        Calculator_box.delete(0, END)
        Calculator_box.insert(0, str(answer))
    if operation == "-":
        toBeDeletedto = secondNum_plus_firstNum.find("-") + 1
        firstnum_and_plus = secondNum_plus_firstNum[0:toBeDeletedto]
        second_num = secondNum_plus_firstNum.replace(firstnum_and_plus, "")
        answer = float(first_num) - float(second_num)
        answer = str(answer)
        Calculator_box.delete(0, END)
        Calculator_box.insert(0, answer)
    if operation == "X":
        toBeDeletedto = secondNum_plus_firstNum.find("X") + 1
        firstnum_and_plus = secondNum_plus_firstNum[0:toBeDeletedto]
        second_num = secondNum_plus_firstNum.replace(firstnum_and_plus, "")
        answer = float(first_num) * float(second_num)
        Calculator_box.delete(0, END)
        Calculator_box.insert(0, str(answer))
    if operation == "/":
        toBeDeletedto = secondNum_plus_firstNum.find("/") + 1
        firstnum_and_plus = secondNum_plus_firstNum[0:toBeDeletedto]
        second_num = secondNum_plus_firstNum.replace(firstnum_and_plus, "")
        answer = float(first_num) / float(second_num)
        Calculator_box.delete(0, END)
        Calculator_box.insert(0, str(answer))


def operation_signs(sign):
    global first_num
    global operation
    if sign == "+":
        first_num = Calculator_box.get()
        Calculator_box.insert(END, "+")
        operation = "+"
    elif sign == "-":
        first_num = Calculator_box.get()
        Calculator_box.insert(END, "-")
        operation = "-"
    elif sign == "X":
        first_num = Calculator_box.get()
        Calculator_box.insert(END, "X")
        operation = "X"
    elif sign == "/":
        first_num = Calculator_box.get()
        Calculator_box.insert(END, "/")
        operation = "/"


def enter_num(num):
    number = str(Calculator_box.get()) + str(num)
    Calculator_box.delete(0, END)
    Calculator_box.insert(0, number)


def clear_box():
    Calculator_box.delete(0, END)


Calculator_box = Entry(root, width=38, borderwidth=5)
Calculator_box.grid(row=0, column=0, columnspan=4)
# underneath there are 4 columns

button_7 = Button(root, text="7", command=lambda: enter_num(7), width=7, height=2).grid(
    row=1, column=0)
button_4 = Button(root, text="4", command=lambda: enter_num(4), width=7, height=2).grid(
    row=2, column=0)
button_1 = Button(root, text="1", command=lambda: enter_num(1), width=7, height=2).grid(
    row=3, column=0)

button_8 = Button(root, text="8", command=lambda: enter_num(8), width=7, height=2).grid(
    row=1, column=1)
button_5 = Button(root, text="5", command=lambda: enter_num(5), width=7, height=2).grid(
    row=2, column=1)
button_2 = Button(root, text="2", command=lambda: enter_num(2), width=7, height=2).grid(
    row=3, column=1)
button_0 = Button(root, text="0", command=lambda: enter_num(0), width=7, height=2).grid(
    row=4, column=1)

button_9 = Button(root, text="9", command=lambda: enter_num(9), width=7, height=2).grid(
    row=1, column=2)
button_6 = Button(root, text="6", command=lambda: enter_num(6), width=7, height=2).grid(
    row=2, column=2)
button_3 = Button(root, text="3", command=lambda: enter_num(3), width=7, height=2).grid(
    row=3, column=2)

button_plus = Button(root, text="+", width=7, height=2, command=lambda: operation_signs("+")
                     ).grid(row=1, column=3)
button_minus = Button(root, text="-", width=7, height=2,
                      command=lambda: operation_signs("-")).grid(row=2, column=3)
button_multipy = Button(root, text="X", width=7,
                        height=2, command=lambda: operation_signs("X")).grid(row=3, column=3)
button_divide = Button(root, text="/", width=7,
                       height=2, command=lambda: operation_signs("/")).grid(row=4, column=3)
button_equals = Button(root, text="=", width=7,
                       height=2, command=equals).grid(row=4, column=2)
button_clear = Button(root, text="clear", width=7,
                      height=2, command=clear_box).grid(row=4, column=0)
root.mainloop()
