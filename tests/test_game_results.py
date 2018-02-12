from games.tictactoe import TicTacToeState
from games.players import PlayerWithOpponent
import numpy as np

def test_if_initial_state_draw():
    state = TicTacToeState(np.zeros((3,3)), PlayerWithOpponent(move_value = 1, game_result_winning_value = 1, game_result_losing_value = 0, game_result_draw_value = 0.5))
    assert state.game_result() == 0.5

def test_if_1_wins_diagonal_case1():
    gamestate = np.zeros((3,3))
    gamestate[0,0] = 1
    gamestate[1,1] = 1
    gamestate[2,2] = 1

    state = TicTacToeState(gamestate, PlayerWithOpponent(move_value = 1, game_result_winning_value = 1, game_result_losing_value = 0, game_result_draw_value = 0.5))
    assert state.game_result() == 1

def test_if_1_wins_diagonal_case2():
    gamestate = np.zeros((3,3))
    gamestate[0,2] = 1
    gamestate[1,1] = 1
    gamestate[2,0] = 1

    state = TicTacToeState(gamestate, PlayerWithOpponent(move_value = 1, game_result_winning_value = 1, game_result_losing_value = 0, game_result_draw_value = 0.5))
    assert state.game_result() == 1

def test_if_0_wins_diagonal_case1():
    gamestate = np.zeros((3,3))
    gamestate[0,2] = -1
    gamestate[1,1] = -1
    gamestate[2,0] = -1

    state = TicTacToeState(gamestate, PlayerWithOpponent(move_value = 1, game_result_winning_value = 1, game_result_losing_value = 0, game_result_draw_value = 0.5))
    assert state.game_result() == 0

def test_if_0_wins_diagonal_case2():
    gamestate = np.zeros((3,3))
    gamestate[0,0] = -1
    gamestate[1,1] = -1
    gamestate[2,2] = -1

    state = TicTacToeState(gamestate, PlayerWithOpponent(move_value = 1, game_result_winning_value = 1, game_result_losing_value = 0, game_result_draw_value = 0.5))
    assert state.game_result() == 0


def test_if_draw_diagonal_case1():
    gamestate = np.zeros((3,3))
    gamestate[0,0] = -1
    gamestate[1,1] = 1
    gamestate[2,2] = -1

    state = TicTacToeState(gamestate, PlayerWithOpponent(move_value = 1, game_result_winning_value = 1, game_result_losing_value = 0, game_result_draw_value = 0.5))
    assert state.game_result() == 0.5

def test_if_draw_diagonal_case2():
    gamestate = np.zeros((3,3))
    gamestate[0,0] = 1
    gamestate[1,1] = 1
    gamestate[2,2] = -1

    state = TicTacToeState(gamestate, PlayerWithOpponent(move_value = 1, game_result_winning_value = 1, game_result_losing_value = 0, game_result_draw_value = 0.5))
    assert state.game_result() == 0.5

def test_if_draw_other_diagonal_case1():
    gamestate = np.zeros((3,3))
    gamestate[0,2] = 1
    gamestate[1,1] = 1
    gamestate[2,0] = -1

    state = TicTacToeState(gamestate, PlayerWithOpponent(move_value = 1, game_result_winning_value = 1, game_result_losing_value = 0, game_result_draw_value = 0.5))
    assert state.game_result() == 0.5

def test_if_draw_other_diagonal_case2():
    gamestate = np.zeros((3,3))
    gamestate[0,2] = -1
    gamestate[1,1] = 1
    gamestate[2,0] = -1

    state = TicTacToeState(gamestate, PlayerWithOpponent(move_value = 1, game_result_winning_value = 1, game_result_losing_value = 0, game_result_draw_value = 0.5))
    assert state.game_result() == 0.5


def test_if_0_wins_all_1_but_diagonal_case1():
    gamestate = np.ones((3,3))
    gamestate[0,2] = -1
    gamestate[1,1] = -1
    gamestate[2,0] = -1

    state = TicTacToeState(gamestate, PlayerWithOpponent(move_value = 1, game_result_winning_value = 1, game_result_losing_value = 0, game_result_draw_value = 0.5))
    assert state.game_result() == 0


def test_if_0_wins_all_1_but_diagonal_case2():
    gamestate = np.ones((3,3))
    gamestate[0,0] = -1
    gamestate[1,1] = -1
    gamestate[2,2] = -1

    state = TicTacToeState(gamestate, PlayerWithOpponent(move_value = 1, game_result_winning_value = 1, game_result_losing_value = 0, game_result_draw_value = 0.5))
    assert state.game_result() == 0

def test_if_1_wins_all_1_but_diagonal_case1():
    gamestate = -np.ones((3,3))
    gamestate[0,2] = 1
    gamestate[1,1] = 1
    gamestate[2,0] = 1

    state = TicTacToeState(gamestate, PlayerWithOpponent(move_value = 1, game_result_winning_value = 1, game_result_losing_value = 0, game_result_draw_value = 0.5))
    assert state.game_result() == 1

def test_if_1_wins_all_1_but_diagonal_case2():
    gamestate = -np.ones((3,3))
    gamestate[0,0] = 1
    gamestate[1,1] = 1
    gamestate[2,2] = 1

    state = TicTacToeState(gamestate, PlayerWithOpponent(move_value = 1, game_result_winning_value = 1, game_result_losing_value = 0, game_result_draw_value = 0.5))
    assert state.game_result() == 1
