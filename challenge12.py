import turtle

window = turtle.Screen()

shub = turtle.Turtle() # Name

sideLength = int(input('How long do you want the sides to be?'))

shub.forward(sideLength)
shub.left(90)
shub.forward(sideLength)
shub.left(90)
shub.forward(sideLength)
shub.left(90)
shub.forward(sideLength)

turtle.getscreen()._root.mainloop() # Keeps turtle window open
