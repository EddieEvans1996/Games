#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Responsible for pieces.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

class Piece():
    def __init__(self, colour):
        self.colour = colour

    def is_valid_move(self):
        return True

    def is_white(self):
        if self.colour == 'w':
            return True
        else:
            return False

    def __str__(self):
        if self.colour == 'w':
            return self.name
        else:
            return '\033[94m' + self.name + '\033[0m'
            # return self.name.lower()

class King(Piece):
    def __init__(self, colour):
        self.can_castle = True
        super().__init__(colour)
        self.value = 999
        self.name = "K"

    def can_castle(self):
        return self.can_castle
    
    def is_valid_move(self, board, start, end):
        return True

class Queen(Piece):
    def __init__(self, colour):
        super().__init__(colour)
        self.value = 9
        self.name = "Q"

    def is_valid_move(self, board, start, end):
        return True

class Rook(Piece):
    def __init__(self, colour):
        self.value = 5
        super().__init__(colour)
        self.name = "R"

    def is_valid_move(self, board, start, end):
        return True

class Bishop(Piece):
    def __init__(self, colour):
        self.value = 3
        super().__init__(colour)
        self.name = "B"

    def is_valid_move(self, board, start, end):
        return True

class Knight(Piece):
    def __init__(self, colour):
        self.value = 3
        super().__init__(colour)
        self.name = "N"

    def is_valid_move(self, board, start, end):
        return True

class Pawn(Piece):
    def __init__(self, colour):
        self.value = 1
        super().__init__(colour)
        self.name = "P"

    def is_valid_move(self, board, start, end):
        return True

class GhostPawn(Piece):
    def __init__(self, colour):
        self.value = 0
        super().__init__(colour)
        self.name = " "

    def is_valid_move():
        return False