import turtle
import math    

def drawTree1(t):
    ''' draw a tree '''

    # draw the base
    t.setheading(90) # point up
    t.forward(100)
    
    t.circle(50)

def drawTree2(t):
    ''' draw a tree '''

    # draw the base
    t.setheading(90) # point up
    t.forward(100)
    
    t.left(90)
    t.circle(50)

def drawTree3(t):
    ''' draw a tree '''

    # draw the base
    t.setheading(90) # point up
    t.forward(100)
    
    t.right(90)
    t.circle(50)


def drawStuff(t):
    ''' draw some example houses '''
    
    drawTree1(t)
    


if __name__ == "__main__":
    x = raw_input("Press return when ready to see the turtle")
    fred = turtle.Turtle()
    x = raw_input("Press return when ready to draw")
    drawStuff(fred)
    x = raw_input("Press return when done")
