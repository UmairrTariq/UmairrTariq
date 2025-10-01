from turtle import *

def draw_flag():
    """
    Draws the flag of Palestine.
    """
    # Set up the screen
    screen = Screen()
    screen.title("Palestinian Flag")
    screen.setup(width=600, height=400)
    screen.setworldcoordinates(0, 0, 600, 400)

    # Draw the black stripe
    penup()
    goto(0, 400)
    pendown()
    color("black")
    begin_fill()
    goto(600, 400)
    goto(600, 266.67)
    goto(0, 266.67)
    goto(0, 400)
    end_fill()

    # Draw the white stripe
    penup()
    goto(0, 266.67)
    pendown()
    color("white")
    begin_fill()
    goto(600, 266.67)
    goto(600, 133.33)
    goto(0, 133.33)
    goto(0, 266.67)
    end_fill()

    # Draw the green stripe
    penup()
    goto(0, 133.33)
    pendown()
    color("green")
    begin_fill()
    goto(600, 133.33)
    goto(600, 0)
    goto(0, 0)
    goto(0, 133.33)
    end_fill()

    # Draw the red triangle
    penup()
    goto(0, 0)
    pendown()
    color("red")
    begin_fill()
    goto(200, 200)
    goto(0, 400)
    goto(0, 0)
    end_fill()

    hideturtle()
    screen.exitonclick()

draw_flag()