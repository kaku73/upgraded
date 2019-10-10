
class Board:
      def __init__(self,height,width):
            """creates Board class with three attribbutes: height, width and slots of the board"""
            self.height = height
            self.width = width
            self.slots = [[' '] * self.width for row in range(self.height)]

      def __repr__(self):
            """ Returns a string representation for a Board object."""
            s = ""
            label = ""
            for row in range(self.height):
                  s += "|"
                  for col in range(self.width):
                        s += self.slots[row][col] + "|"
                  s += "\n"
            s += "-" * (self.width *2 + 1)
            s += "\n"
            for i in range(self.width):
                  label = i % 10
                  s += " " + str(label)
            return s

      def add_checker(self,checker,col):
            """ adds a checker (either X or O) to a specified column"""
            assert(checker == 'X' or checker == 'O')
            assert(0 <= col < self.width)
            for row in range(self.height):
                  if self.slots[self.height - row - 1][col] == " ":
                        self.slots[self.height - row - 1][col] = checker
                        break

      def reset(self):
            """reset the Board object on which it is called by setting all slots to contain a space character"""
            self.slots = [[' '] * self.width for row in range(self.height)]

      def add_checkers(self,colnums):
            """takes in a string of column numbers and places alternating checkers in those columns of the called Board object, starting with 'X'."""
            checker = "X"
            for col_str in colnums:
                  col = int(col_str)
                  if 0 <= col < self.width:
                        self.add_checker(checker,col)
                  if checker == "X":
                        checker = "O"
                  else:
                        checker = "X"

      def can_add_to(self,col):
            """returns True if it is valid to place a checker in the column col on the calling Board object. Otherwise, it should return False."""
            if col < 0:
                  return False
            elif col >= self.width:
                  return False
            elif self.slots[0][col] != " ":
                  return False
            else:
                  return True

      def is_full(self):
            """returns True if the called Board object is completely full of checkers, and returns False otherwise."""
            for col in range(self.width):
                  if self.can_add_to(col) == True:
                        return False
            return True

      def remove_checker(self, col):
            """removes the top checker from column col of the called Board object. If the column is empty, then the method should do nothing"""
            for row in range(self.height):
                  if self.slots[row][col] == "X" or self.slots[row][col] == "O":
                        self.slots[row][col] = " "
                        break

      def is_win_for(self,checker):
            """accepts a parameter checker that is either 'X' or 'O', and returns True if there are four consecutive slots containing checker on the board. Otherwise, it should return False."""
            assert(checker == 'X' or checker == 'O')
            if self.is_horizontal_win(checker) or self.is_vertical_win(checker) or self.is_down_diagonal_win(checker) or self.is_up_diagonal_win(checker):
                  return True
            else:
                  return False
      #Helper for is_win_for function
      def is_horizontal_win(self, checker):
            """Checks for a horizontal wins"""
            for row in range(self.height):
                  for col in range(self.width -3):
                        if self.slots[row][col] == checker and self.slots[row][col+1] == checker and self.slots[row][col+2] == checker and self.slots[row][col+3] == checker:
                              return True
            return False

      def is_vertical_win(self, checker):
            """Checks for vertical wins"""
            for col in range(self.width):
                  for row in range(3,self.height):
                        if self.slots[row-3][col] == checker and self.slots[row-2][col] == checker and self.slots[row-1][col] == checker and self.slots[row][col] == checker:
                              return True
            return False

      def is_down_diagonal_win(self, checker):
            """Checks for down diagonal wins"""
            for row in range(self.height-3):
                  for col in range(self.width-3):
                        if self.slots[row][col] == checker and self.slots[row+1][col+1] == checker and self.slots[row+2][col+2] == checker and self.slots[row+3][col+3] == checker:
                              return True
            return False

      def is_up_diagonal_win(self, checker):
            """Checks for up diagonal wins"""
            for row in range(3,self.height):
                  for col in range(self.width-3):
                        if self.slots[row][col] == checker and self.slots[row-1][col+1] == checker and self.slots[row-2][col+2] == checker and self.slots[row-3][col+3] == checker:
                              return True
            return False

