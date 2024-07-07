from tkinter import Tk
from tkinter import Entry
from tkinter import Button
from tkinter import Canvas
from tkinter import Label



w= Tk()
w.title ("Euclidean Division")
w.geometry ("300x500")
w.resizable (False,False)

def eq(e):
    re= inp.get()
    er= inp1.get()
    yu= int (float(re) / float(er) ) 
    fu= float(re) % float(er) 

    l.config (text=yu)
    l1.config (text=fu)

def eqe():
    re= inp.get()
    er= inp1.get()
    yu=  int (float(re) / float(er) ) 
    fu= float(re) % float(er)
    
    l.config (text=yu)
    l1.config (text=fu)
    
c= Canvas (w, height=500,width=300,bg="white")
c.place (x=0,y=0)

c1= c.create_line (150,0,150,500)
c2= c.create_line (150,135,300,135)

bt1= Button (c, text="Result",height=2
                ,width=10,bg="light gray"
                ,activebackground="gray"
                ,command= eqe )
bt1.place (x=110,y=460)

inp= Entry (w,width=13, font=100, justify="center")
inp.place (x=20,y=65)

inp1= Entry (w,width=13, font=100,justify="center")
inp1.place (x=170,y=65)

l= Label (c,font=500,bg="white",fg="black")
l.place (x=152,y=175)

l1= Label (c,font=50,bg="white",fg="red")
l1.place (x=62,y=175)

w.bind ("<Return>", eq)
w.mainloop()
