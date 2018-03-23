## Implementation of basic Monte Carlo Tree Search algorithm for Tic Tac Toe

This is supplementary code for [Monte Carlo Tree Search tutorial blog post here](https://int8.io/monte-carlo-tree-search-beginners-guide)

to run try:

```python

import numpy as np
from mcts.nodes import *
from mcts.search import MonteCarloTreeSearch
from games.tictactoe import TicTacToeGameState

state = np.zeros((3,3))
initial_board_state = TicTacToeGameState(state = state, next_to_move = 1)

root = TwoPlayersGameMonteCarloTreeSearchNode(state = initial_board_state, parent = None)
mcts = MonteCarloTreeSearch(root)
best_node = mcts.best_action(1000)

```
