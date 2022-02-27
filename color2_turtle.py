import turtle
import time
#time.sleep(3)
col=("red","pink","green","cyan","purple","yellow")
t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("black")
t.speed(1000)
time.sleep(3)

count=0
for i in range(2000):
	t.color(col[i%6])
	t.forward(1+count)
	count+=0.65
#	t.backward()
#	t.shape("circle")
	t.right(29)
#	t.left(1)
#	t.right(25)
#	t.left(1)
	t.width(3)