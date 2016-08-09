import turtle
import math    

def drawHouse(t):
    ''' draw a house '''

    # draw the base
    t.forward(100)

    # draw the right wall
    t.left(90)
    t.forward(50)

    # draw the line between 1st story and roof
    t.left(90)
    t.forward(100)

    # draw the left wall
    t.left(90)
    t.forward(50)

    # backup and turn around
    t.backward(50)
    t.left(180)

    # Go to peak of roof.   Its a 45 degree angle, so its
    # is sqrt(2) times 50 long

    t.right(45)
    t.forward(math.sqrt(2.0) * 50)

    # rest of roof
    
    t.right(90)
    t.forward(math.sqrt(2.0) * 50)

    

def drawStuff(t):
    ''' draw some example houses '''
    
    drawHouse(t)
    


if __name__ == "__main__":
    x = raw_input("Press return when ready to see the turtle")
    fred = turtle.Turtle()
    x = raw_input("Press return when ready to draw")
    drawStuff(fred)
    x = raw_input("Press return when done")
