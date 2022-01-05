#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Responsible for game logic.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import Board

class Chess():
    def __init__(self):
        self.board = Board.Board()


def translate(coord):

    try:
        file = coord[0]
        rank = coord[1]
        dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f':5, 'g':6, 'h':7}

        rank = int(rank)
        if rank < 1 or rank > 8:
            return None
        else:
            return (dict[file], 8 - rank)
    except:
        return None

def main():
    chess = Chess()
    start = ""
    end = ""
    chess.board.print_board()
    while (True):
        start = input("Start: ")
        ###TEMPORARY SOLUTION TO QUITTING THE GAME
        if start == "quit":
            quit()

        end = input("End: ")

        ###TEMPORARY SOLUTION TO QUITTING THE GAME
        if end == "quit":
            quit()

        start = translate(start)
        end = translate(end)

        if start == None or end == None:
            print("Not a valid start or end entry.")
            continue
        
        if (chess.board.valid_move(chess.board.board, start, end) == True):
            if (chess.board.check_self_discovery(start, end) == False):
                chess.board.move(start, end)
                chess.board.white_to_move = not chess.board.white_to_move
        else:
            continue

        chess.board.print_board()

if __name__ == "__main__":
    main()