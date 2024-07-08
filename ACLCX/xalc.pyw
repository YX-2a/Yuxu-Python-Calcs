from tkinter import Tk, Canvas, Label, Entry, Button, NORMAL, DISABLED, END, PhotoImage

w = Tk()
w.geometry ("300x500")
w.title('ACalcX')
w.resizable(False, False)
i = PhotoImage (file="icon.png")
w.iconphoto  (False, i)
bge = PhotoImage (file="bg.png")

c = Canvas (w, height=500, width=300)
c.create_image(0,0,image = bge, anchor = "nw")
c.grid(row=0,column=0,columnspan=50,rowspan=100)
def plusi():
    n1= inp.get()
    n11=inp1.get()
    eq.config (state=NORMAL)
    eq.delete(0, END)
    eq.insert(0, float(n1) + float(n11))
    eq.config (state=DISABLED)

def plui():
    n1= inp.get()
    n11=inp1.get()
    eq.config (state=NORMAL)
    eq.delete(0, END)
    eq.insert(0, float(n1) - float(n11))
    eq.config (state=DISABLED)
def pusi():
    n1= inp.get()
    n11=inp1.get()
    eq.config (state=NORMAL)
    eq.delete(0, END)
    eq.insert(0, float(n1) * float(n11))
    eq.config (state=DISABLED)
    
def lusi():
    n1= inp.get()
    n11=inp1.get()
    eq.config (state=NORMAL)
    eq.delete(0, END)
    eq.insert(0, float(n1) / float(n11))
    eq.config (state=DISABLED)

def lui():
    eq.config (state=NORMAL)
    eq.delete(0, END)
    eq.config (state=DISABLED)

inp = Entry(w, width=50)
ps = Button(w,text="+", command=plusi)
ms = Button(w,text="-", command=plui)
my = Button(w,text="×", command=pusi)
ds = Button(w,text="÷", command=lusi)
cls = Button(w,text="clear", command=lui) 

ps.grid(row=2,column=0)
ms.grid(row=2,column=1)
my.grid(row=2,column=2)
ds.grid(row=2,column=3)
inp.grid(row=0,column=0,columnspan=100)
cls.grid(row=2,column=4)

inp1 = Entry(w, width=50)

inp1.grid(row=3,column=0,columnspan=100)

sep= Label (w, text="=")
eq = Entry(w,width=48,bd=5,state=DISABLED)

eq.grid(row=5,column=0, columnspan=100)
sep.grid(row=4,column=0)

w.mainloop()


