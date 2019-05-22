from tkinter import Canvas, Tk
# root = Tk()
# root.title('RatAndMazes')
# root.geometry('800x800+0+0')
# root.mainloop()
from turtle import *
sizeCase = 25
root = Tk()
cv1 = Canvas(root, width=800, height=800, bg="#ddffff")
cv1.pack()


class Rat(RawTurtle):
    """docstring for Rat."""

    def __init__(self, posX=0, posY=0, speed=1, canvas=cv1):
        super(Rat, self).__init__(canvas)
        self.ht()
        self.up()
        self.speed(0)
        self.goto(posX, posY)
        self.shape('turtle')
        self.color('red', 'yellow')
        self.st()
        self.speed(speed)

    def teleport(self, x, y):
        self.ht()
        if self.isdown():
            self.up()
        speed = self.speed()
        self.speed(0)
        self.goto(x, y)
        self.speed(speed)
        self.st()

    def forward(self):
        super(Rat, self).forward(sizeCase)

    def goLeft(self):
        self.left(90)
        self.forward()

    def goRight(self):
        self.right(90)
        self.forward()

class Maze():
    """docstring for Maze."""

    def __init__(self, arg):
        super(Maze, self).__init__()
        self.arg = arg

class Case():
    """docstring for Case."""

    def __init__(self, x=0, y=0, canvas=cv1):
        self.top = False
        self.right = False
        self.bottom = False
        self.left = False
        self.canvas = canvas
        self.x = x
        self.y = y

    def draw(self):
        pen = RawPen(self.canvas)
        pen.pencolor('black')
        pen.goto(self.x-sizeCase/2, self.y+sizeCase/2)
        pen.seth(0)

bob = Rat()
john = Rat(100, 100)
case = Case()
case.draw()
for x in [bob, john]:
    x.goLeft()
    x.goLeft()
    x.goLeft()
    x.forward()
    x.goRight()
