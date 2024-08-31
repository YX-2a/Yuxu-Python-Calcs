#imports
from tkinter import Tk, PhotoImage
from tkinter.ttk import Entry, Label, Button
from gcd import GCD

#other funcs
def g_c_d ():
    num1 = float (ent.get()) 
    num2 = float (ent1.get()) 

    res = GCD (num1, num2)
    lb1.config (text = "Result : " + str(res))
    
#main func
def main ():
    global ent, ent1, lb1
    #winconf
    w = Tk ()
    w.title ("GCD GUI")
    w.geometry ("250x150")
    i = PhotoImage (file="icon.png")
    w.iconphoto  (False, i)
    w.resizable (0,0)

    #UI
    ent = Entry (w)
    ent1 = Entry (w)
    lb = Label (w, text = "/")
    lb1 = Label (w, text = "Result : None")
    btn = Button (w, text = "Submit", command = g_c_d)

    #placement
    ent.pack (pady = 1 )
    lb.pack (pady = 1 )
    ent1.pack (pady = 1 )
    btn.pack(pady = 2 )
    lb1.pack (pady = 2)

    w.mainloop ()

if __name__ == "__main__" :
    main ()
