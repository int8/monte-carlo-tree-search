from mcts.common import AbstractMonteCarloTreeSearchNode
from games.tictactoe import TicTacToeState
import numpy as np

class TicTacToeMonteCarloTreeSearchNode((AbstractMonteCarloTreeSearchNode)):

    def __init__(self, current_state: TicTacToeState):
        AbstractMonteCarloTreeSearchNode.__init__(self, current_state)

    def compute_child_nodes(self):
        legal_actions = self.current_state.get_legal_actions()
        child_nodes = [TicTacToeMonteCarloTreeSearchNode(self.current_state.move(move)) for move in legal_actions]
        return child_nodes


    def rollout_policy(self, possible_moves):
        return possible_moves[np.random.randint(len(possible_moves))]
