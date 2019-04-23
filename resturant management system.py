import tkinter
from tkinter import *
root = tkinter.Tk()
root.minsize(1000, 600)
root.maxsize(1000, 600)
root.title("Resturent management system")

f1 = LabelFrame(root, text="Food Items", width=800, height=500)
f1.grid(row=0, column=0)
f2 = LabelFrame(root, text="Action", width=200, height=500)
f2.grid(row=0, column=1)
f3 = Frame(root, width=1000, height=20, padx=20)
f3.grid(row=1, column=0, columnspan=2)

def button(t, r, c, bg="#8E24AA", master=f1, fg="white"):
    Button(master, text=t, bg=bg, command=lambda: total(t),fg=fg, font="arial 16 bold", width=17, height=5).grid(row=r, column=c, padx=12, pady=12)

def actionbtn(text, bg, command, r):
    Button(f2, text=text, bg=bg, font="arial 15 bold", fg="white", command=command, width=14, height=2).grid(row=r, column=0, pady=16, padx=25)

set = ""
string = ""

def total(food):
    global set
    global string
    if "Samosa"==food:
        price = 7
    elif "Chawmin"==food:
        price = 30
    elif "Breadpakora"==food:
        price = 10
    elif "Burger"==food:
        price = 30
    elif "Egg Roll"==food:
        price = 30
    elif "Idli"==food:
        price = 30
    elif "Dosa"==food:
        price = 50
    elif "Kachori"==food:
        price = 7
    else:
        price = 20
    set += str(price)+"+"
    string = food+" = "+str(price)+"/-\n"
    t.insert(END,string)

def final():
    global set
    global string
    set += "0"
    data = eval(set)
    string = "\nTotal Bill = "+str(data)+"/-"
    t.insert(END,string)

def clear():
    global set
    global string
    string = ""
    set = ""
    t.delete(0,END)

def view():
    pass

def setting():
    pass

button("Samosa", 0, 0)
button("Chawmin", 0, 1)
button("Burger", 0, 2)
button("Egg Roll", 1, 0)
button("Idli", 1, 1)
button("Dosa", 1, 2)
button("Kachori", 2, 0)
button("Breadpakora", 2, 1)
button("Chhat", 2, 2)

actionbtn("Total", "#673AB7", final, 0)
actionbtn("Clear", "#607D8B", clear, 1)
actionbtn("View", "#4CAF50", view, 2)
actionbtn("Quit", "#E53935", quit, 3)
actionbtn("Setting", "#FB8C00", setting, 4)
button("Breadpakora", 2, 1)
button("Chhat", 2, 2)

actionbtn("Total", "#673AB7", final, 0)
actionbtn("Clear", "#607D8B", clear, 1)
actionbtn("View", "#4CAF50", view, 2)

t = Listbox(f3, width=85, font="arial 14 bold")
t.pack()

root.mainloop()