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
        pass

    def pushdisk(self, disk):
        pass

    def popdisk(self):
        pass


class Hanoi(object):
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        self.startp = Pole(start, 0, 0)
        self.workspacep = Pole(workspace, 150, 0)
        self.destinationp = Pole(destination, 300, 0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()

        for i in range(n):
            self.startp.pushdisk(Disk("d"+str(i), 0, i*150, 20, (n-i)*30))


    def move_disk(self, start, destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower(self, n, s, d, w):
        if n == 1:
            self.move_disk(s, d)
        else:
            self.move_tower(n -1, s, w, d)
            self.move_disk(s, d)
            self.move_tower(n -1, w, d, s)

    def solve(self):
        self.move_tower(3, self.startp, self.destinationp, self.workspacep)

h = Hanoi()
h.solve()
