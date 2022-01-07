#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Responsible for game logic.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import Board
import GameLog

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
    gamelog = GameLog.GameLog()
    gamelog.append_starting_position(chess.board.board)
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
                gamelog.update_gamelog(chess.board.board, chess.board.reset_halfmove_clock)
        else:
            continue
        
        chess.board.print_board()

        if chess.board.check_for_mate():
            if chess.board.white_to_move:
                message = "Checkmate. Black wins."
            else:
                message = "Checkmate. White wins."

            print(message)
            while (True):
                play_again = input("Play again? (Y/N) ")
                if play_again == "Y":
                    chess = Chess()
                    gamelog = GameLog.GameLog()
                    start = ""
                    end = ""
                    chess.board.print_board()
                    break
                elif play_again == "N":
                    quit()
                else:
                    continue

        if (gamelog.check_50_move_rule() | gamelog.check_for_repetition() | chess.board.check_for_stalemate()):
            print("A draw.")
            while (True):
                play_again = input("Play again? (Y/N) ")
                if play_again == "Y":
                    chess = Chess()
                    gamelog = GameLog.GameLog()
                    start = ""
                    end = ""
                    chess.board.print_board()
                    break
                elif play_again == "N":
                    quit()
                else:
                    continue

if __name__ == "__main__":
    main()