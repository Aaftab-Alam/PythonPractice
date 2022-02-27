from tkinter import *
root=Tk()
root.geometry("1000x1000")
root.title("Calculator")

def func(event):
	global var
	val=event.widget.cget("text")
	if val=="C":
		var.set("")
	elif val=="=":
		try:
			result=eval(var.get())
		except:
			result="Invalid Syntax"
		var.set(result)
	else:
		var.set(str(var.get())+val)
	wdgt.update()
	
var=StringVar()
var.set("")
wdgt=Entry(root, textvariable=var, font="arial 15 bold",justify="right",fg="#654575")
wdgt.pack(side=TOP,fill=X,pady=(20,5),ipady=10)
top_frame=Frame(root)
top_frame.pack(side=TOP,anchor="c")	

count=0

frame1=Frame(top_frame)
frame1.pack(side=LEFT)

frame=None
def button(digit,px=30,py=30,bg="#fff"):
	global count,frame
	if count%3==0:
		frame=Frame(frame1)
		frame.pack(fill=X)
		
	btn=Button(frame,text=f"{digit}",bg=bg,activebackground="#efe")
	btn.pack(side=LEFT,ipadx=px,ipady=py)
	btn.bind("<Button-1>",func)
	count+=1

button("C",px=215,bg="#eee")
count=0

for i in range(9,-1,-1):
	button(i,px=124) if i==0 else button(i)
button(".",px=37,bg="#eee")
frame2=Frame(top_frame)
frame2.pack(side=LEFT)

btn_list=["/","*","-","+","="]
for char in btn_list:
	btn=Button(frame2,text=char,bg="#eee", activebackground="#efe")
	btn.pack(ipadx=35,ipady=30,fill=X)	
	btn.bind("<Button-1>",func)	
root.mainloop()