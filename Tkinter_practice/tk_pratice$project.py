from tkinter import *
root=Tk()
root.geometry("1000x800")

mainmenu=Menu(root,bg="#5B5B52")

m1=Menu(mainmenu)
m1.add_command(label="New")
m1.add_command(label="Save")

m1.add_command(label="Save as")


mainmenu.add_cascade(label="File",menu=m1)


m2=Menu(mainmenu)
m2.add_command(label="Image")
m2.add_command(label="Filters")

m2.add_command(label="Adjust")


mainmenu.add_cascade(label="Edit",menu=m2)

mainmenu.add_cascade(label="3D")

mainmenu.add_cascade(label="Help")
root.config(menu=mainmenu)

frame3=Frame(root)
frame3.pack(side=BOTTOM,fill=X)

left_frame=Frame(root,bg="white")
left_frame.pack(side=LEFT,fill=Y,pady=(5,0))

label1=Label(left_frame,text="Projects",bg="white",font="lucida 6")
label1.pack(padx=(0,40))

label1=Label(left_frame,text="Python",font="lucida 6",bg="white")
label1.pack(padx=(0,40),anchor="w")

label1=Label(left_frame,text="Java",bg="white",font="lucida 6")
label1.pack(padx=(0,40),anchor="w")



scrollbar_y=Scrollbar(root,width=16)
scrollbar_y.pack(side=RIGHT,fill=Y)

scrollbar_x=Scrollbar(frame3,width=16, orient=HORIZONTAL)
scrollbar_x.pack(side=BOTTOM,fill=X)
root.mainloop()