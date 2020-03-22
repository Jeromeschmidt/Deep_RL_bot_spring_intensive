
class Board():
    def __init__(self):
        self.board = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]]

    def show_board(self):
        for i in range(len(self.board)):
            print(str(self.board[i][0]) + " | " + str(self.board[i][1]) + " | " + str(self.board[i][2]) + " | " + str(self.board[i][3]) + " | " + str(self.board[i][4]) + " | " + str(self.board[i][5]) + " | ")
            # print("_" + " | " + "_" + " | " + "_")

    def get_position(self, col_num):
        if self.board[0][col_num] is " ":
            return True
        return False

    def get_height(self, col_num):
        for i in range(len(self.board[0])+1):
            if self.board[i][col_num] != " ":
                return i-1
        return i

    def place_X(self, col_num):
        row_num = self.get_height(col_num)
        self.board[row_num][col_num] = "X"

    def place_O(self, col_num):
        row_num = self.get_height(col_num)
        self.board[row_num][col_num] = "O"

    def check_win(self):
        #check column win
        for i in range(len(self.board)-4, 0, -1):
            for j in range(len(self.board[i])):
                if ((self.board[i][j] == self.board[i+1][j]) and (self.board[i+1][j] == self.board[i+2][j]) and (self.board[i+2][j] == self.board[i+3][j]) and (self.board[i][j] != " ")):
                    return True
        #check row win
        for i in range(len(self.board)):
            for j in range(len(self.board[i])-4):
                if ((self.board[i][j] == self.board[i][j+1]) and (self.board[i][j+1] == self.board[i][j+2]) and (self.board[i][j+2] == self.board[i][j+3]) and (self.board[i][j] != " ")):
                    return True
        #check diagonal win
        for i in range(len(self.board)-3):
            for j in range(3, len(self.board[i])):
            ##/
                if ((self.board[i][j] == self.board[i+1][j-1]) and (self.board[i+1][j-1] == self.board[i+2][j-2]) and (self.board[i+2][j-2] == self.board[i+3][j-3]) and (self.board[i][j] != " ")):
                    return True
        for i in range(len(self.board)-3):
            for j in range(len(self.board[i])-3):
            ##\
                if((self.board[i][j] == self.board[i+1][j+1]) and (self.board[i+1][j+1] == self.board[i+2][j+2]) and (self.board[i+2][j+2] == self.board[i+3][j+3]) and (self.board[i][j] != " ")):
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
        if ((index == 0) or (index == 1) or (index == 2) or (index == 3) or (index == 4) or (index == 5)):
            return True
        return False

    def get_move(self):
        col_num = int(input("What column: "))
        while self.is_index_valid(col_num) is False:
            print("Please enter a a valid column index. ")
            col_num = int(input("What column: "))

        if self.board.get_position(col_num):
            return col_num
        else:
            print("Please choose an open column!")
            return self.get_move()
