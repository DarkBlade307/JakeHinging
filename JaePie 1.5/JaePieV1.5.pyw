f= open("styles\\buttononetext.txt", "r")
b1t = f.read()
f.close()
f= open("styles\\buttontwotext.txt", "r")
b2t = f.read()
f.close()
f= open("styles\\buttonthreetext.txt", "r")
b3t = f.read()
f.close()
f= open("styles\\buttononecolour.txt", "r")
b1c = f.read()
f.close()
f= open("styles\\buttontwocolour.txt", "r")
b2c = f.read()
f.close()
f= open("styles\\buttonthreecolour.txt", "r")
b3c = f.read()
f.close()
f= open("styles\\tc1.txt", "r")
t1c = f.read()
f.close()
f= open("styles\\tc2.txt", "r")
t2c = f.read()
f.close()
f= open("styles\\tc3.txt", "r")
t3c = f.read()
f.close()
#Imports
from tkinter import ttk
from tkinter import filedialog
import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import Menu
#Definitions
def refresh():
    f= open("styles\\buttononetext.txt", "r")
    b1t = f.read()
    f.close()
    f= open("styles\\buttontwotext.txt", "r")
    b2t = f.read()
    f.close()
    f= open("styles\\buttonthreetext.txt", "r")
    b3t = f.read()
    f.close()
    f= open("styles\\buttononecolour.txt", "r")
    b1c = f.read()
    f.close()
    f= open("styles\\buttontwocolour.txt", "r")
    b2c = f.read()
    f.close()
    f= open("styles\\buttonthreecolour.txt", "r")
    b3c = f.read()
    f.close()
    f= open("styles\\tc1.txt", "r")
    t1c = f.read()
    f.close()
    f= open("styles\\tc2.txt", "r")
    t2c = f.read()
    f.close()
    f= open("styles\\tc3.txt", "r")
    t3c = f.read()
    buttonone.configure(text= b1t)
    buttonone.configure(bg= b1c)
    buttonone.configure(fg= t1c)
    buttontwo.configure(text= b2t)
    buttontwo.configure(bg= b2c)
    buttontwo.configure(fg= t2c)
    buttonthree.configure(text= b3t)
    buttonthree.configure(bg= b3c)
    buttonthree.configure(fg= t3c)
def runone():
    f= open("importantfiles\\numberone.txt", "r")
    runner = f.read()
    f.close()
    os.startfile(runner)
def runtwo():
    f= open("importantfiles\\numbertwo.txt", "r")
    runner = f.read()
    f.close()
    os.startfile(runner)
def runthree():
    f= open("importantfiles\\numberthree.txt", "r")
    runner = f.read()
    f.close()
    os.startfile(runner)
def setone():
    one = assigner.get()
    onen = nicknamer.get()
    f= open("importantfiles\\numberone.txt", "w")
    f.write(one)
    f.close()
    f= open("styles\\buttononetext.txt", "w")
    f.write(onen)
    f.close()
    buttonone.configure(text= onen)
def settwo():
    two = assigner.get()
    twon = nicknamer.get()
    f= open("importantfiles\\numbertwo.txt", "w")
    f.write(two)
    f.close()
    f= open("styles\\buttontwotext.txt", "w")
    f.write(twon)
    f.close()
    buttontwo.configure(text= twon)
def setthree():
    three = assigner.get()
    threen = nicknamer.get()
    f= open("importantfiles\\numberthree.txt", "w")
    f.write(three)
    f.close()
    f= open("styles\\buttonthreetext.txt", "w")
    f.write(threen)
    f.close()
    buttonthree.configure(text= threen)
def customhub():
    os.startfile("programs\\JPSCs\\customhub.pyw")
window = Tk()
window.title("JaePie V1.0")
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Launcher")
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Button Assignment")
tab_control.pack(expand=1, fill="both")
buttonone = Button(tab1, text=b1t, bg=b1c, fg=t1c, command=runone, font="verdana")
buttontwo = Button(tab1, text=b2t, bg=b2c, fg=t2c, command=runtwo, font="verdana")
buttonthree = Button(tab1, text=b3t, bg=b3c, fg=t3c, command=runthree, font="verdana")
buttonfour = Button(tab2, text="Assign button one", bg="blue", fg=t1c, command=setone, font="verdana")
buttonfive = Button(tab2, text="Assign button two", bg="red", fg=t2c, command=settwo, font="verdana")
buttonsix = Button(tab2, text="Assign button three", bg="green", fg=t3c, command=setthree, font="verdana")
buttonone.grid(column=0, row=0)
buttontwo.grid(column=0, row=1)
buttonthree.grid(column=0, row=2)
buttonfour.grid(column=0, row=0)
buttonfive.grid(column=0, row=1)
buttonsix.grid(column=0, row=2)
assigner = Entry(tab2, width=20, font="verdana")
nicknamer = Entry(tab2, width=20, font="verdana")
assigner.grid(column=1, row=1)
elifeman = Label(tab2, text="File name:", font="verdana")
nickname = Label(tab2, text="Button nickname:", font="verdana")
elifeman.grid(column=1, row=0)
nickname.grid(column=1, row=2)
nicknamer.grid(column=1, row=3)
menu = Menu(window)
window.geometry("400x150")
refresher = Button(tab2, text="Refresh buttons", bg="black", fg="white", command=refresh)
refresher.grid(column=0, row=3)

new_item = Menu(menu, tearoff=0)
new_item.add_command(label="Customisation Hub", command=customhub)
menu.add_cascade(label="Customisation", menu=new_item)
window.config(menu=menu)
window.mainloop()

