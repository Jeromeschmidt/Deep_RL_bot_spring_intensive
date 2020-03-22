
class Board():
    def __init__(self, board=None):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        if board != None:
            self.board = board

    def show_board(self):
        print("-------------")
        print("   " + "0" + " | " + "1" + " | " + "2")
        print("*************")
        for i in range(len(self.board)):
            print(str(i) + "* "+ str(self.board[i][0]) + " | " + str(self.board[i][1]) + " | " + str(self.board[i][2]))
            # print("_" + " | " + "_" + " | " + "_")

    def get_position(self, loc):
        if self.board[loc[0]][loc[1]] is " ":
            return True
        return False

    def get_open_positions(self):
        open = list()
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == " ":
                    open.append((i, j))
        return open

    def place_X(self, loc):
        self.board[loc[0]][loc[1]] = "X"

    def place_O(self, loc):
        self.board[loc[0]][loc[1]] = "O"

    def undo_move(self, loc):
        self.board[loc[0]][loc[1]] = " "

    def check_win(self):
        #check row win
        for i in range(len(self.board)):
            if ((self.board[i][0] == self.board[i][1]) and (self.board[i][1] == self.board[i][2]) and (self.board[i][0] != " ")):
                return (True, self.board[i][0])
        #check column win
        for i in range(len(self.board)):
            if ((self.board[0][i] == self.board[1][i]) and (self.board[1][i] == self.board[2][i]) and (self.board[0][i] != " ")):
                return (True, self.board[0][i])
        #check diagonal win
        if ((self.board[0][0] == self.board[1][1]) and (self.board[1][1] == self.board[2][2]) and (self.board[0][0] != " ")):
            return (True, self.board[0][0])
        if ((self.board[0][2] == self.board[1][1]) and (self.board[1][1] == self.board[2][0]) and (self.board[0][2] != " ")):
            return (True, self.board[0][2])
        if len(self.get_open_positions()) == 0:
            #draw
            return (True, "Draw")
        return (False, None)

class Game():
    def __init__(self):
        self.board = Board()
        self.bot = Bot()

    def play(self):
        print("Indexes start at 0!")
        while self.board.check_win()[0] is False:
            self.player_X_turn()
            self.board.show_board()
            if self.board.check_win()[0] is False:
                self.player_O_turn()
                self.board.show_board()
        if self.board.check_win()[1] == "Draw":
            print("It's a draw!")
        else:
            print(str(self.board.check_win()[1]) + " has won!")

    def player_X_turn(self):
        move = self.get_move()
        self.board.place_X(move)

    def player_O_turn(self):
        ## will use this for minimax player
        # move = self.get_move()
        move = self.bot.play_move(self.board)
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

class Bot:

    def minimax(self, board, isMaxPlayer):
        if ((board.check_win()[0] is True) and (board.check_win()[1] == "X")):
            return -1
        elif((board.check_win()[0] is True) and (board.check_win()[1] == "O")):
            return 1
        elif(board.check_win()[0] is True and board.check_win()[1] == "Draw"):
            return 0

        open_moves = board.get_open_positions()

        if isMaxPlayer == True:
            best_score = float("-inf")
            for move in open_moves:
                board.place_O(move)
                score = self.minimax(board, not isMaxPlayer)
                board.undo_move(move)
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for move in open_moves:
                board.place_X(move)
                score = self.minimax(board, not isMaxPlayer)
                board.undo_move(move)
                best_score = min(score, best_score)
            return best_score

    def find_move(self, board):
        best_score = float("-inf")
        best_move = None

        open_moves = board.get_open_positions()

        for move in open_moves:
            board.place_O(move)
            score = self.minimax(board, False)
            board.undo_move(move)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def play_move(self, board):
        return self.find_move(board)
