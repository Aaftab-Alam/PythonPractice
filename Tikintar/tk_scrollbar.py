from tkinter import *
root=Tk()
root.geometry("1000x1000")

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox=Listbox(root,yscrollcommand=scrollbar.set)

for i in range(344):
	listbox.insert("end",f"Item {i}")
	
listbox.pack(fill="both")

scrollbar.config(command=listbox.yview)

root.mainloop()