from tkinter import Tk
from tkinter import PhotoImage
from tkinter import Entry
from tkinter import Button
from tkinter import END

w = Tk()
w.geometry ("500x500")
w.resizable (False, False)
w.title('Balculator')
i = PhotoImage (file="C:\\Users\\lenovo\\Desktop\\yahia\\icon.png")
w.iconphoto  (False, i)
w.configure (bg="black")

e = Entry(w, bd=6, font=700, fg="#00ff1f", bg="gray", width=54)

def numad(number):
    current = e.get()
    e.delete( 0, END)
    e.insert( 0, str(current) + str(number))

def clearscreen():
    e.delete(0, END)

def plu():
    f_n = e.get()
    global first_num
    first_num = int(f_n)
    e.delete(0, END)

def eql():
    s_n = e.get()
    e.delete (0, END)
    e.insert(0, first_num + int(s_n))

    
on=Button(w, text="1",height=5,width=10
          ,font=170, bg="#14151a",fg="white",command=lambda: numad(1))

tw=Button(w, text="2",height=5, width=10
          ,font=170,bg="#14151a",fg="white",command=lambda: numad(2))

tr=Button(w, text="3",height=5, width=10,
          font=170,bg="#14151a",fg="white",command=lambda: numad(3))

fr=Button(w, text="4",height=5, width=10
          ,font=170,bg="#14151a",fg="white",command=lambda: numad(4))

fv=Button(w, text="5",height=5, width=10
          ,font=170, bg="#14151a",fg="white",command=lambda: numad(5))

sx=Button(w, text="6",height=5, width=10
          ,font=170,bg="#14151a",fg="white",command=lambda: numad(6))

sv=Button(w, text="7",height=5, width=10
          ,font=170,bg="#14151a",fg="white",command=lambda: numad(7))

et=Button(w, text="8",height=5, width=10,
          font=170,bg="#14151a",fg="white",command=lambda: numad(8))

nn=Button(w, text="9",height=5, width=10
          ,font=170, bg="#14151a",fg="white",command=lambda: numad(9))

zr=Button(w, text="0",height=2, width=4
          ,font=70,bg="#14151a",fg="white",command=lambda: numad(0))

p=Button(w, text="+",height=2, width=4
         ,font=70, bg="#14151a",fg="white",command=plu)

q=Button(w, text="=",height=2, width=4,font=70
         , bg="#14151a",fg="white",command=eql )

cls=Button(w, text="CS",height=2, width=4
           ,font=70,bg="#14151a",fg="sky blue",command=clearscreen)

on.grid(row=1,column=1)
tw.grid(row=1,column=48)
tr.grid(row=1,column=98)
fr.grid(row=4,column=1)
fv.grid(row=4,column=48)
sx.grid(row=4,column=98)
sv.grid(row=7,column=1)
et.grid(row=7,column=48)
nn.grid(row=7,column=98)
zr.grid(row=30,column=1)
p.grid(row=30,column=28)
q.grid(row=30,column=68)
cls.grid(row=30,column=98)
e.grid(row=0,column=0, columnspan=100,rowspan=1)


w.mainloop()
     
