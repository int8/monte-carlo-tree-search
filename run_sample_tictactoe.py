import numpy as np
from mcts.nodes import TwoPlayersGameMonteCarloTreeSearchNode
from mcts.search import MonteCarloTreeSearch
from games.tictactoe import TicTacToeGameState, TicTacToeMove

# Initialise
initial_state = np.zeros((3, 3))
board_state = TicTacToeGameState(state=initial_state, next_to_move=1)

b_interactive = False  # choose if there is a human player
human_player = TicTacToeGameState.x

while not board_state.is_game_over():
    if b_interactive & (board_state.next_to_move == human_player):
        user_row = int(input('What''s your move row? \n'))
        user_col = int(input('What''s your move column? \n'))
        user_move = board_state.move(
            TicTacToeMove(user_row, user_col, human_player))
        # update
        board_state = user_move
    else:
        root = TwoPlayersGameMonteCarloTreeSearchNode(
            state=board_state, parent=None)
        mcts = MonteCarloTreeSearch(root)
        best_node = mcts.best_action(1000)
        # update
        board_state = best_node.state

    print(board_state.board)
    print('\n')

print('--- Game result is: %s' % board_state.game_result)