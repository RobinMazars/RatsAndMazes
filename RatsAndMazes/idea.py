import pprint

pp = pprint.PrettyPrinter(indent=2).pprint


def createBoard(nbrCaseH, nbrCaseV):
    board = []
    for x in range(nbrCaseV):
        line = []
        for y in range(nbrCaseH):
            line.append([x+1, y+1])
        board.append(line)
    return board


def createWall():
    pass


class Board():
    def __init__(self, nbrCaseH, nbrCaseV):
        self.board = []
        self.pp = pprint.PrettyPrinter(indent=2).pprint
        for x in range(nbrCaseV):
            line = []
            for y in range(nbrCaseH):
                line.append([x+1, y+1])
            self.board.append(line)

    def show(self):
        print('--------------------------------')
        self.pp(self.board)
        print('--------------------------------')

    def getBoard(self):
        return self.board

    def clean(self, position):
        self.board[position.y][position.x] = self.board[position.y][position.x][:2]


class Mj():
    def __init__(self):
        self.createBoard(5, 5)

    def createBoard(self, nbrCaseH, nbrCaseV):
        self.board = Board(nbrCaseH, nbrCaseV)

    def createRat(self, position, name='R'):
        self.rat = Rat(position, name)

    def spawnRat(self):
        RatPosition = self.rat.getPosition()
        self.board.getBoard()[RatPosition.y][RatPosition.x].append(self.rat.name)

    def moveRat(self, mouvX=0, mouvY=0):
        self.cleanBoard(self.rat.getPosition())
        self.rat.move(mouvX, mouvY)
        self.spawnRat()

    def cleanBoard(self, position):
        self.board.clean(position)


class Position():
    def __init__(self, x, y):
        self.x = x-1
        self.y = y-1


class Rat():
    """docstring for Rat."""

    def __init__(self, position, name='Rat'):
        self.position = position
        self.name = name

    def getPosition(self):
        return self.position

    def move(self, mouvX=0, mouvY=0):
        self.position.x += mouvX
        self.position.y += mouvY
        return self.position


if __name__ == '__main__':
    nbrCaseH = 8
    nbrCaseV = nbrCaseH
    nbrCaseTotal = nbrCaseH + nbrCaseV
    origineX = 1
    origineY = 2
    mj = Mj()
    mj.createBoard(nbrCaseH, nbrCaseV)
    mj.createRat(Position(origineX, origineY))
    mj.board.show()
    mj.spawnRat()
    mj.board.show()
    mj.moveRat(1, 0)
    mj.board.show()
    mj.moveRat(0, 1)
    mj.board.show()
