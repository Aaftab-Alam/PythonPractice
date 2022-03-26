from tkinter import *
root=Tk()
root.geometry("1000x1000")

def origin(event):
	global x,y
	x=event.x
	y=event.y

def rect(event):
	x1,y1=event.x,event.y
	canvas.delete("last")
	canvas.create_rectangle(x,y,x1,y1,outline="grey", width=5,tag="last")
	canvas.update()
	
def release(event):
	x2,y2=event.x,event.y
	canvas.delete("last")
	canvas.create_rectangle(x,y,x2,y2,fill="#992512",outline="#992512")
	
canvas=Canvas(root,width=700,height=700, highlightbackground="black", highlightthickness=4)
canvas.pack(anchor="c")
canvas.bind("<Button-1>",origin)
canvas.bind("<B1-Motion>",rect)
canvas.bind("<ButtonRelease-1>", release)

Button(text="Clear",command=lambda :canvas.delete("all")).pack()
root.mainloop()