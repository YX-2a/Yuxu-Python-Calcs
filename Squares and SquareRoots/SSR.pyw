from tkinter import Tk, Button, PhotoImage, Entry, Label, Canvas

##The Window Configuration##

w= Tk()
w.title ("Squarin' 'n Rootin' ")
w.geometry ("300x200")
w.resizable (False, False)
i = PhotoImage (file="icon.png")
w.iconphoto (False , i)

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

can= Canvas (w, height=200,width=300, bg="red")
can.place(x=0,y=0)

ip = Entry (can, width=25, font=40, justify="center",fg="#009900",bg="#909090")
ip.place(x=50,y=50)

lbip = Label (can, text= "=",fg="#ffaaff",bg="red", font= "bold")
lbip.place (x=45,y=75)

btnip = Button (can, image = psqrt, command=sqrt)
btnip.place (x=10,y=50)

ipq = Entry (can, width=25, font=40, justify="center",fg="#009900",bg="#909090")
ipq.place(x=50,y=100)

lbipq = Label (can, text= "=",fg="#ffaaff",bg="red", font= "bold")
lbipq.place (x=45,y=125)

btnipq = Button (can, image = psq, command=sq)
btnipq.place (x=10,y=100)


##The End##

w.mainloop()
