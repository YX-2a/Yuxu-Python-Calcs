#imports
from tkinter import Tk, Button, Label, Entry, PhotoImage
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
lb1 = Label (w, text = "Select Range : ")
lb2 = Label (w, text = ", ")
lb3 = Label (w, text = "", fg = "#ff0000")

ent1 = Entry (w, width = 10)
ent2 = Entry (w, width = 10)

btn = Button (w, text = "Apply", command = gorgy)

lb1.place  (x = 50,y = 25)
ent1.place(x = 135,y = 25)
lb2.place  (x = 210,y = 25)
ent2.place(x = 230,y = 25)
btn.place  (x = 195 ,y = 60)
lb3.place  (x = 195,y = 95)

#mainloop
w.mainloop ()
