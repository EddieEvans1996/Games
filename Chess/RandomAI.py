#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#AI producing random moves.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import MoveFinder
import random

class RandomAI():
    def __init__(self):
        print("Random AI initiated.")

    def move(self, board):
        possible_moves = MoveFinder.move_finder(board)
        try:
            return random.choice(possible_moves)
        except:
            print("Something has gone wrong! There should be moves to choose from :)")
