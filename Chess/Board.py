#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Responsible for GUI and entertaining the user!
#To start, this will simply be a command line.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import Piece

class Board():
    def __init__(self):
        self.white_to_move = True
        self.board = [[None for i in range(0,8)] for j in range(0,8)]

        #Setting up the white pieces
        self.board[7][0] = Piece.Rook('w')
        self.board[7][1] = Piece.Knight('w')
        self.board[7][2] = Piece.Bishop('w')
        self.board[7][3] = Piece.Queen('w')
        self.board[7][4] = Piece.King('w')
        self.board[7][5] = Piece.Bishop('w')
        self.board[7][6] = Piece.Knight('w')
        self.board[7][7] = Piece.Rook('w')
        for i in range(0,8):
            self.board[6][i] = Piece.Pawn('w')

        #Setting up the black pieces
        self.board[0][0] = Piece.Rook('b')
        self.board[0][1] = Piece.Knight('b')
        self.board[0][2] = Piece.Bishop('b')
        self.board[0][3] = Piece.Queen('b')
        self.board[0][4] = Piece.King('b')
        self.board[0][5] = Piece.Bishop('b')
        self.board[0][6] = Piece.Knight('b')
        self.board[0][7] = Piece.Rook('b')
        for i in range(0,8):
            self.board[1][i] = Piece.Pawn('b')


    def print_board(self):
        string = ""
        for i in range(0,21):
            string += "*"
        print(string)
        print(string)
        for i in range(0,8):
            string = "**|"
            for j in self.board[i]:
                if j == None:
                    string += " |"
                else:
                    string = string + str(j) + "|"
            string += "**"
            print(string)
        string = ""
        for i in range(0,21):
            string += "*"
        print(string)
        print(string)
        

    def valid_move(self,start,end):
        if self.board[start[1]][start[0]] == None:
            return False
        elif self.board[start[1]][start[0]].is_valid_move(self.board, start, end) == False:
            return False
        else:
            return True


    def move(self, start, end):
        self.board[end[1]][end[0]] = self.board[start[1]][start[0]]
        self.board[start[1]][start[0]] = None