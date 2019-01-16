from mcts.nodes import TwoPlayersGameMonteCarloTreeSearchNode
from mcts.search import MonteCarloTreeSearch
from games.tictactoe import TicTacToeGameState
import numpy as np

def test_if_terminal_state_works():
    random_full_board = np.ones(9)  # initialise
    random_full_board[np.random.choice(range(8), 4, replace=False)] = -1
    test_state = TicTacToeGameState(random_full_board.reshape((3, 3)))
    test_search = MonteCarloTreeSearch(
        TwoPlayersGameMonteCarloTreeSearchNode(test_state, parent=None))
    assert test_search.root.is_terminal_node(), 'Root should be terminal'
    #  Call for next action, this should just say game it's over
    assert isinstance(test_search.best_action(100),
        TwoPlayersGameMonteCarloTreeSearchNode), 'Unexpected best action'
