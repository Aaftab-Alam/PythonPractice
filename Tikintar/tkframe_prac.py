from tkinter import *
root=Tk()

root.geometry("1000x700")
f1=Frame(root,bg="grey")
#f1.geometry("1000x200")
f1.pack(side=TOP, fill="x")

f2=Frame(root,bg="black")
f2.pack(side=LEFT, fill=Y)

l1=Label(f1,text="Top Bar",bg="white")
l1.pack(pady=5)

l2=Label(f2,text="Side Bar",bg="black",fg="white")
l2.pack(padx=5,side=LEFT)
root.mainloop()