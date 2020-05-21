from tkinter import *

exp = ""


def press(num):
    global exp
    exp = exp + str(num)
    var.set(exp)


def equal():
    global exp
    try:
        total = str(eval(exp))
        exp=str(total)
        var.set(exp)
    except:
        var.set("error")


def clear():
    global exp
    exp = ""
    var.set(exp)


def back():
    global exp
    exp = exp[:-1]
    var.set(exp)


if __name__ == "__main__":
    root = Tk()
    root.geometry("255x390")
    root.minsize(255, 390)
    root.maxsize(255, 390)
    root.title("Calculator")
    root.config(bg="#eaf2e4")
    var = StringVar()
    entry_top = Entry(root, font=("Times", 18), textvariable=var)
    var.set("Enter data")
    entry_top.grid(row=0, column=0, columnspan=4, pady=5)

    btn_bro = Button(root, text="(", font=1, width=6, height=3, command=lambda: press("("), pady=1)
    btn_bro["bg"]="#fcfffa"
    btn_bro.grid(row=1, column=0)
    btn_brc = Button(root, text=")", font=1, width=6, height=3, command=lambda: press(")"), pady=1)
    btn_brc["bg"] = "#fcfffa"
    btn_brc.grid(row=1, column=1)
    btn_C = Button(root, text="C", font=1, width=6, height=3, command=lambda: clear(), pady=1)
    btn_C["bg"] = "#fcfffa"
    btn_C.grid(row=1, column=2)
    btn_Back = Button(root, text="<-", font=1, width=6, height=3, command=lambda: back(), pady=1)
    btn_Back["bg"] = "#fcfffa"
    btn_Back.grid(row=1, column=3)

    btn_7 = Button(root, text="7", font=1, height=3, width=6, command=lambda: press("7"))
    btn_7["bg"] = "#fcfffa"
    btn_7.grid(row=2, column=0)
    btn_8 = Button(root, text="8", font=1, width=6, height=3, command=lambda: press("8"))
    btn_8["bg"] = "#fcfffa"
    btn_8.grid(row=2, column=1)
    btn_9 = Button(root, text="9", font=1, width=6, height=3, command=lambda: press("9"))
    btn_9["bg"] = "#fcfffa"
    btn_9.grid(row=2, column=2)
    btn_Div = Button(root, text="/", font=1, width=6, height=3, command=lambda: press("/"))
    btn_Div["bg"] = "#fcfffa"
    btn_Div.grid(row=2, column=3)

    btn_4 = Button(root, text="4", font=1, width=6, height=3, command=lambda: press("4"))
    btn_4["bg"] = "#fcfffa"
    btn_4.grid(row=3, column=0)
    btn_5 = Button(root, text="5", font=1, width=6, height=3, command=lambda: press("5"))
    btn_5["bg"] = "#fcfffa"
    btn_5.grid(row=3, column=1)
    btn_6 = Button(root, text="6", font=1, width=6, height=3, command=lambda: press("6"))
    btn_6["bg"] = "#fcfffa"
    btn_6.grid(row=3, column=2)
    btn_Mul = Button(root, text="X", font=1, height=3, width=6, command=lambda: press("*"))
    btn_Mul["bg"] = "#fcfffa"
    btn_Mul.grid(row=3, column=3)

    btn_1 = Button(root, text="1", font=1, width=6, height=3, command=lambda: press("1"))
    btn_1["bg"] = "#fcfffa"
    btn_1.grid(row=4, column=0)
    btn_2 = Button(root, text="2", font=1, width=6, height=3, command=lambda: press("2"))
    btn_2["bg"] = "#fcfffa"
    btn_2.grid(row=4, column=1)
    btn_3 = Button(root, text="3", font=1, height=3, width=6, command=lambda: press("3"))
    btn_3["bg"] = "#fcfffa"
    btn_3.grid(row=4, column=2)
    btn_Sub = Button(root, text="-", font=1, width=6, height=3, command=lambda: press("-"))
    btn_Sub["bg"] = "#fcfffa"
    btn_Sub.grid(row=4, column=3)

    btn_Dec = Button(root, text=".", font=1, width=6, height=3, command=lambda: press("."))
    btn_Dec["bg"] = "#fcfffa"
    btn_Dec.grid(row=5, column=0)
    btn_0 = Button(root, text="0", font=1, width=6, height=3, command=lambda: press("0"))
    btn_0["bg"] = "#fcfffa"
    btn_0.grid(row=5, column=1)
    btn_Eql = Button(root, text="=", font=1, width=6, height=3, command=lambda: equal())
    btn_Eql["bg"] = "#c0ff96"
    btn_Eql.grid(row=5, column=2)
    btn_Add = Button(root, text="+", font=1, width=6, height=3, command=lambda: press("+"))
    btn_Add["bg"] = "#fcfffa"
    btn_Add.grid(row=5, column=3)

    root.mainloop()
