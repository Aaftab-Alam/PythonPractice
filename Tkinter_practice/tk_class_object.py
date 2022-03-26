from tkinter import *

class GUI(Tk):
	def __init__(self):
		super().__init__()
		width=self.winfo_screenwidth()
		height=self.winfo_screenheight()
		self.geometry(f"{width-50}x{height-90}")
		
	def status(self):
		self.var=StringVar()
		self.var.set("Ready")
		self.statusbar=Label(self,textvariable=self.var,anchor="w",relief=SUNKEN)
		self.statusbar.pack(side=BOTTOM,fill=X)
	
	def com(self):
		Label(text="You clicked on Button",anchor="w").pack(side=TOP,fill=X)
		
	def button(self):
		Button(text="Submit",command=self.com).pack(side=BOTTOM,pady=40,anchor="e",padx=60)	
		
if __name__=="__main__":
	window=GUI()
	window.status()
	window.button()
	window.mainloop()