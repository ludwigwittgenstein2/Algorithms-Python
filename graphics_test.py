#!/bin/python

from graphics import *

def makeRect(corner, width, height):
    corner2 = corner
    corner2.move(width, height)
    return Rectangle(corner, corner2)

def circle():
    win = GraphWin('Face', 200, 150) # Title and Dimensions

    head = Circle(Point(40,100), 25) #Creating a circle with center and radius
    head.draw(win)

    eye1 = Circle(Point(30,105), 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2 = Line(Point(45, 105), Point(55, 105)) # Set Co-ordinates
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = Oval(Point(30,90), Point(50,85))
    mouth.setFill("red")
    mouth.draw(win)

    label = Text(Point(100,120), "A Face")
    label.draw(win)

    message = Text(Point(win.getWidth()/2, 20), "Click to click")
    message.draw(win)
    win.getMouse()
    win.close()

def main():
    makeRect(50,10,20)


if __name__ == "__main__":
    main()

