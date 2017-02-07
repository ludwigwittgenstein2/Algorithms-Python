#!/bin/env python

"""
Author: Rick Sam
Date: Jan 23, 2017
Handshake problem


Definition: If there are n-people in the room,
how many handshakes are there?

Input: 4
Output: 6

version:0.1

"""
from graphics import *


def handshake():
    win = GraphWin('Enter Handshake', 360, 180)

    head = Rectangle(Point(50,50), 20)
    head.draw(win)

    text = Text(Point(win.getWidth()/2, 30),'Enter handshakes')
    p1 = win.getMouse()
    p1.input("Enter the number of people in the room")
#   n = int(p1)
#   print "The number of people in room is:", n
#   f = (n*(n-1)/2)
#   print f



if __name__ == '__main__':
    handshake()

