from tkinter import *
root=Tk()
root.geometry("1000x1000")

def change():
	frame2["bg"]=colors[var.get()]
    #radio["bg"]=colors[var.get()]

frame=Frame(root)
frame.pack(side=LEFT,anchor="nw")

frame2=Frame(root)
frame2.pack(side=TOP)
Label(frame2,text="").pack(padx=170,pady=500)

Label(frame,text="Change window color to:-",font="lucida 10 bold").pack(anchor="n")

var=IntVar()
var.set(None)



colors=["red","cyan","yellow","blue","black","white","pink","green","orange"]

for i in range(len(colors)):
	radio=Radiobutton(frame,text=colors[i].capitalize(),variable=var,value=i,command=change)
	radio.pack(anchor="w")

#Button(text="Submit",command=change).pack()
root.mainloop()