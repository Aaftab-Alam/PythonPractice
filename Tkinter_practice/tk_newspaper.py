from tkinter import *
from PIL import ImageTk,Image  

root=Tk()
root.geometry("1000x1200")
root.title("Newspaper")
heading=Label(root,text="Latest News",font="X 11 bold")
heading.pack()

datee=Label(root,text="29/02/2021",font="X 4 bold")
datee.pack()

for i in range(2):
	img=Image.open("news.jpg")
	resize_img= img.resize((200,150), Image.ANTIALIAS)
	final_img = ImageTk.PhotoImage(resize_img)
	
	butt=Button(root,activebackground="#33B5E5")
	butt.pack(pady=(80,0))
	frame=Frame(butt)
	frame.pack(padx=40,pady=15)
	
	label=Label(frame,text="Realme ने कॉपी किया \nApple iPhone का ये खास फीचर, अब कम कीमत \nवाले इस फोन में भी मिलेगा आईफोन जैसा \nमज़ा",font="X 5",justify=LEFT)
	label.pack(side="left",padx=(0,100))
	
	
	Label(frame,image=final_img).pack(side=RIGHT)

root.mainloop()