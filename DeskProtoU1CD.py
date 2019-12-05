#IMPORTS

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk,Image

#DEFINE FUNCTIONS

#SUBMITTING TASKS

def mysubmit(event):
    if (e1.get() == ""):
        print("ERROR: Field not filled out")
    if (e2.get() == ""):
        print("ERROR: Field not filled out")
    if (e3.get() == ""):
        print("ERROR: Field not filled out")
    else:
        global mytasks
        count = 0
        mytasks.append([e1.get(),e2.get(),e3.get()])
        for l in mytasks: 
            imgframe1 = Frame(win,borderwidth = 1.5, relief=RAISED, width=300,height=30)
            imgframe1.grid(row=count,column=2)
            b2 = Button(imgframe1,text="Delete Task",command=lambda l=l: deletetask(l))
            b2.grid(row=count,column=3)
            widgetlist.append(b2)
            lwindow1 = Label(imgframe1,text=l[0] + ", " + l[1] + ", " + l[2])
            lwindow1.grid(row=count,column=2)
            lwindow1.config(fg="blue")
            widgetlist.append(lwindow1)
            widgetlist.append(imgframe1)
            count = count + 1
        

def submit():
    if (e1.get() == ""):
        print("ERROR: Field not filled out")
    if (e2.get() == ""):
        print("ERROR: Field not filled out")
    if (e3.get() == ""):
        print("ERROR: Field not filled out")
    else:
        global mytasks
        count = 0
        mytasks.append([e1.get(),e2.get(),e3.get()])
        for l in mytasks: 
            imgframe1 = Frame(win,borderwidth = 1.5, relief=RAISED, width=300,height=30)
            imgframe1.grid(row=count,column=2)
            b2 = Button(imgframe1,text="Delete Task",command=lambda l=l: deletetask(l))
            b2.grid(row=count,column=3)
            widgetlist.append(b2)
            lwindow1 = Label(imgframe1,text=l[0] + ", " + l[1] + ", " + l[2])
            lwindow1.grid(row=count,column=2)
            lwindow1.config(fg="blue")
            widgetlist.append(lwindow1)
            widgetlist.append(imgframe1)
            count = count + 1


def redraw():
    for widget in widgetlist:
        widget.destroy()


#DELETING TASKS
       
def deletetask(data):
    global mytasks
    mytasks.remove(data)
    redraw()
    
#MAIN INTERFACE

mytasks = []

widgetlist = []

win = Tk()
win.title("Example Taskbar Prototype")
win.geometry("650x350")

l1 = Label(win,text="Enter Task")
l1.grid(row=0,column=0)

e1 = Entry(win)
e1.grid(row=0,column=1)
e1.bind('<Return>', mysubmit)

l2 = Label(win,text="Set Priority Level")
l2.grid(row=1,column=0)

e2 = Entry(win)
e2.grid(row=1,column=1)
e2.bind('<Return>', mysubmit)

l3 = Label(win,text="Set Date")
l3.grid(row=2,column=0)

e3 = Entry(win)
e3.grid(row=2,column=1)
e3.bind('<Return>', mysubmit)

b1 = Button(win,text="Submit",command=submit)
b1.grid(row=3,column=1)
