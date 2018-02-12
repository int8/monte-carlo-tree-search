class PlayerWithOpponent:
    def __init__(self, move_value, game_result_winning_value, game_result_draw_value, game_result_losing_value):
        self.move_value = move_value
        self.game_result_winning_value = game_result_winning_value
        self.game_result_draw_value = game_result_draw_value
        self.game_result_losing_value = game_result_losing_value

    def define_opponent(self, opponent):
        self.opponent = opponent
