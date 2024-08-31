#imports
from tkinter import Tk, PhotoImage
from tkinter.ttk import Button, Label, Entry, Frame
from random import randrange

#window conf
w = Tk ()
w.title ("Random Number Generator")
w.geometry ("350x150")
i = PhotoImage (file="icon.png")
w.iconphoto  (False, i)
w.resizable (0,0)

#function
def gorgy ():
    x = int (ent1.get ())
    y = int (ent2.get())
    texinfo = randrange (x , y)

    lb3.config (text = texinfo)

#interface

frm = Frame (w)

lb1 = Label (frm, text = "Select Range : ")
lb2 = Label (frm, text = ", ")
lb3 = Label (w, text = "")

ent1 = Entry (frm, width = 10)
ent2 = Entry (frm, width = 10)

btn = Button (w, text = "Apply", command = gorgy)

frm.pack (side = "top", pady = 20)
lb1.pack  (side = "left", padx = 5)
ent1.pack(side = "left", padx = 5)
lb2.pack (side = "left", padx = 5)
ent2.pack (side = "left", padx = 5)
btn.pack  (side = "top")
lb3.pack  (side = "top")

#mainloop
w.mainloop ()
