from tkinter import *
import random
canvas_width = 1000
canvas_height = 900

def origin(event):
	global x2,y2
	x2,y2=event.x,event.y
	
def paint( event ):
  colors_list=["red","green","blue"]
  color=random.choice(colors_list)
  global x2,y2
 # x2,y2=0,0
  x1,y1=event.x,event.y
  w.create_line( x2,y2,x1,y1, fill = color ,smooth=True)
  x2,y2=x1,y1


master = Tk()
master.title( "Paint Brush" )
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind("<Button-1>",origin)
w.bind( "<B1-Motion>", paint )


message = Label( master, text = "Press and Drag the mouse to draw" )
message.pack(  )

Button(text="Clear",command=lambda :w.delete("all")) .pack(side=BOTTOM)


       
mainloop()