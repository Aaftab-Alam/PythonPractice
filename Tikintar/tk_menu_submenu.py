from tkinter import *
root=Tk()
root.geometry("1000x1000")

def myfunc():
	print("Hello")

mainmenu=Menu(root)
m1=Menu(mainmenu)
m1.add_command(label="New" , command=myfunc)
m1.add_command(label="Save" , command=myfunc)
m1.add_separator()  #Adds a separation line
m1.add_command(label="Save As" , command=myfunc)
m1.add_command(label="Open" , command=myfunc)


mainmenu.add_cascade(label="File",menu=m1)

m2=Menu(mainmenu)
m2.add_command(label="Image" , command=myfunc)
m2.add_command(label="Adjustment" , command=myfunc)
m2.add_command(label="Effects" , command=myfunc)
m2.add_command(label="Filter" , command=myfunc)


mainmenu.add_cascade(label="Edit",menu=m2)
root.config(menu=mainmenu)


root.mainloop()