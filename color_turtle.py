import turtle
loc1=("dark slate blue","crimson","indigo","cyan","purple","white","deep pink")

loc=("indigo","cyan","deep pink","purple","white","dark slate blue","crimson")


t=turtle.Turtle()
e=turtle.Turtle()
f=turtle.Turtle()
g=turtle.Turtle()
screen=turtle.Screen()
screen.title("Polygon")
screen.setup(1000,1980)
screen.bgcolor("black")
turtle.delay(0)
turtle.tracer(30)

col=loc1
def func(a):
	a.speed(0)
	a.ht()
	global col
	if col==loc1:
		col=loc
	else:
		col=loc1
	for i in range(650):
		a.color(col[i%7])
		a.forward(i*1.5)
		a.left(52.25)
		a.width(3)
	
#	a.goto(0,0)
		
func(e)
func(t)
func(f)
func(g)