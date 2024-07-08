#imports
from tkinter import Tk, Canvas, Label, Entry, Button, PhotoImage
from random import randrange

#winconf
w = Tk()
w.title ("Linear Function Drawer")
w.resizable (False, False)
i = PhotoImage (file="icon.png")
w.iconphoto (False , i)

#functions
def makeline ():
    X = 650
    p = float(en1.get())
    d = float(en2.get())

    yb = X*p+d

    colorstrr = randrange (20, 255)
    colorstrg = randrange (20, 255)
    colorstrb = randrange (20, 255)
    
    colorrand = "#{:02x}{:02x}{:02x}".format (colorstrr,colorstrg,colorstrb)

    can.create_line (X-650,400-d,X,400-yb,fill = colorrand)

#UI
lab1 = Label (w, text = "400")
lab1.pack(anchor = "nw")

can = Canvas (w, height = 400, width =650 , bg="#000000")
can.pack (anchor = "n")

lab = Label (w, text = "0" + " "*222 + "650")
lab.pack(anchor = "sw")

lab3 = Label (w, text = "x axis :")
lab3.pack(anchor = "w")

en = Entry (w)
en.insert (0, "650")
en.config (state = "disabled")
en.pack (anchor = "w")

lab5 = Label (w, text = "y axis :")
lab5.pack(anchor = "w")

en0 = Entry (w)
en0.insert (0, "400")
en0.config (state = "disabled")
en0.pack (anchor = "w")

lab4 = Label (w, text = "Enter multiplier :")
lab4.pack(anchor = "w")

en1 = Entry (w)
en1.insert (0, "0")
en1.pack (anchor = "w")

lab5 = Label (w, text = "Enter adder :")
lab5.pack(anchor = "w")

en2 = Entry (w)
en2.insert (0, "0")
en2.pack (anchor = "w")

btn = Button (w, text = "Enter", command = makeline)
btn.pack (anchor = "w")


#ml
w.mainloop()

