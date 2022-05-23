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

### Example Game Play
```python
import numpy as np
from mctspy.tree.nodes import TwoPlayersGameMonteCarloTreeSearchNode
from mctspy.tree.search import MonteCarloTreeSearch
from mctspy.games.examples.connect4 import Connect4GameState

# define inital state
state = np.zeros((7, 7))
board_state = Connect4GameState(
    state=state, next_to_move=np.random.choice([-1, 1]), win=4)

# link pieces to icons
pieces = {0: " ", 1: "X", -1: "O"}

# print a single row of the board
def stringify(row):
    return " " + " | ".join(map(lambda x: pieces[int(x)], row)) + " "

# display the whole board
def display(board):
    board = board.copy().T[::-1]
    for row in board[:-1]:
        print(stringify(row))
        print("-"*(len(row)*4-1))
    print(stringify(board[-1]))
    print()

display(board_state.board)
# keep playing until game terminates
while board_state.game_result is None:
    # calculate best move
    root = TwoPlayersGameMonteCarloTreeSearchNode(state=board_state)
    mcts = MonteCarloTreeSearch(root)
    best_node = mcts.best_action(total_simulation_seconds=1)

    # update board
    board_state = best_node.state
    # display board
    display(board_state.board)

# print result
print(pieces[board_state.game_result])

```
