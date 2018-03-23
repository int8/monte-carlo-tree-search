class TwoPlayersGameState:

    def __init__(self, state, next_to_move):
        self.state = state
        self.next_to_move = next_to_move

    def game_result(self):
        raise NotImplemented("Implement game_result function")

    def is_game_over(self):
        raise NotImplemented("Implement is_game_over function")

    def move(self, action):
        raise NotImplemented("Implement move function")

    def get_legal_actions(self):
        raise NotImplemented("Implement get_legal_actions function")


class Action:
    pass
