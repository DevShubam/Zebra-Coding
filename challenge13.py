import turtle

window = turtle.Screen()

shub = turtle.Turtle()

radius = int(input ('What do you want the radius of the circle to be?') )

shub.circle(radius)

turtle.getscreen()._root.mainloop() # Keeps turtle window open
