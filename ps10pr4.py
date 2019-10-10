#
# ps10pr4.py  (Problem Set 10, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps10pr3 import *

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """constructs a new AIPlayer object"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """returns a string representing an AIPlayer object"""
        s = "Player " + str(self.checker) + " (" + self.tiebreak + ", " + str(self.lookahead) + ")" 
        return s
    
    def max_score_column(self, scores):
        """takes a list scores containing a score for each column of the board, and that returns the index of the column with the maximum score. If one or more columns are tied for the maximum score, the method should apply the called AIPlayer‘s tiebreaking strategy to break the tie."""
        max_score = max(scores)
        max_scores = []
        for i in range(len(scores)):
            if scores[i] == max_score:
                max_scores += [i]
        if self.tiebreak == "RIGHT":
            return max_scores[-1]
        elif self.tiebreak == "LEFT":
            return max_scores[0]
        else:
            return random.choice(max_scores)
    def scores_for(self, board):
        """takes a Board object board and determines the called AIPlayer‘s scores for the columns in board."""
        scores = [0 for x in range(board.width)]
        for i in range(board.width):
            if board.can_add_to(i) == False:
                scores[i] = -1
            elif board.is_win_for(self.checker) == True:
                scores[i] = 100
            elif board.is_win_for(self.opponent_checker()) == True:
                scores[i] = 0
            elif self.lookahead == 0:
                scores[i] = 50
            else:
                board.add_checker(self.checker, i)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                opp_scores = opponent.scores_for(board)
                max_opp = max(opp_scores)
                if max_opp == 0:
                    scores[i] = 100
                elif max_opp == 50:
                    scores[i] = 50
                elif max_opp == 100:
                    scores[i] = 0
                board.remove_checker(i)
        return scores

    def next_move(self, board):
        """Overrides player class' next_move. this version of next_move should return the called AIPlayer‘s judgment of its best possible move"""
        scores = self.scores_for(board)
        col_index = self.max_score_column(scores)
        self.num_moves += 1
        return col_index
