class Bot:

    def minimax(self, board, isMaxPlayer):
        if isMaxPlayer == True and board.check_win() == True:
            return -1
        elif(isMaxPlayer != True and board.check_win() == True):
            return 1
        # elif(board.check_win() is "Draw"):
        #     return 0

        moves = dict()
        open_moves = board.get_open_positions()
        print(open_moves)
        board.show_board()

        if isMaxPlayer == True:
            best_score = float("-inf")
            for move in open_moves:
                board.place_O(move)
                score = self.minimax(board, not isMaxPlayer)
                board.undo_move(move)
                moves[score] = move
                print(moves.keys())
            return moves[max(moves.keys())]
        else:
            best_score = float("inf")
            for move in open_moves:
                board.place_X(move)
                score = self.minimax(board, not isMaxPlayer)
                board.undo_move(move)
                moves[score] = move
            return moves[min(moves.keys())]


    def find_move(self, board):
        self.minimax(board, True)

    def play_move(self, board):
        return self.find_move(board)
