
class Board():
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def show_board(self):
        for i in range(len(self.board)):
            print(str(self.board[i][0]) + " | " + str(self.board[i][1]) + " | " + str(self.board[i][2]))
            # print("_" + " | " + "_" + " | " + "_")

    def get_position(self, loc):
        if self.board[loc[0]][loc[1]] is " ":
            return True
        return False

    def place_X(self, loc):
        self.board[loc[0]][loc[1]] = "X"

    def place_O(self, loc):
        self.board[loc[0]][loc[1]] = "O"

    def check_win(self):
        #check row win
        for i in range(len(self.board)):
            if ((self.board[i][0] == self.board[i][1]) and (self.board[i][1] == self.board[i][2]) and (self.board[i][0] != " ")):
                return True
        #check column win
        for i in range(len(self.board)):
            if ((self.board[0][i] == self.board[1][i]) and (self.board[1][i] == self.board[2][i]) and (self.board[0][i] != " ")):
                return True
        #check diagonal win
        if ((self.board[0][0] == self.board[1][1]) and (self.board[1][1] == self.board[2][2]) and (self.board[0][0] != " ")):
            return True
        if ((self.board[0][2] == self.board[1][1]) and (self.board[1][1] == self.board[2][0]) and (self.board[0][2] != " ")):
            return True
        return False

class Game():
    def __init__(self):
        self.board = Board()

    def play(self):
        print("Indexes start at 0!")
        while self.board.check_win() is False:
            self.player_X_turn()
            self.board.show_board()
            if self.board.check_win() is False:
                self.player_O_turn()
                self.board.show_board()

    def player_X_turn(self):
        move = self.get_move()
        self.board.place_X(move)

    def player_O_turn(self):
        move = self.get_move()
        self.board.place_O(move)

    def is_index_valid(self, index):
        if ((index == 0) or (index == 1) or (index == 2)):
            return True
        return False

    def get_move(self):
        row_num = int(input("What row: "))
        while self.is_index_valid(row_num) is False:
            print("Please enter a a valid row index. ")
            row_num = int(input("What row: "))

        col_num = int(input("What column: "))
        while self.is_index_valid(col_num) is False:
            print("Please enter a a valid column index. ")
            col_num = int(input("What column: "))

        if self.board.get_position((row_num, col_num)):
            return ((row_num, col_num))
        else:
            print("Please choose an open space!")
            return self.get_move()
