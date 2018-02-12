## Experimental implementation of Monte Carlo Tree Search algorithm

The purpose of this code is to create MCTS + neural-network based chess bot. So far, simple implementation of MCTS for tic-tac-toe

(code may still be buggy, not tested)


to run try:

```python

import numpy as np
from mcts.tictactoe import *
from mcts.common import MonteCarloTreeSearchSimulation
from games.tictactoe import *
from games.players import *

player_x = PlayerWithOpponent(move_value = 1, game_result_winning_value = 1, game_result_losing_value = 0, game_result_draw_value = 0.5)
player_o = PlayerWithOpponent(move_value = -1, game_result_winning_value = 0, game_result_losing_value = 1, game_result_draw_value = 0.5)
player_x.define_opponent(player_o)
player_o.define_opponent(player_x)

root = TicTacToeMonteCarloTreeSearchNode(current_state = TicTacToeState(state = np.zeros((3,3)), player_to_move = player_x), parent = None)
mcts = MonteCarloTreeSearchSimulation(root)
mcts.simulate(1000)

```
