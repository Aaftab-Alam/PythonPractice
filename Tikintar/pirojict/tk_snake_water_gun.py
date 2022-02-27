from tkinter import *
import random
root=Tk()
root.title("Snake_water&gun")
root["bg"]="#eff"
root.geometry("1000x1000")

comp_list=["Snake","Water","Gun"]
def func(event):
	global var
	user=event.widget.cget("text")
	comp=random.choice(comp_list)
	txt=f"You selected {user}\nComputer selected {comp}"
	if user==comp:
		var.set(f"Tie!\n{txt}")
	elif (user=="Snake" and comp=="Water") or (user=="Water" and comp=="Gun") or (user=="Gun" and comp=="Snake"):
		var.set(f"You won!\n{txt}")
	else:
		var.set(f"You lost!\n{txt}")
		
	lbl.update()
	


frame1=Frame(root,bg="#eff")
frame1.pack(side=TOP,fill=X)

var=StringVar()
var.set("Let's Start")
lbl=Label(frame1, textvariable=var,bg="#eff")
lbl.pack(pady=(300,0))



frame2=Frame(root,bg="#eff")
frame2.pack(side=BOTTOM,ipady=180)

btn_list=["Snake","Water","Gun"]
for i in btn_list:
	btn=Button(frame2,text=i,bg="#ffb6c1", activebackground="#38aaf8")
	btn.pack(side=LEFT,padx=20)
	btn.bind("<Button-1>",func)
	

root.mainloop()