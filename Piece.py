class Piece:
    def __init__(self, sq):
        self.sq = sq
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.giveValue()
    def giveValue(self):
        self.value = 0
        self.name = ' '
        if self.sq[1] in ['2', '7']:
            self.value = 1.0
            self.name = 'p'
        elif self.sq[1] in  ['1', '8']:
            if self.sq[0] in ['a', 'h']:
                self.value = 5.0
                self.name = 'r'
            elif self.sq[0] in ['b', 'g']:
                self.value = 2.9
                self.name = 'k'
            elif self.sq[0] in ['c', 'f']:
                self.value = 3.0
                self.name = 'b'
            elif self.sq in ['e1', 'e8']:
                self.value = 70.0
                self.name = 'K'
            elif self.sq in ['d1', 'd8']:
                self.value = 9.0
                self.name = 'Q'
            elif self.sq[0] not in self.letters or self.sq[1] not in self.numbers:
                sq = str(input('Give a valid square: '))
                self = Piece(sq)
            elif self.value != 0:
                pass
        return self

    def __str__(self):
        s = ''
        if self.value == 0:
            s += '   |'
            #s += self.sq + ' |'
        else:
            s += ' ' + self.name + ' |'
        return s