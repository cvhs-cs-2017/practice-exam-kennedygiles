"""Use a loop to make a turtle draw a shape that is has at least 100 sides and
that shows symmetry.  The entire shape must fit inside the screen"""
import turtle
turtle = turtle.Turtle()
for i in range(100):
    turtle.forward(10)
    turtle.right(30)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(50)
    turtle.right(30)

    turtle.penup()
    turtle.setposition(0 ,0)
    turtle.pendown()
    turtle.right(2)
