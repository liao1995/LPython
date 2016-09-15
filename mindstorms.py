import turtle

def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_art(brad):
	brad.shape("turtle")
	brad.color("white")
	brad.speed(6)
	draw_square(brad)
	brad.shape("arrow")
	brad.circle(-100)	

def start_draw():
	window = turtle.Screen()
	window.bgcolor("black")
	# Create the turtle Brad - Draws a square
	brad = turtle.Turtle()
	
	for i in range(1,13):
		draw_art(brad)	
		brad.left(30)
	window.exitonclick()

start_draw()

