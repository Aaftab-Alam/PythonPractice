from tkinter import *
root=Tk()

root.geometry("1000x700")
def getvalue():
	root1=Tk()
	root1.geometry("1000x700")
	
	name=Label(root1,text=f"My name is {uservalue.get()}")
	name.grid(sticky="w")
	
	passw=Label(root1,text=f"My password is {passvalue.get()}")
	passw.grid(row=1, sticky="w")
	
	
	root1.mainloop()
	root.destroy()
	
user=Label(root,text="Name:")
password=Label(root,text="Password:")
user.grid(sticky="w")
password.grid(row=1)

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root, textvariable=passvalue)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit" ,command=getvalue).grid()
root.mainloop()