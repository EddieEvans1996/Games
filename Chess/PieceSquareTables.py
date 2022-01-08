#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Stores Piece Square Tables for early and late game.
#Initial tables used taken from 'https://www.chessprogramming.org/Simplified_Evaluation_Function'
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

pawn_table = [[0,  0,  0,  0,  0,  0,  0,  0],
            [50, 50, 50, 50, 50, 50, 50, 50],
            [10, 10, 20, 30, 30, 20, 10, 10],
            [ 5,  5, 10, 25, 25, 10,  5,  5],
            [ 0,  0,  0, 20, 20,  0,  0,  0],
            [ 5, -5,-10,  0,  0,-10, -5,  5],
            [ 5, 10, 10,-20,-20, 10, 10,  5],
            [ 0,  0,  0,  0,  0,  0,  0,  0]]

knight_table = [[-50,-40,-30,-30,-30,-30,-40,-50],
            [-40,-20,  0,  0,  0,  0,-20,-40],
            [-30,  0, 10, 15, 15, 10,  0,-30],
            [-30,  5, 15, 20, 20, 15,  5,-30],
            [-30,  0, 15, 20, 20, 15,  0,-30],
            [-30,  5, 10, 15, 15, 10,  5,-30],
            [-40,-20,  0,  5,  5,  0,-20,-40],
            [-50,-40,-30,-30,-30,-30,-40,-50]]

bishop_table = [[-20,-10,-10,-10,-10,-10,-10,-20],
            [-10,  0,  0,  0,  0,  0,  0,-10],
            [-10,  0,  5, 10, 10,  5,  0,-10],
            [-10,  5,  5, 10, 10,  5,  5,-10],
            [-10,  0, 10, 10, 10, 10,  0,-10],
            [-10, 10, 10, 10, 10, 10, 10,-10],
            [-10,  5,  0,  0,  0,  0,  5,-10],
            [-20,-10,-10,-10,-10,-10,-10,-20]]

rook_table = [[0,  0,  0,  0,  0,  0,  0,  0],
            [5, 10, 10, 10, 10, 10, 10,  5],
            [-5,  0,  0,  0,  0,  0,  0, -5],
            [-5,  0,  0,  0,  0,  0,  0, -5],
            [-5,  0,  0,  0,  0,  0,  0, -5],
            [-5,  0,  0,  0,  0,  0,  0, -5],
            [-5,  0,  0,  0,  0,  0,  0, -5],
            [0,  0,  0,  5,  5,  0,  0,  0]]

queen_table = [[-20,-10,-10, -5, -5,-10,-10,-20],
            [-10,  0,  0,  0,  0,  0,  0,-10],
            [-10,  0,  5,  5,  5,  5,  0,-10],
            [ -5,  0,  5,  5,  5,  5,  0, -5],
            [  0,  0,  5,  5,  5,  5,  0, -5],
            [-10,  5,  5,  5,  5,  5,  0,-10],
            [-10,  0,  5,  0,  0,  0,  0,-10],
            [-20,-10,-10, -5, -5,-10,-10,-20]]

king_midgame_table = [[-30,-40,-40,-50,-50,-40,-40,-30],
                [-30,-40,-40,-50,-50,-40,-40,-30],
                [-30,-40,-40,-50,-50,-40,-40,-30],
                [-30,-40,-40,-50,-50,-40,-40,-30],
                [-20,-30,-30,-40,-40,-30,-30,-20],
                [-10,-20,-20,-20,-20,-20,-20,-10],
                [20, 20,  0,  0,  0,  0, 20, 20],
                [20, 30, 10,  0,  0, 10, 30, 20]]

king_endgame_table = [[-50,-40,-30,-20,-20,-30,-40,-50],
                    [-30,-20,-10,  0,  0,-10,-20,-30],
                    [-30,-10, 20, 30, 30, 20,-10,-30],
                    [-30,-10, 30, 40, 40, 30,-10,-30],
                    [-30,-10, 30, 40, 40, 30,-10,-30],
                    [-30,-10, 20, 30, 30, 20,-10,-30],
                    [-30,-30,  0,  0,  0,  0,-30,-30],
                    [-50,-30,-30,-30,-30,-30,-30,-50]]

def flip_table(table):
    return table[::-1]

def get_tablesquare_value(board, fen):
    score = 0
    for i in range(0,8):
        for j in range(0,8):
            if board[j][i] != None:
                match board[j][i].name:
                    case 'K':
                        if (fen.count("Q") == 0) & (fen.count("q") == 0):
                            if board[j][i].is_white():
                                score += king_endgame_table[j][i]
                            else:
                                score -= flip_table(king_endgame_table)[j][i]
                        else:
                            if board[j][i].is_white():
                                score += king_midgame_table[j][i]
                            else:
                                score -= flip_table(king_midgame_table)[j][i]
                    case 'Q':
                        if board[j][i].is_white():
                            score += queen_table[j][i]
                        else:
                            score -= flip_table(queen_table)[j][i]
                    case 'R':
                        if board[j][i].is_white():
                            score += rook_table[j][i]
                        else:
                            score -= flip_table(rook_table)[j][i]
                    case 'B':
                        if board[j][i].is_white():
                            score += bishop_table[j][i]
                        else:
                            score -= flip_table(bishop_table)[j][i]
                    case 'N':
                        if board[j][i].is_white():
                            score += knight_table[j][i]
                        else:
                            score -= flip_table(knight_table)[j][i]
                    case 'P':
                        if board[j][i].is_white():
                            score += pawn_table[j][i]
                        else:
                            score -= flip_table(pawn_table)[j][i]
    return score