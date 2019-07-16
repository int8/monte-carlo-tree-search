import numpy as np
from mctspy.games.common import TwoPlayersAbstractGameState, AbstractGameAction


class TicTacToeMove(AbstractGameAction):
    def __init__(self, x_coordinate, y_coordinate, value):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.value = value

    def __repr__(self):
        return "x:{0} y:{1} v:{2}".format(
            self.x_coordinate,
            self.y_coordinate,
            self.value
        )


class TicTacToeGameState(TwoPlayersAbstractGameState):

    x = 1
    o = -1

    def __init__(self, state, next_to_move=1):
        if len(state.shape) != 2 or state.shape[0] != state.shape[1]:
            raise ValueError("Only 2D square boards allowed")
        self.board = state
        self.board_size = state.shape[0]
        self.next_to_move = next_to_move

    @property
    def game_result(self):
        # check if game is over
        rowsum = np.sum(self.board, 0)
        colsum = np.sum(self.board, 1)
        diag_sum_tl = self.board.trace()
        diag_sum_tr = self.board[::-1].trace()

        player_one_wins = any(rowsum == self.board_size)
        player_one_wins += any(colsum == self.board_size)
        player_one_wins += (diag_sum_tl == self.board_size)
        player_one_wins += (diag_sum_tr == self.board_size)

        if player_one_wins:
            return self.x

        player_two_wins = any(rowsum == -self.board_size)
        player_two_wins += any(colsum == -self.board_size)
        player_two_wins += (diag_sum_tl == -self.board_size)
        player_two_wins += (diag_sum_tr == -self.board_size)

        if player_two_wins:
            return self.o

        if np.all(self.board != 0):
            return 0.

        # if not over - no result
        return None

    def is_game_over(self):
        return self.game_result is not None

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
        return self.board[move.x_coordinate, move.y_coordinate] == 0

    def move(self, move):
        if not self.is_move_legal(move):
            raise ValueError(
                "move {0} on board {1} is not legal". format(move, self.board)
            )
        new_board = np.copy(self.board)
        new_board[move.x_coordinate, move.y_coordinate] = move.value
        if self.next_to_move == TicTacToeGameState.x:
            next_to_move = TicTacToeGameState.o
        else:
            next_to_move = TicTacToeGameState.x

        return TicTacToeGameState(new_board, next_to_move)

    def get_legal_actions(self):
        indices = np.where(self.board == 0)
        return [
            TicTacToeMove(coords[0], coords[1], self.next_to_move)
            for coords in list(zip(indices[0], indices[1]))
        ]
