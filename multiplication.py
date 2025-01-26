from tkinter import*
from tkinter.ttk import*

root = Tk()
root.title("Multiplication table")
root.geometry("500x500")

title = Label(root,text = "Multiplication table",font = ("Times",18,"bold"))
title.grid(row = 0,column = 1,pady = 25)
range_lbl = Label(root,text = "Please select the range: ",font = ("times",12,"bold"))
range_lbl.grid(row = 1,column = 0,padx = 10)
#combobox creation
num = IntVar()
numbers = Combobox(root,textvariable = num,width = 5,state = "readonly")
numbers["values"] = tuple(range(101))
numbers.grid(row = 2,column= 1)
root.mainloop()