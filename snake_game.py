import turtle
import time
import random

bg_color=["pink","lightblue"]
head_color=["black","purple"]
num=random.choice([0,1])


#first screen to print "game begins now"
screen0=turtle.Screen()
screen0.bgcolor("black")
screen0.setup(1000,1000)
screen0.bgpic("snake.jpg")
pen=turtle.Turtle()
pen.goto(-185,0)
pen.speed(0)
pen.color("white")
pen.shape("turtle")
pen.write("Game begins now!")
pen.speed(1.35)
pen.goto(185,0)
pen.clear()
pen.hideturtle()




#second screen to show the game
# Creating a window screen 

screen = turtle.Screen() 
screen.title("Snake Game") 
screen.bgcolor(bg_color[num]) 
screen.setup(width=1000, height=1000) 
screen.tracer(0) 



# head of the snake 

head = turtle.Turtle() 
head.shape("square") 
head.color(head_color[num]) 
head.penup() 
head.goto(0, 0) 
head.direction = "Stop"

while True:
	screen.update()
	
	#collison with border
	if head.xcor() > 490 or head.xcor() < -490 or head.ycor() > 490 or head.ycor() < -490: 
		time.sleep(1) 
		head.goto(0, 0) 
		head.direction = "Stop"
		
		

