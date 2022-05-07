import turtle
window = turtle.Screen()
artist = turtle.Turtle()


def makesquare():
    artist.fillcolor(colorinput)
    artist.begin_fill()
    for i in range(4):
        artist.forward(sizeinput)
        artist.left(90)
    artist.end_fill()


def makecircle():
    artist.fillcolor(colorinput)
    artist.begin_fill()
    for i in range(1):
        artist.circle(sizeinput)
    artist.end_fill()

    
def maketriangle():
    artist.fillcolor(colorinput)
    artist.begin_fill()
    for i in range(3):
        artist.forward(sizeinput)
        artist.left(120) 
    artist.end_fill()

userinput = int(input("Do you want to make a square, circle, or triangle? Enter 1 for a square. 2 for a circle. 3 for a triangle: "))
sizeinput = int(input("What is the size of the shape: "))
colorinput = str(input("What color do you want the shape to be: "))

if userinput == 1:
    makesquare()

if userinput == 2:
    makecircle()

if userinput == 3:
    maketriangle()



# Keeps the window open
turtle.done()
