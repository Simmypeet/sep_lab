from turtle import *


class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

    def showdish(self):
        pass

    def newpos(self, xpos, ypos):
        pass

    def cleardisk(self):
        pass

class Pole(object):
    def __init__(self, name="", xpos=0, ypos=0, thick=10, length=100):
        self.pname = name
        self.stack = []
        self.toopos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

    def showpole(self):
        pen = Turtle()
        pen.penup()
        pen.goto(self.pxpos, self.pypos)
        pen.pendown()
        pen.forward(self.pthick / 2)
        pen.left(90)
        pen.forward(self.plength)
        pen.left(90)
        pen.forward(self.pthick)
        pen.left(90)
        pen.forward(self.plength)
        pen.left(90)
        pen.forward(self.pthick / 2)

    def pushdisk(self, disk: Disk):
        self.stack.append(disk)
        self.toopos += disk.dheight
        disk.showdish()

    def popdisk(self):
        pass