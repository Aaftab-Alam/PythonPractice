from tkinter import *
from os import listdir
import tkinter.messagebox as tmsg




root= Tk()
root.title("File Opener")
root.geometry("1000x2000")

scrollbar=Scrollbar(root,width=0)
scrollbar.pack(side=RIGHT,fill=Y)

file_name="/storage/emulated/0"
name=""
def next(event=None):
	global name
	name=listbox.get(listbox.curselection())
	
	global file_name
	#dirs=os.listdir(f'/storage/emulated/0/{name}')
	file_name=file_name+"/"+str(name)
	
	files()
	
def back():
	global file_name
	#-----------------#
	file_name=file_name.rsplit("/",1)[0]
	#-----------------#
	files()


def files():
		try:
			dirs=os.listdir(file_name)
			
			dirs.sort()
			global listbox
			
			last=listbox.size()
			listbox.delete(0,last)
	
			
			for i in dirs:
				listbox.insert(END,i)
				
			
		except:
			tmsg.showinfo("Can't Open","Sorry ,the selected file is not \na directory")
			back()

		
frame=Frame(root)
frame.pack(side=BOTTOM,fill=X)	
Button(frame,text="Open", command=next).pack(side=RIGHT,padx=30)

Button(frame,text="Back",command=back).pack(side=LEFT,padx=30)

listbox=Listbox(root, yscrollcommand=scrollbar.set, height=1000, selectbackground="sky blue",selectforeground="purple", activestyle="none")
listbox.pack(fill=X)
listbox.bind("<Double-1>",next)
files()

scrollbar.config(command=listbox.yview)
root.mainloop()