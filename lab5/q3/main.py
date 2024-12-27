import turtle
class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
        self.pen = turtle.Turtle()

    def showdisk(self):
        self.pen.penup()
        self.pen.setpos(self.dxpos, self.dypos)
        self.pen.seth(0)
        self.pen.pendown()
        self.pen.fillcolor("red")
        self.pen.pencolor("black")
        self.pen.begin_fill()
        self.pen.fd(self.dwidth / 2)
        self.pen.left(90)
        self.pen.fd(self.dheight)
        self.pen.left(90)
        self.pen.fd(self.dwidth)
        self.pen.left(90)
        self.pen.fd(self.dheight)
        self.pen.left(90)
        self.pen.fd(self.dwidth / 2)
        self.pen.end_fill()
        

    def newpos(self, xpos, ypos):
        self.dxpos = xpos
        self.dypos = ypos

    def cleardisk(self):
        self.pen.penup()
        self.pen.setpos(self.dxpos, self.dypos)
        self.pen.seth(0)
        self.pen.pendown()
        self.pen.fillcolor("white")
        self.pen.pencolor("white")
        self.pen.begin_fill()
        self.pen.fd(self.dwidth / 2)
        self.pen.left(90)
        self.pen.fd(self.dheight)
        self.pen.left(90)
        self.pen.fd(self.dwidth)
        self.pen.left(90)
        self.pen.fd(self.dheight)
        self.pen.left(90)
        self.pen.fd(self.dwidth / 2)
        self.pen.end_fill()
    
d = Disk("a", 100, 100)
d.showdisk()
d.cleardisk()