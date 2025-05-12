from tkinter import Tk, Label, Frame, PhotoImage
from tkinter.ttk import Entry, Button
from time import sleep

def count ():
	mini_num = float (ent.get ())
	step_num = float (ent3.get())
	maxi_num = float (ent2.get ())
	
	while mini_num <= maxi_num :
		w.update ()
		sleep (0.01)
		lb3.config (text = str(mini_num))
		mini_num += step_num
	
	for _ in range(15) :
		w.update ()
		sleep (0.5)
		lb3.config (fg = "#ff0000")
	
		w.update ()
		sleep (0.5)
		lb3.config (fg = "#000000")
		
def main ():
	global ent, ent2,ent3, lb3, w
	w = Tk ()
	w.title ("Counter GUI")
	i = PhotoImage (file="icon.png")
	w.iconphoto  (False, i)
	w.resizable (0,0)
	
	frm = Frame (w)
	frm2 = Frame (w)
	frm3 = Frame (w)
	
	lb = Label (frm, text = "Minimum Number :")
	ent = Entry (frm)
	
	lb4 = Label (frm3, text = "Step Number :")
	ent3 = Entry (frm3)
	
	lb2 = Label (frm2, text = "Maximum Number :")
	ent2 = Entry (frm2)
	
	lb3 = Label (w, text = "")
	btn = Button (w, text = "Submit", command = count )
	
	frm.pack (side = "top", pady = 10, padx = 10)
	frm3.pack (side = "top", pady = 10, padx = 10)
	frm2.pack (side = "top", pady = 10, padx = 10)
	lb.pack (side = "left")
	ent.pack (side = "left")
	lb4.pack (side = "left", pady = 12, padx = 12)
	ent3.pack (side = "left", pady = 12, padx = 12)
	lb2.pack (side = "left")
	ent2.pack (side = "left")
	btn.pack (side = "top", pady = 10)
	lb3.pack (side = "top", pady = 10)
	
	w.mainloop ()

if __name__ == "__main__" :
	main ()
	