#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#An AI which maximises a very simple evaluation score (based on material and piece square tables)
#in position after making a single move.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import MoveFinder
import Evaluation
import copy

class MinMaxAI:
    def __init__(self):
        depth = ""
        valid = False
        while (not valid):
            depth = input("What depth would you like the AI to search? ")
            try:
                depth = int(depth)
                if (depth in [1,2,3,4]):
                    valid = True
            except:
                print("Not a valid input. Please input 1,2,3 or 4.")
        self.depth = depth
        self.evaluator = Evaluation.Evaluator("simple")


    def move(self, board): #THIS WILL BE RENAMED SINCE THIS IS CURRENTLY ONLY A SINGLE DEPTH SEARCH. JUST FOR TESTING.
        #Performs a one deep minmax search.
        movelist = MoveFinder.move_finder(board)
        colour = board.board[movelist[0][0][1]][movelist[0][0][0]].is_white()
        colour_multiplier = 1 if colour else -1
        scores = []
        for i in movelist:
            next_scores = []
            workingboard = copy.deepcopy(board)
            workingboard.move(i[0], i[1])
            workingboard.white_to_move = not workingboard.white_to_move
            if workingboard.check_for_mate():
                return i

            next_movelist = MoveFinder.move_finder(workingboard)

            for j in next_movelist:
                next_workingboard = copy.deepcopy(workingboard)
                next_workingboard.move(j[0],j[1])
                next_workingboard.white_to_move = not next_workingboard.white_to_move
                if next_workingboard.check_for_mate():
                    next_scores.append(-99999 * colour_multiplier)
                else:
                    next_scores.append(self.evaluator.evaluate_board(next_workingboard.board))
            scores.append(min([score * colour_multiplier for score in next_scores]))
        print(movelist)
        print(scores)

        return movelist[scores.index(max(scores))]

