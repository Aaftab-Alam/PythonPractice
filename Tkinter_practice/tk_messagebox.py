from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("1000x1000")

def info():
	tmsg.showinfo("Message","Your response was submitted successfully!")
	root.destroy()
	
Button(text="Submit",command=info).pack()
	
root.mainloop()


##-----All Commands-----##
"""
'askokcancel', 'askquestion', 'askretrycancel', 'askyesno', 'askyesnocancel', 'showerror', 'showinfo', 'showwarning'

"""