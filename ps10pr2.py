#
# ps10pr2.py  (Problem Set 10, Problem 2)
#
# A Connect-Four Player class 
#  

from ps10pr1 import Board
import random

# write your class below
class Player:
    def __init__(self,checker):
        """constructs a new Player object by initializing checker and number of moves"""
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """returns a string representing a Player object. The string returned should indicate which checker the Player object is using"""
        s = "Player " + str(self.checker)
        return s

    def opponent_checker(self):
        """returns a one-character string representing the checker of the Player object’s opponent"""
        if self.checker == "X":
            return "O"
        else:
            return "X"

    def next_move(self,board):
        """returns a one-character string representing the checker of the Player object’s opponent"""
        col = -1
        while  board.can_add_to(col) == False:
            col = int(input("Enter a column: "))
            if board.can_add_to(col) == False:
                print("Try again!")
        self.num_moves += 1
        return col

class RandomPlayer(Player):
    def next_move(self, board):
        """overrides (i.e., replaces) the next_move method that is inherited from Player. Rather than asking the user for the next move, this version of next_move should choose at random from the columns in the specified board that are not yet full, and return the index of that randomly selected column"""
        cols = []
        for col in range(board.width):
            if board.can_add_to(col) == True:
                cols += [col]
        select_col = random.choice(cols)
        self.num_moves += 1
        return select_col


        
        
