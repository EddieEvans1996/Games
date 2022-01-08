#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Provides chess with the AI moves. This page is not itself an AI.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import RandomAI

def get_list_of_AI():
    return ["random"]

class MoveGenerator():
    def __init__(self, AI_choice):
        match AI_choice:
            case "random":
                self.AI = RandomAI.RandomAI()

    def move(self, board):
        [start, end] = self.AI.move(board)
        board.move(start, end)