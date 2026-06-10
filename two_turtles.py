import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Non-blocking Dual Turtles")

# Turn off automatic animation for smooth, simultaneous rendering
screen.tracer(0)

# Create the first turtle (Red)
red_turtle = turtle.Turtle()
red_turtle.color("red")
red_turtle.shape("turtle")
red_turtle.penup()
red_turtle.goto(-100, 100)

# Create the second turtle (Blue)
blue_turtle = turtle.Turtle()
blue_turtle.color("blue")
blue_turtle.shape("turtle")
blue_turtle.penup()
blue_turtle.goto(-100, -100)

# Move both turtles simultaneously in a loop
for _ in range(200):
    red_turtle.forward(2)
    red_turtle.right(1)
    
    blue_turtle.forward(2)
    blue_turtle.left(1)
    
    # Manually update the screen to show both movements at once
    screen.update()
    time.sleep(0.01)

# Keep the window open
screen.mainloop()
