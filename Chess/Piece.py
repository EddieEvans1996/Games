#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Responsible for pieces.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import numpy as np

def valid_diagonal_move(board, start, end):
    #Firstly see if it goes in the diagonal direction
    if abs(start[0] - end[0]) == abs(start[1] - end[1]):
        if abs(start[0] - end[0]) > 1:
            for i in range(1, abs(start[0] - end[0])):
                if board[start[1] + (np.sign(end[1] - start[1])*i)][start[0] + (np.sign(end[0] - start[0])*i)] != None:
                    return False
        if board[end[1]][end[0]] != None:
            if board[end[1]][end[0]].is_white() == board[start[1]][start[0]].is_white():
                return False
            else:
                return True
        else:
            return True
    else:
        return False

def valid_horver_move(board, start, end):
    #Firstly see if it does move in a horizontal or vertical way
    if (start[0] == end[0]) | (start[1] == end[1]):
        #Checking if there are any pieces in the way
        if max(abs(start[0] - end[0]), start[1] - end[1]) > 1:
            for i in range(1, max(abs(start[0] - end[0]), abs(start[1] - end[1]))):
                if board[start[1] + np.sign(end[1] - start[1])*i][start[0] + np.sign(end[0] - start[0])*i] != None:
                    return False
        #Checking if there is a friendly piece on the end square
        if board[end[1]][end[0]] == None: #End square is free
            return True
        elif board[end[1]][end[0]].is_white() != board[start[1]][start[0]].is_white(): #Can capture enemy piece
            return True
        else:
            return False #Else there is a friendly piece which we cannot move to
    else:
        return False

def valid_knight_move(board, start, end):
    #Easy since knight can jump over stuff. Check it has done an L shape, then check if the square is free/capturable
    if ((abs(start[0] - end[0]) == 2) & (abs(start[1] - end[1]) == 1)) | ((abs(start[0] - end[0]) == 1) & (abs(start[1] - end[1]) == 2)):
        if board[end[1]][end[0]] == None:
            return True
        elif board[end[1]][end[0]].is_white() != board[start[1]][start[0]].is_white():
            return True
        else:
            return False
    else:
        return False

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

# We can write functions to check if start and end are on the same row/col/diagonal seperately, and then use them on each of the functions.
#Checking if there is a possible knight move is the other option. This will be put next to the functions mentioned above since this
#will make it clear where all of the code should belong.
class King(Piece):
    def __init__(self, colour, has_moved = False):
        self.can_castle = True
        super().__init__(colour)
        self.value = 999
        self.name = "K"
        self.has_moved = has_moved

    #TODO: #2 Implement castling.
    ##Note that moving through check is just the same as checking if the king is in check if you move one square, or checking if the
    ##king is in check if you actually do the castrel. Makes the coding easier since it just breaks it down into these two cases.
    def can_castle(self):
        return self.can_castle
    
    def is_valid_move(self, board, ghost_board, start, end):
        if start == end:
            return False #Preventing moving to own square

        #Check it is moving in the squares around the king, and only taking enemy pieces, and not being allowed on white pieces
        if (start[0] + 1 >= end[0]) & (start[0] - 1 <= end[0]) & (start[1] + 1 >= end[1]) & (start[1] - 1 <= end[1]):
            if board[end[1]][end[0]] != None:
                #Only take opposite colour.
                if board[end[1]][end[0]].is_white() != self.is_white():
                    return True
                else:
                    return False
            return True
        else:
            return False
        

class Queen(Piece):
    def __init__(self, colour, has_moved = False):
        super().__init__(colour)
        self.value = 9
        self.name = "Q"

    def is_valid_move(self, board, ghost_board, start, end):
        if start == end:
            return False #Preventing moving to own square

        return (valid_diagonal_move(board, start, end) | valid_horver_move(board, start, end))

class Rook(Piece):
    def __init__(self, colour, has_moved = False):
        self.value = 5
        super().__init__(colour)
        self.name = "R"
        self.has_moved = has_moved

    def is_valid_move(self, board, ghost_board, start, end):
        if start == end:
            return False #Preventing moving to own square

        return valid_horver_move(board, start, end)

class Bishop(Piece):
    def __init__(self, colour, has_moved = False):
        self.value = 3
        super().__init__(colour)
        self.name = "B"

    def is_valid_move(self, board, ghost_board, start, end):
        if start == end:
            return False #Preventing moving to own square

        return valid_diagonal_move(board, start, end)

class Knight(Piece):
    def __init__(self, colour, has_moved = False):
        self.value = 3
        super().__init__(colour)
        self.name = "N"

    def is_valid_move(self, board, ghost_board, start, end):
        if start == end:
            return False #Preventing moving to own square

        return valid_knight_move(board, start, end)

class Pawn(Piece):
    #TODO: #3 Implement promotion.
    def __init__(self, colour, has_moved = False):
        self.value = 1
        super().__init__(colour)
        self.name = "P"
        self.has_moved = has_moved

    def is_valid_move(self, board, ghost_board, start, end):
        if start == end:
            return False #Preventing moving to own square
        if self.is_white():
            plus = - 1
        else:
            plus = 1
        #Can the pawn move forward one square.
        if (end[0] == start[0]) & (end[1] == start[1] + plus) & (board[end[1]][end[0]] == None):
            return True
        #Can the pawn move forward two squares.
        elif (end[0] == start[0]) & (end[1] == start[1] + 2*plus) & (board[end[1]][end[0]] == None) & (board[end[1] - plus][end[0]] == None) & (self.has_moved == False):
            return True
        elif (abs(end[0] - start[0]) == 1) & (end[1] == start[1] + plus) & (board[end[1]][end[0]] != None):
            if board[end[1]][end[0]].is_white() != self.is_white():
                return True
            else:
                return False
        #The en passent clause
        elif (abs(end[0] - start[0]) == 1) & (end[1] == start[1] + plus) & (board[end[1]][end[0]] == None) & (ghost_board[end[1]][end[0]] != None):
            return True
        else:
            return False

class GhostPawn(Piece):
    def __init__(self, colour, has_moved = False):
        self.value = 0
        super().__init__(colour)
        self.name = " "

    def is_valid_move():
        return False