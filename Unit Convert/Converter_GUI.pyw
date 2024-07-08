#imports
from tkinter import Tk, Frame, Menu, Entry, Label
from UConv import cmin, mft, kmmi

#winconf
w = Tk ()
w.title ("GUI Unit Converter")
w.geometry ("250x80")
w.resizable (0,0)
menu = Menu ()
w.config (menu = menu)

#functions
def ci ():
    lab.config (text = "Mode : Cm To Inch")
    val = float(en.get ())
    result = cmin (val, "cmtoinch")
    lab1.config (text = f"Output : {result} in")
    
def ic ():
    lab.config (text = "Mode : Inch To Cm")
    val = float(en.get ())
    result = cmin (val, "inchtocm")
    lab1.config (text = f"Output : {result} cm")
    
def mf ():
    lab.config (text = "Mode : M To Foot")
    val = float(en.get ())
    result = mft (val, "mtoft")
    lab1.config (text = f"Output : {result} ft")
    
def fm ():
    lab.config (text = "Mode : Foot To M")
    val = float(en.get ())
    result = mft (val, "fttom")
    lab1.config (text = f"Output : {result} m")
    
def km ():
    lab.config (text = "Mode : Km To Mile")
    val = float(en.get ())
    result = kmmi (val, "kmtomi")
    lab1.config (text = f"Output : {result} mi")
    
def mk ():
    lab.config (text = "Mode : Mile To Km")
    val = float(en.get ())
    result = kmmi (val, "mitokm")
    lab1.config (text = f"Output : {result} km")

#UI

#Menu Bar
mode_menu = Menu (menu, tearoff = 0)
menu.add_cascade (menu = mode_menu, label = "Mode")
mode_menu.add_radiobutton (label = "Cm To Inch", command = ci)
mode_menu.add_radiobutton (label = "Inch To Cm", command = ic)
mode_menu.add_radiobutton (label = "M To Feet", command = mf)
mode_menu.add_radiobutton (label = "Feet To M", command = fm)
mode_menu.add_radiobutton (label = "Km To Mile", command = km)
mode_menu.add_radiobutton (label = "Mile To Km", command = mk)

#body
lab = Label (w, text = "Mode :  None")
body = Frame (w)
en = Entry (body, font = "Helevetica, 15")
en.insert (0, "Insert Value As Number")
lab1 = Label (body , text = "Output : None")

#Placements
lab.pack (side = "top")
body.pack (side = "top")
en.pack (side = "top") 
lab1.pack (side = "top")

#mainloop
w.mainloop ()
