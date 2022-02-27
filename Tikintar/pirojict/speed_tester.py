import pyspeedtest
from tkinter import *
from tkinter import ttk



root=Tk()
root.geometry("1000x1200")

def test():
	down.set("Testing...")
	up.set("Testing...")
	ping.set("Testing...")
	root.update()
	st=pyspeedtest.SpeedTest("www.google.com")
	down.set(st.download())
	#up.set(st.upload())
	#ping.set(st.ping())

up=StringVar()
up.set("0.0")
down=StringVar()
down.set("0.0")
ping=StringVar()
ping.set("0ms")

f1=Frame(root)
f1.pack(side=TOP,fill=X)
separator = ttk.Separator(root,orient='horizontal')
separator.pack(fill=X)
f2=Frame(root)
f2.pack(side=TOP,fill=BOTH,pady=30)

separator = ttk.Separator(root,orient='horizontal')
separator.pack(fill=X)
f3=Frame(root)
f3.pack(side=BOTTOM, fill=X)

l1=Label(f1,text="Speedtest",font="Lucida 17 bold",fg="purple")
l1.pack(anchor="nw")

l2=Label(f2,text="Download Speed",font="Helvetica 13 bold")
l2.pack(anchor="nw")

l3=Label(f2,textvariable=down,font=("Noto Serif",40))
l3.pack(anchor="c",pady=120)
f_down=Frame(f2)
f_down.pack(side=BOTTOM,fill=X)

l4=Label(f2,text="Upload Speed",font="lucida 7 bold")
l4.pack(side=LEFT,anchor="w")

l5=Label(f_down,textvariable=up,font=("Noto Serif",6))
l5.pack(side=LEFT)

l6=Label(f2,text="Ping",font="lucida 7 bold")
l6.pack(side=RIGHT,anchor="e")

l6=Label(f_down,textvariable=ping,font="lucida 6")
l6.pack(side=RIGHT)



button=Button(f3,text="Test",command=test)
button.pack(pady=30)

root.mainloop()