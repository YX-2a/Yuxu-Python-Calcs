from tkinter import Tk, Button, PhotoImage, Entry, Label, Frame

##The Window Configuration##

w= Tk()
w.title ("Squarin' 'n Rootin' ")
w.geometry ("300x200")
w.resizable (False, False)
i = PhotoImage (file="icon.png")
w.iconphoto (False , i)
w.config (bg="#ff0000")

##important vars
psqrt = PhotoImage (file="sqrt.png")
psq = PhotoImage (file="sq.png")

##The Functions##

def sqrt ():
    sqrtip =  ip.get()
    calc = "=" , (float(sqrtip)**0.5)
    dpy = lbip.config (text=calc)


def sq ():
    sqrtip =  ipq.get()
    calc = "=" , float (sqrtip) * float (sqrtip)
    dpy = lbipq.config (text=calc)

##The Interface##

sqrte = Frame (w, bg = "#ff0000")
sqre = Frame (w, bg = "#ff0000")

ip = Entry (sqrte, width=25, font=40, justify="center",fg="#009900",bg="#909090")

lbip = Label (w, text= "=",fg="#ffaaff",bg="red", font= "bold")

btnip = Button (sqrte, image = psqrt, command=sqrt)

ipq = Entry (sqre, width=25, font=40, justify="center",fg="#009900",bg="#909090")

lbipq = Label (w, text= "=",fg="#ffaaff",bg="red", font= "bold")

btnipq = Button (sqre, image = psq, command=sq)

sqrte.pack (side="top", padx = 5, pady = 5)
lbip.pack (side="top", padx = 5, pady = 5)
sqre.pack (side="top", padx = 5, pady = 5)
lbipq.pack (side="top", padx = 5, pady = 5)

btnip.pack(side="left", padx = 5, pady = 10)
ip.pack(side="left", padx = 5, pady = 10)

btnipq.pack(side="left", padx = 5, pady = 10)
ipq.pack(side="left", padx = 5, pady = 10)


##The End##

w.mainloop()
