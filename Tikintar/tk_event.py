from tkinter import *
root=Tk()
root.geometry("1000x500")
a=1
def aadil(event):
	global a
	a+=1
	Label(root,text=f"You clicked butten at {event.x},{event.y}").grid(row=a,sticky="w")
	
widget=Button(root,text="Click me")
widget.grid()

widget.bind("<Button-1>",aadil)


root.mainloop()