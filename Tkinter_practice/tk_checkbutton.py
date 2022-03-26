from tkinter import *
root=Tk()

root.geometry("1000x700")
def getvalue():
	
	name=Label(root,text=f"My name is {uservalue.get()}")
	name.grid(row=4,sticky="w")
	
	passw=Label(root,text=f"My password is {passvalue.get()}")
	boxlabel=Label(root,text=f"Value of checkbutton {box.get()}")
	boxlabel.grid(row=6, sticky="w")
	passw.grid(row=5,sticky="w")
	
	
user=Label(root,text="Name:")
password=Label(root,text="Password:")
user.grid(sticky="w")
password.grid(row=1,sticky="w")

uservalue=StringVar()
passvalue=StringVar()
box=IntVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root, textvariable=passvalue)
boxentry=Checkbutton(root,text="Yes",variable=box)

userentry.grid(row=0,column=1,sticky="w")
passentry.grid(row=1,column=1,sticky="w")
boxentry.grid(row=2,sticky="w")

Button(text="Submit" ,command=getvalue).grid(row=3,sticky="w")
root.mainloop()