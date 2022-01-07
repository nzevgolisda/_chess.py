
from Piece import Piece
class Board:
    def __init__(self):
        self.board = []
        self.createBoard()
    def createBoard(self):
        p = Piece('a1')
        for number in p.numbers:
            row = []
            for letter in p.letters:
                sq = str(letter) + str(number)
                p = Piece(sq)
                row.append(p)
            self.board.append(row)
        print(self)
        return self
    def move(self):
        s = []
        sq2 = str(input('Give the destination square: '))
        for i in range(7, -1, -1):
            for j in range(8):
                p = self.board[i][j]
                if p.sq == sq2:
                    s.append([i, j])
        p2 = self.board[s[0][0]][s[0][1]]
        sq1 = str(input('Give the square of your piece: '))
        for i in range(7, -1, -1):
            for j in range(8):
                p = self.board[i][j]
                if p.sq == sq1:
                    s.append([i, j])
        p1 = self.board[s[1][0]][s[1][1]]
        p2.value = p1.value
        p2.name = p1.name
        p1.value = 0
        p1.name = ' '
        print(self)
        return self
    def __str__(self):
        s = ''
        for i in range(7, -1, -1):
            for j in range(8):
                p = self.board[i][j]
                s += str(p)
            s += ' * '+str(p.numbers[i])
            s += '\n'
        for letter in p.letters:
            s += 2*' *'
        s+= ' *'
        s+= '\n'
        for letter in p.letters:
            s += ' ' + letter + '  '
        return s