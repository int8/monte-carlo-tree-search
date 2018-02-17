## Experimental implementation of Monte Carlo Tree Search algorithm

The purpose of this code is to create MCTS + neural-network based chess bot. So far, simple implementation of MCTS for tic-tac-toe

(code may still be buggy, not tested)


to run try:

```python

import numpy as np
from mcts.nodes import *
from mcts.search import MonteCarloTreeSearch
from games.tictactoe import TicTacToeGameState


initial_board_state = TicTacToeGameState(state = np.zeros((3,3)), next_to_move = 1)

root = TwoPlayersGameMonteCarloTreeSearchNode(state = initial_board_state, parent = None)
mcts = MonteCarloTreeSearch(root)
best_node = mcts.best_action(1000)

```
