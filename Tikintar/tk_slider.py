from tkinter import *
root=Tk()
root.geometry("1000x1000")

Label(root,text="Brightness").pack()
slider=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=10,length=1000, resolution=10,troughcolor="red")
slider.set(50)
slider.pack()

root.mainloop()