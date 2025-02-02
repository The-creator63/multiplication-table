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

#radiobutton creation
endval = IntVar()
r10 = Radiobutton(root,text = "10",variable = endval,value = 10)
r20 = Radiobutton(root,text = "20",variable = endval,value = 20)
r30 = Radiobutton(root,text = "30",variable = endval,value = 30)
endval.set(10)

r10.grid(row = 4,column = 2)
r20.grid(row = 5,column = 2)
r30.grid(row = 6,column = 2)

def multtable():
    tables = ""
    for i in range(1,endval.get() + 1):
        multiply = num.get()*i
        tables += str(num.get()) + " X " + str(i) + " = " + str(multiply) + "\n"
root.mainloop()