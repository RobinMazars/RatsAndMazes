from tkinter import Canvas, Tk
import time
import random
# root = Tk()
# root.title('RatAndMazes')
# root.geometry('800x800+0+0')
from turtle import RawTurtle, RawPen
sizeTile = 25
nbrTileW = 3
nbrTileH = 5
width = sizeTile*nbrTileW
height = sizeTile*nbrTileH
root = Tk()
padding = 150
CanvasW = width+padding*2
CanvasH = height+padding*2
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

    def __init__(self, canvas=cv1):
        self.CreateTile()
        # self.drawAll()
        for value in range(1):
            self.start()

    def CreateTile(self):
        self.listeTile = []
        for x in range(nbrTileW):
            for y in range(nbrTileH):
                # print(x, y)
                self.listeTile.append(Tile(x+1, y+1))

    def drawAll(self):
        for x in self.listeTile:
            x.draw()

    def start(self):
        nbrExtTile = ((nbrTileW*2)-1+(nbrTileH*2)-1)-1
        for rngNbr1 in range(1, nbrExtTile+1):
            print("nbrExtTile :", nbrExtTile)
            print(rngNbr1)
            self.tileStart = {}
            if rngNbr1 <= nbrTileW:
                print("<1/4")
                self.tileStart["col"] = rngNbr1
                self.tileStart["line"] = 1
            elif rngNbr1 < nbrTileH + nbrTileW:
                print("<2/4")
                self.tileStart["col"] = nbrTileW
                self.tileStart["line"] = rngNbr1 - nbrTileW +1
            elif rngNbr1 < nbrTileW * 2 + nbrTileH-1:
                print("<3/4")
                self.tileStart["col"] = nbrTileW*2+nbrTileH - rngNbr1-1
                self.tileStart["line"] = nbrTileH
            else:
                print("<4/4")
                self.tileStart["col"] = 1
                self.tileStart["line"] = (nbrTileH*2+nbrTileW*2) - rngNbr1 - 2
            print(self.tileStart)
            testTile = Tile(self.tileStart["col"], self.tileStart["line"])
            testTile.draw()


class Tile():
    """docstring for Tile."""

    def __init__(self, col, line, canvas=cv1):
        self.border = [True,
                       True,
                       True,
                       True,
                       ]
        self.canvas = canvas
        self.col = col
        self.line = line
        self.tileToPos()

    def draw(self):
        pen = RawPen(self.canvas)
        pen.ht()
        pen.pencolor('black')
        pen.fillcolor("blue")
        pen.speed(0)
        pen.up()
        pen.goto(self.x, self.y)
        pen.seth(0)
        center = self.getCenter()
        print(center)
        for x in self.border:
            if x is True:
                pen.down()
                pen.forward(sizeTile)
                pen.up()
            else:
                pen.forward(sizeTile)
            pen.right(90)
        self.drawTexte()

    def tileToPos(self):
        self.x = (((self.col-1)*sizeTile)-height/2)
        self.y = -(((self.line-1)*sizeTile)-width/2)

    def posToTileNbr(self):
        print("self.x : ", self.x)
        print("self.y : ", self.y)
        self.col = ((self.x + height/2) / sizeTile) + 1
        self.line = ((-self.y + width/2) / sizeTile) + 1

    def getCenter(self):
        center = {}
        center["x"] = self.x+sizeTile/2
        center["y"] = self.y-sizeTile/2
        return center

    def drawTexte(self):
        center = self.getCenter()
        pen = RawPen(self.canvas)
        pen.ht()
        pen.up()
        pen.goto(center["x"]-5, center["y"])
        pen.write("%d:%d" % (self.col, self.line))


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


cadre = Rat(-width/2, height/2, colorIn="black", speed=0)
cadre.down()
cadre.forward(width)
cadre.right(90)
cadre.forward(height)
cadre.right(90)
cadre.forward(width)
cadre.right(90)
cadre.forward(height)

# 1 1
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
#         tile = Tile(x+1, y+1)
#         tile.tileToPos()
#         rat = Rat(x1, y1, colorIn="blue", speed=0)
#         rat.down()
#         for i in range(4):
#             rat.forward(sizeTile)
#             rat.right(90)

maze = Maze()
time.sleep(10)
