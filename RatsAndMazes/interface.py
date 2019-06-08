from tkinter import Canvas, Tk
import time
# root = Tk()
# root.title('RatAndMazes')
# root.geometry('800x800+0+0')
from turtle import RawTurtle, RawPen
sizeTile = 25
nbrTileW = 8
nbrTileH = 8
width = sizeTile*nbrTileW
height = sizeTile*nbrTileH
root = Tk()
padding = 150
CanvasW = width+padding
CanvasH = height+padding
root.geometry('%dx%d+0+0' % (CanvasW, CanvasH))
cv1 = Canvas(root, width=CanvasW, height=CanvasH, bg="#ddffff")
cv1.pack()
# root.mainloop()


class Rat(RawTurtle):
    """docstring for Rat."""

    def __init__(self, posX=0, posY=0, speed=1, canvas=cv1, colorIn="yellow"):
        super(Rat, self).__init__(canvas)
        self.ht()
        self.up()
        self.speed(0)
        self.goto(posX, posY)
        self.shape('turtle')
        self.color('red', colorIn)
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

    def forward(self, distance=sizeTile):
        super(Rat, self).forward(distance)

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


class Tile():
    """docstring for Tile."""

    def __init__(self, x=0, y=0, canvas=cv1):
        self.top = False
        self.right = False
        self.bottom = False
        self.left = False
        self.canvas = canvas
        self.x = x
        self.y = y
        self.posToTileNbr()
        print("col", self.col)
        print("line", self.line)
        self.draw()

    def draw(self):
        pen = RawPen(self.canvas)
        pen.pencolor('black')
        pen.fillcolor("blue")
        pen.up()
        pen.goto(self.x-sizeTile/2, self.y+sizeTile/2)
        pen.down()
        pen.seth(0)
        for x in range(4):
            pen.forward(sizeTile)
            pen.right(90)

    def tileToPos(self):
        self.x = (((self.col-1)*sizeTile)-height/2)
        self.y = -(((self.line-1)*sizeTile)-width/2)

    def posToTileNbr(self):
        print("self.x : ", self.x)
        print("self.y : ", self.y)
        self.col = ((self.x + height/2) / sizeTile) + 1
        self.line = ((-self.y + width/2) / sizeTile) + 1


class Tile2():
    """docstring for Tile2."""

    def __init__(self, col, line):
        self.col = col
        self.line = line


# for x in range(nbrTileW):
#     for y in range(nbrTileH):
#         print(x+1, y+1)
#         case = Tile2(x+1, y+1)
#         x1, y1 = tileToPos(case)
#         john = Rat(round(x1), round(y1))
def tileToPos(Tile):
    print("Tile.col : ", Tile.col)
    print("Tile.line : ", Tile.line)
    print("width", width)
    print("height", height)

    x = (((Tile.col-1)*sizeTile)-height/2)
    y = -(((Tile.line-1)*sizeTile)-width/2)
    print(x, y)
    return x, y


# cadre = Rat(-width/2, height/2, colorIn="black", speed=0)
# cadre.down()
# cadre.forward(width)
# cadre.right(90)
# cadre.forward(height)
# cadre.right(90)
# cadre.forward(width)
# cadre.right(90)
# cadre.forward(height)

# # 1 1
# tile = Tile2(1, 1)
# x, y = tileToPos(tile)
# rat = Rat(x, y, colorIn="blue")
#
# tile = Tile2(2, 1)
# x, y = tileToPos(tile)
# rat = Rat(x, y)
# tile = Tile2(1, 2)
# x, y = tileToPos(tile)
# rat = Rat(x, y)
# tile = Tile2(2, 2)
# x, y = tileToPos(tile)
# rat = Rat(x, y, colorIn="green")
# for x in range(nbrTileW):
#     for y in range(nbrTileH):
#         tile = Tile2(x+1, y+1)
#         x1, y1 = tileToPos(tile)
#         rat = Rat(x1, y1, colorIn="blue", speed=0)
#         rat.down()
#         for i in range(4):
#             rat.forward(sizeTile)
#             rat.right(90)

tile = Tile(-width/2, height/2)
tile = Rat(-width/2, height/2)
time.sleep(10)
