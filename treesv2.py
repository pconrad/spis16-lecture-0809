import turtle
import math    

def drawTree(t,tcolor):
    ''' draw a tree '''

    t.color(tcolor)

    # draw the base
    t.setheading(90) # point up
    t.forward(100)
    
    t.right(90)
    t.circle(50)


def drawStuff(t):
    ''' draw some example houses '''
    
    drawTree(t,"green")
    t.goto(200,200)
    drawTree(t,"purple")
    t.goto(-200,-200)
    drawTree(t,"red")


if __name__ == "__main__":
    x = raw_input("Press return when ready to see the turtle")
    fred = turtle.Turtle()
    x = raw_input("Press return when ready to draw")
    drawStuff(fred)
    x = raw_input("Press return when done")
