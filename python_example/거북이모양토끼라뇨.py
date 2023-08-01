import turtle

# Set up the turtle
screen = turtle.Screen()
screen.title("Control the Rabbit")
screen.bgcolor("lightblue")

rabbit = turtle.Turtle()
rabbit.shape("turtle")
rabbit.color("brown")
rabbit.penup()

# Function to move the rabbit forward by 500 units
def move_forward():
    rabbit.forward(500)

# Function to turn the rabbit left
def turn_left():
    rabbit.left(15)

# Function to turn the rabbit right
def turn_right():
    rabbit.right(15)

# Bind keyboard keys to the functions
screen.listen()
screen.onkeypress(move_forward, "Up")
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")

# Start the event loop
turtle.done()
