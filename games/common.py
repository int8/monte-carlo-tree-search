class TwoPlayersGameState:

    def __init__(self, state, player_to_move):
        self.state = state
        self.player_to_move = player_to_move

    def game_result(self):
        raise NotImplemented("Implement game_result function")

    def is_game_over(self):
        raise NotImplemented("Implement is_game_over function")

    def move(self, action):
        raise NotImplemented("Implement move function")

    def get_legal_actions(self):
        raise NotImplemented("Implement get_legal_actions function")

    def player_to_move_wins(self):
        self.game_result() == self.player_to_move.winning_value

    def player_to_move_loses(self):
        self.game_result() == self.player_to_move.losing_value

    def draw(self):
        self.game_result() == self.player_to_move.draw_value


class Action:
    pass
