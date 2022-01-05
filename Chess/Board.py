#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Responsible for GUI and entertaining the user!
#To start, this will simply be a command line.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import Piece

class Board():
    def __init__(self):
        self.white_to_move = True
        self.board = [[None for i in range(0,8)] for j in range(0,8)]
        self.ghost_board = [[None for i in range(0,8)] for j in range(0,8)]

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
        #Ensures that a piece has been chosen.
        #Ensures that a null move (i.e. moving a piece to where it currently is) is not allowed.
        if self.board[start[1]][start[0]] == None or start == end:
            return False
        elif self.white_to_move != self.board[start[1]][start[0]].is_white():
            return False
        else:
            return self.board[start[1]][start[0]].is_valid_move(self.board, self.ghost_board, start, end)

    def check_for_check(self, temp_board):
        print("Hello.")

    def move(self, start, end):
        def en_passent_logic(start, end):
            #Updating ghost board for en passent reasons.
            self.ghost_board = [[None for i in range(0,8)] for j in range(0,8)]
            if (self.board[start[1]][start[0]].name == "P") & (abs(start[1] - end[1]) == 2):
                self.ghost_board[int((start[1] + end[1])/2)][start[0]] = Piece.GhostPawn(self.board[start[1]][start[0]].colour)

            #Some extra logic to remove the enemy pawn if we are doing en passent.
            if (self.board[start[1]][start[0]].name == "P") & (start[0] != end[0]) & (self.board[end[1]][end[0]] == None):
                self.board[end[1] + 1][end[0]] = None
                self.board[end[1] - 1][end[0]] = None #Fine to set both to none, since if ghost pawn is present, then opposite pawn has only just
                #moved, and thus both the squares above and below where were are moving to are where the pawn was and where the pawn is... i.e. we 
                #want to remove where the pawn is, and where the pawn was is empty anyway.

        def check_pawn_promotion(start, end):
            #PAWN PROMOTION Logic
            if (self.board[start[1]][start[0]].name == "P") & ((end[1] == 7) | (end[1] == 0)):
                promoted = False
                while (not promoted):
                    promote_to = input("What would you like to promote to? (Enter 'Q' for Queen, etc.) ")
                    match promote_to:
                        case "Q":
                            self.board[end[1]][end[0]] = Piece.Queen(self.board[start[1]][start[0]].colour, True)
                            promoted = True
                        case "R":
                            self.board[end[1]][end[0]] = Piece.Rook(self.board[start[1]][start[0]].colour, True)
                            promoted = True
                        case "B":
                            self.board[end[1]][end[0]] = Piece.Bishop(self.board[start[1]][start[0]].colour, True)
                            promoted = True
                        case "N":
                            self.board[end[1]][end[0]] = Piece.Knight(self.board[start[1]][start[0]].colour, True)
                            promoted = True

        en_passent_logic(start, end)
        self.board[start[1]][start[0]].has_moved = True
        self.board[end[1]][end[0]] = self.board[start[1]][start[0]]
        check_pawn_promotion(start, end)
        self.board[start[1]][start[0]] = None