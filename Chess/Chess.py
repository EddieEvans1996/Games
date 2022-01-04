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
        end = input("End: ")

        start = translate(start)
        end = translate(end)

        if start == None or end == None:
            print("Not a valid start or end entry.")
            continue
        
        if chess.board.valid_move(start,end) == True:
            chess.board.move(start,end)
        else:
            continue

        chess.board.print_board()

if __name__ == "__main__":
    main()

