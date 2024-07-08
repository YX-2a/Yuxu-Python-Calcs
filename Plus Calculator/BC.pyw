from tkinter import Tk, PhotoImage, Entry, Button, END

w = Tk()
w.geometry ("500x500")
w.resizable (False, False)
w.title('Plus Calculator')
i = PhotoImage (file="icon.png")
w.iconphoto  (False, i)
w.config (bg="black")

e = Entry(w, bd=6, font=700, fg="#00ff1f", bg="gray", width=54)
nums = []

def numad(number):
    global var
    current = e.get()
    e.delete( 0, END)
    var = str(current) + str(number)
    e.insert( 0, var)

def clearscreen():
    e.delete(0, END)
    nums.clear ()

def plu():
    e.delete(0, END)
    nums.append (var)
    
def eql():
    nums.append (var)
    res = eval ("+".join (nums))
    e.delete (0, END)
    e.insert(0, res)

    
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
     
