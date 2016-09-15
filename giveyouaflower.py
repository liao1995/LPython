import turtle

def draw_parallelogram(brad):
	for i in range(1, 3):
		brad.forward(50)
		brad.right(45)
		brad.forward(50)
		brad.right(135)

def draw():
	window = turtle.Screen()
	window.bgcolor("black")
	brad = turtle.Turtle()
	brad.color("white")
	brad.shape("turtle")
	brad.speed(10)
	for i in range(1, 37):
		draw_parallelogram(brad)
		brad.right(10)
	brad.right(90)
	brad.forward(150)
	window.exitonclick()
draw()

