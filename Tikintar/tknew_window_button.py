from tkinter import *
root=Tk()
root.geometry("1000x700")

def func():
	root1=Tk()
	root1.geometry("500x350")
	root1.title("New window")
	root.destroy()
	
	
f1=Frame(root,bg="grey")
f1.pack(side=BOTTOM,fill=X)

b1=Button(f1, text="New window", borderwidth=5, relief=SUNKEN,pady=0 ,command=func)
b1.pack(pady=30,side=RIGHT,padx=30)
root.mainloop()