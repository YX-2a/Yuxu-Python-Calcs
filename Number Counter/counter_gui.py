from tkinter import Tk, Label, Entry, Button, Frame
from time import sleep

def count ():
	mini_num = int (ent.get ())
	maxi_num = int (ent2.get ())
	
	while mini_num <= maxi_num :
		w.update ()
		sleep (0.01)
		lb3.config (text = str(mini_num))
		mini_num += 1
	
	for _ in range(15) :
		w.update ()
		sleep (0.5)
		lb3.config (fg = "#ff0000")
	
		w.update ()
		sleep (0.5)
		lb3.config (fg = "#000000")
		
def main ():
	global ent, ent2, lb3, w
	w = Tk ()
	w.title ("Counter GUI")
	w.resizable (0,0)
	
	frm = Frame (w)
	frm2 = Frame (w)
	lb = Label (frm, text = "Minimum Number :")
	ent = Entry (frm)
	lb2 = Label (frm2, text = "Maximum Number :")
	ent2 = Entry (frm2)
	lb3 = Label (w, text = "")
	btn = Button (w, text = "Submit", command = count )
	
	frm.pack (side = "top", pady = 10, padx = 10)
	frm2.pack (side = "top", pady = 10, padx = 10)
	lb.pack (side = "left")
	ent.pack (side = "left")
	lb2.pack (side = "left")
	ent2.pack (side = "left")
	btn.pack (side = "top", pady = 10)
	lb3.pack (side = "top", pady = 10)
	
	w.mainloop ()

if __name__ == "__main__" :
	main ()
	