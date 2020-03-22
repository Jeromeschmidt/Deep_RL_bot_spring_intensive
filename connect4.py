
class Board():
    def __init__(self):
        self.board = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]]

    def show_board(self):
        print("--------------------------")
        print("0" + " | " + "1" + " | " + "2" + " | " + "3" + " | " + "4" + " | " + "5")
        print("**************************")
        for i in range(len(self.board)):
            print(str(self.board[i][0]) + " | " + str(self.board[i][1]) + " | " + str(self.board[i][2]) + " | " + str(self.board[i][3]) + " | " + str(self.board[i][4]) + " | " + str(self.board[i][5]) + " | ")
            # print("_" + " | " + "_" + " | " + "_")

    def get_position(self, col_num):
        if self.board[0][col_num] is " ":
            return True
        return False

    def get_value(self, loc):
        return self.board[loc[0]][loc[1]]

    def get_open_positions(self):
        open = list()
        for i in range(len(self.board[0])):
            if self.board[0][i] == " ":
                open.append(i)
        return open

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

    def undo_move(self, col_num):
        row_num = self.get_height(col_num)+1
        self.board[row_num][col_num] = " "

    def check_win(self):
        #check column win
        for i in range(len(self.board)-3):
            for j in range(len(self.board[i])):
                if ((self.board[i][j] == self.board[i+1][j]) and (self.board[i+1][j] == self.board[i+2][j]) and (self.board[i+2][j] == self.board[i+3][j]) and (self.board[i][j] != " ")):
                    return (True, self.board[i][j])
        #check row win
        for i in range(len(self.board)):
            for j in range(len(self.board[i])-4):
                if ((self.board[i][j] == self.board[i][j+1]) and (self.board[i][j+1] == self.board[i][j+2]) and (self.board[i][j+2] == self.board[i][j+3]) and (self.board[i][j] != " ")):
                    return (True, self.board[i][j])
        #check diagonal win
        for i in range(len(self.board)-3):
            for j in range(3, len(self.board[i])):
            ##/
                if ((self.board[i][j] == self.board[i+1][j-1]) and (self.board[i+1][j-1] == self.board[i+2][j-2]) and (self.board[i+2][j-2] == self.board[i+3][j-3]) and (self.board[i][j] != " ")):
                    return (True, self.board[i][j])
        for i in range(len(self.board)-3):
            for j in range(len(self.board[i])-3):
            ##\
                if((self.board[i][j] == self.board[i+1][j+1]) and (self.board[i+1][j+1] == self.board[i+2][j+2]) and (self.board[i+2][j+2] == self.board[i+3][j+3]) and (self.board[i][j] != " ")):
                    return (True, self.board[i][j])
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

class Bot:

    def check_vertical_streak(self, x, y, board, length):
        count = 0
        for i in range(x, 5):
            if board.get_value((i,y)) == board.get_value((x,y)):
                count += 1
        if count >= length:
            return 1
        return 0

    def check_horizontal_streak(self, x, y, board, length):
        count = 0
        for i in range(x, 6):
            if board.get_value((x, i)) == board.get_value((x, y)):
                count += 1
        if count >= length:
            return 1
        return 0

    # def check_diagonal_streak(self, x, y, board, length):
    #     count = 0
    #     result = 0
    #     #\
    #     for i in range(x, 4):
    #         if board.get_value((x+i, y+i)) == board.get_value((x, y)):
    #             count += 1
    #     if count >= length:
    #         result =  1
    #
    #     count = 0
    #
    #     #/
    #     for i in range(x, 4):
    #         if board.get_value((x+i, y-i)) == board.get_value((x, y)):
    #             count += 1
    #     if count >= length:
    #         result +=  1
    #
    #     return result

    def check_streak(self, tile, board, length):
        count = 0
        for i in range(5):
            for j in range(6):
                if board.get_value((i,j)) == tile:
                    count += self.check_vertical_streak(i, j, board, length)
                    count += self.check_horizontal_streak(i, j, board, length)
                    # count += self.check_diagonal_streak(i, j, board, length)
        return count

    def evaluate_board(self, board):
        #evaluation formula adapted from: https://github.com/prakhar10/Connect4
        bot_4 = self.check_streak("O", board, 4)
        bot_3 = self.check_streak("O", board, 3)
        bot_2 = self.check_streak("O", board, 2)
        human_4 = self.check_streak("X", board, 4)
        human_3 = self.check_streak("X", board, 3)
        human_2 = self.check_streak("X", board, 2)
        return (((bot_4*10) + (bot_3*5)+ (bot_2*2)) - ((human_4*10) + (human_3*5)+ (human_2*2)))

    def minimax(self, board, isMaxPlayer, alpha, beta, depth):
        if depth == 4:
            return self.evaluate_board(board)

        if ((board.check_win()[0] is True) and (board.check_win()[1] == "X")):
            # print("-1")
            return -1
        elif((board.check_win()[0] is True) and (board.check_win()[1] == "O")):
            # print("1")
            return 1
        elif(board.check_win()[0] is True and board.check_win()[1] == "Draw"):
            # print("Draw")
            return 0

        open_moves = board.get_open_positions()

        if isMaxPlayer == True:
            best_score = float("-inf")
            for move in open_moves:
                board.place_O(move)
                score = self.minimax(board, not isMaxPlayer, alpha, beta, depth+1)
                board.undo_move(move)
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break;
                # print(best_score)
            return best_score
        else:
            best_score = float("inf")
            for move in open_moves:
                board.place_X(move)
                score = self.minimax(board, not isMaxPlayer, alpha, beta, depth+1)
                board.undo_move(move)
                best_score = min(score, best_score)
                beta = min(best_score, beta)
                if beta <= alpha:
                    break;
                # print(best_score)
            return best_score

    def find_move(self, board):
        best_score = float("-inf")
        best_move = None

        open_moves = board.get_open_positions()

        for move in open_moves:
            board.place_O(move)
            score = self.minimax(board, False, float("-inf"), float("inf"), 0)
            board.undo_move(move)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def play_move(self, board):
        return self.find_move(board)
