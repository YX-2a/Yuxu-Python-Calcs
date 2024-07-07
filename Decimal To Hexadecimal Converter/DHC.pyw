from tkinter import Tk, Entry, Button, Label, PhotoImage, END

w = Tk()
w.resizable (False, False)
w.title ("Hexadecimal translator")
i = PhotoImage (file="icon.png")
w.iconphoto  (False, i)

def butt():
    hec.config (state = "normal")
    hec.delete (0, END)
    tra= int ( dec.get () )
    hec.insert (0,"%X" % tra)
    hec.config (state = "disabled")
    
    

dec= Entry (w)
dec.grid(column=0,row=0)

for x in range (1, 9):
    space= Label (w)
    space.grid (column=x ,row=0)


hec= Entry (w,state = "disabled")
hec.grid(column=9,row=0)


spaced= Button (w, text="translate", command=butt)
spaced.grid (column=5,row=1)


w.mainloop()
