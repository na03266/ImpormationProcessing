import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Obstacle Avoiding Game")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)

# Create the turtle (player)
player = turtle.Turtle()
player.shape("turtle")
player.color("brown")
player.penup()

# Set the speed of the player turtle
player_speed = 15

# Function to move the player turtle up
def move_up():
    y = player.ycor()
    if y < 290:  # Limit the player's movement to stay within the screen
        player.sety(y + player_speed)

# Function to move the player turtle down
def move_down():
    y = player.ycor()
    if y > -280:  # Limit the player's movement to stay within the screen
        player.sety(y - player_speed)

# Function to create obstacles
def create_obstacle():
    obstacle = turtle.Turtle()
    obstacle.shape("square")
    obstacle.color("red")
    obstacle.shapesize(stretch_wid=1, stretch_len=4)
    obstacle.penup()
    x = random.randint(-380, 380)
    y = random.randint(-280, 280)
    obstacle.goto(x, y)
    return obstacle  # Add "obstacle" as the return value

# List to store the obstacles
obstacles = []

# Rest of the code remains the same
