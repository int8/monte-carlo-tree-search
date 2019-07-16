## mctspy : python implementation of Monte Carlo Tree Search algorithm

 
Basic python implementation of [Monte Carlo Tree Search](https://int8.io/monte-carlo-tree-search-beginners-guide) (MCTS) intended to run on small game trees. 
 

### Installation

```
pip3 install mctspy
``` 

### Running tic-tac-toe example 

to run tic-tac-toe example:

```python

import numpy as np
from mctspy.tree.nodes import TwoPlayersGameMonteCarloTreeSearchNode
from mctspy.tree.search import MonteCarloTreeSearch
from mctspy.games.examples.tictactoe import TicTacToeGameState

state = np.zeros((3,3))
initial_board_state = TicTacToeGameState(state = state, next_to_move=1)

root = TwoPlayersGameMonteCarloTreeSearchNode(state = initial_board_state)
mcts = MonteCarloTreeSearch(root)
best_node = mcts.best_action(10000)

```


### Running MCTS for your own 2 players zero-sum game 

If you want to apply MCTS for your own game, its state implementation should derive from  
`mmctspy.games.common.TwoPlayersGameState` 

(lookup `mctspy.games.examples.tictactoe.TicTacToeGameState` for inspiration)