import numpy as np
from mctspy.games.examples.tictactoe import TicTacToeGameState, TicTacToeMove

class Connect4GameState(TicTacToeGameState):

    def is_move_legal(self, move):
        # check if correct player moves
        if move.value != self.next_to_move:
            return False

        # check if inside the board on x-axis
        x_in_range = (0 <= move.x_coordinate < self.board_size)
        if not x_in_range:
            return False

        # check if inside the board on y-axis
        y_in_range = (0 <= move.y_coordinate < self.board_size)
        if not y_in_range:
            return False

        # finally check if board field not occupied yet
        return self.board[move.x_coordinate, move.y_coordinate] == 0 and (move.y_coordinate == 0 or self.board[move.x_coordinate, move.y_coordinate-1] != 0)

    def get_legal_actions(self):
        indices = np.where(np.count_nonzero(self.board,axis=1) != self.board_size)[0]
        # print(indices)
        return [
            TicTacToeMove(i, np.count_nonzero(self.board[i,:]), self.next_to_move)
            for i in indices
        ]
