import turtle
import math

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle instance
t = turtle.Turtle()
t.speed(1)
t.pensize(2)  # Set the pen size

# Define a function to draw a rectangle
def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

# Define a function to draw a circle
def draw_circle(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.circle(radius)

# Define a function to translate a 2D object
def translate(x, y, dx, dy):
    t.penup()
    t.goto(x + dx, y + dy)
    t.pendown()

# Define a function to rotate a 2D object
def rotate(x, y, angle):
    t.penup()
    t.goto(x, y)
    t.setheading(t.heading() + angle)
    t.pendown()

# Define a function to scale a 2D object
def scale(x, y, sx, sy):
    t.penup()
    t.goto(x * sx, y * sy)
    t.pendown()

# Draw a rectangle
draw_rectangle(-200, 0, 100, 50, "blue")

# Translate the rectangle
translate(-200, 0, 200, 0)
draw_rectangle(0, 0, 100, 50, "blue")

# Reset position and heading for rotation
t.penup()
t.goto(0, 0)
t.setheading(0)
t.pendown()

# Rotate the rectangle
rotate(0, 0, 45)
draw_rectangle(0, 0, 100, 50, "blue")

# Reset position and heading for scaling
t.penup()
t.goto(0, 0)
t.setheading(0)
t.pendown()

# Scale the rectangle (Note: scaling won't work as expected with turtle graphics)
# Here we're manually adjusting the size for demonstration
draw_rectangle(0, 0, 200, 100, "blue")

# Draw a circle
draw_circle(100, 100, 50, "red")

# Translate the circle
translate(100, 100, 200, 0)
draw_circle(300, 100, 50, "red")

# Reset position and heading for rotation
t.penup()
t.goto(300, 100)
t.setheading(0)
t.pendown()

# Rotate the circle (Note: rotation won't affect the circle shape in turtle graphics)
rotate(300, 100, 45)
draw_circle(300, 100, 50, "red")

# Reset position and heading for scaling
t.penup()
t.goto(300, 100)
t.setheading(0)
t.pendown()

# Scale the circle (Note: scaling won't work as expected with turtle graphics)
# Here we're manually adjusting the size for demonstration
draw_circle(600, 200, 100, "red")

# Keep the window open until it's closed
turtle.done()
