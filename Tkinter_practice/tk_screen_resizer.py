from tkinter import *
root=Tk()
root.geometry("1000x1000")
root.title("Screen Resizer")
f1=Frame(root)
f1.grid(row=0,sticky="w")

f2=Frame(root)
f2.grid(row=1,sticky="w")

def rsze():
	try:
		wdth=wdth_entry.get()
		hght=hght_entry.get()
		root.geometry(f"{wdth}x{hght}")
		poped=Label(f2,text=f"Screen resized to {wdth}x{hght}")
		poped.grid(sticky="w")
		f2.update()
	except:
		poped=Label(f2,text="Please enter a valid value.")
		poped.grid(sticky="w")
		f2.update()

wdth=Label(f1,text="Width:")
wdth.grid(sticky="w")
hght=Label(f1,text="Height:")
hght.grid(row=1,sticky="w")

wdth_entry=Entry(f1)
wdth_entry.grid(row=0,column=1,sticky="w")
hght_entry=Entry(f1)
hght_entry.grid(row=1,column=1,sticky="w")

btn=Button(f1,text="Submit" , command=rsze)
btn.grid(sticky="w")

root.mainloop()