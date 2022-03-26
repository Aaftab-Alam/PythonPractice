from tkinter import *
root=Tk()
root.geometry("1000x1000")
def order():
	Label(root,text=f"You ordered {items[var.get()]}").pack(anchor="w")
	
Label(text="What you want to order?").pack()

items=["Dosa","Paneer","Samosa","Kheer"]
var=IntVar()
var.set(None)
for i in range(len(items)):
	radio=Radiobutton(root,text=items[i],variable=var,value=i).pack(anchor="w")
	
Button(text="Order Now", command=order).pack(anchor="w")
	

root.mainloop()