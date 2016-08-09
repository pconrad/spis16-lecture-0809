import turtle
import math    

def calculateHypotenuse(a,b):
    ''' if a and b are sides of a right triangle, calculate c, the hypotenuse '''
    return math.sqrt(a**2 + b**2)


def drawHouse(t, houseColor,penSize,height,width):
    ''' draw a house '''

    t.pensize(penSize)
    t.down()
    t.color(houseColor)

    # draw the base
    t.forward(width)

    # draw the right wall
    t.left(90)
    t.forward(height)

    # draw the line between 1st story and roof
    t.left(90)
    t.forward(width)

    # draw the left wall
    t.left(90)
    t.forward(height)

    # backup and turn around
    t.backward(height)
    t.left(180)

    # Go to peak of roof.   Its a 45 degree angle, so its
    # is sqrt(2) times 50 long

    roofAngleInRadians = math.atan( height / (width/2.0) )
    roofAngleInDegrees = math.degrees(roofAngleInRadians)

    roofLength = calculateHypotenuse(height, width/2.0)

    print "roofAngleInDegrees=",roofAngleInDegrees

    t.right(roofAngleInDegrees)
    t.forward(roofLength)

    # rest of roof
    
    t.right(90)  # Rachel thinks this is incorrct (she's right)
    t.forward(roofLength)

    # reset turtle to bottom right, facing east

    t.right(roofAngleInDegrees)  # Andrew T. thinks this is incorrect (he's right)
    t.forward(height)
    t.left(90)
    
    

def drawStuff(t):
    ''' draw some example houses '''

    myColors=["red","purple","turquoise","green","pink","orange"]
    t.goto(-300,0)
    for i in range(6):
      print "drawing house number ",i
      drawHouse(t, myColors[i], 5+(i*2), 50, 100)

    t.up()
    t.goto(-300,-200)

    
    drawHouse(t, "black", 5, 33, 200)


if __name__ == "__main__":
    x = raw_input("Press return when ready to see the turtle")
    fred = turtle.Turtle()
    
    x = raw_input("Press return when ready to draw")
    drawStuff(fred)
    x = raw_input("Press return when done")
