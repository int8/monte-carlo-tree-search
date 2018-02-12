import numpy as np
from games.common import TwoPlayersGameState, Action
from games.players import PlayerWithOpponent


class TicTacToeAction(Action):
    def __init__(self, x_coordinate, y_coordinate, value):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.value = value

    def __repr__(self):
        return "x:" + str(self.x_coordinate) + " y:" + str(self.y_coordinate) + " v:" + str(self.value)

class TicTacToeState(TwoPlayersGameState):

    def __init__(self, state: np.ndarray, player_to_move : PlayerWithOpponent):
        TwoPlayersGameState.__init__(self, state, player_to_move)

    def move(self, action):
        if not self._is_action_legal(action):
            raise ValueError("action is not legal")
        new_state = np.copy(self.state)
        new_state[action.x_coordinate, action.y_coordinate] = action.value
        return TicTacToeState(new_state, self.player_to_move.opponent)

    def _is_action_legal(self, action):
        x_in_range = action.x_coordinate < 3 and action.x_coordinate >= 0
        if not x_in_range:
            return False
        y_in_range = action.y_coordinate < 3 and action.y_coordinate >= 0
        if not y_in_range:
            return False

        v_in_range = action.value == self.player_to_move.move_value
        return v_in_range

    def game_result(self):
        rowsum = np.sum(self.state,0)
        colsum = np.sum(self.state,1)
        diag1sum = self.state[0,0] + self.state[1,1] + self.state[2,2]
        diag2sum = self.state[0,2] + self.state[1,1] + self.state[2,0]

        if any(rowsum == 3) or any(colsum == 3) or diag1sum == 3 or diag2sum == 3:
            return 1
        if any(rowsum == -3) or any(colsum == -3) or diag1sum == -3 or diag2sum == -3:
            return 0
        return 0.5

    def get_legal_actions(self):
        indices = np.where(self.state == 0)
        return [TicTacToeAction(coords[0], coords[1], self.player_to_move.move_value) for coords in list(zip(indices[0], indices[1]))]
