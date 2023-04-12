import turtle

def draw_circle():
    # Create a turtle object
    my_turtle = turtle.Turtle()

    # Set the speed of the turtle
    my_turtle.speed(10)

    # Set the pen color
    my_turtle.pencolor("red")

    # Start drawing the circle
    for i in range(360):
        my_turtle.forward(2)
        my_turtle.right(1)

    # Hide the turtle when finished
    my_turtle.hideturtle()

    # Wait for user input to close the window
    turtle.done()

# Call the function to start drawing
draw_circle()
