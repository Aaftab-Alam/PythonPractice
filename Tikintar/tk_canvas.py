from tkinter import *
root=Tk()

root.geometry("1000x700")
can=Canvas(root,width=1000, height=700)
can.pack()
#line
can.create_line(0,100,800,100)

#rectangle
can.create_rectangle(0,0,100,50,fill="blue")

#oval
can.create_oval(500,500,800,700,fill="red")

#circle
can.create_oval(0,100,400,500)
root.mainloop()