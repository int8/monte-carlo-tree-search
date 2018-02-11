import numpy as np
from mcts.tictactoe import *
from games.tictactoe import *

class TicTacToeMonteCarloTreeSearch:

    def __init__(self, root, number_of_simulations):
        self.root = root
        self.number_of_simulations = number_of_simulations

    def simulate(self, state):
        root = TicTacToeMonteCarloTreeSearchNode(current_state = TicTacToeState(state = state), next_to_move = 1))
        for N_total in range(1,100):
            current_node = root
            while(True):
                if current_node.is_leaf():
                    break
                else:
                    current_node = current_node.choose_node_to_explore(N_total)

            expanded_node = current_node.expand(N_total)
            if expanded_node:
                game_result = expanded_node.rollout()
                expanded_node.backpropagate(game_result)
            else:
                game_result = current_node.current_state.game_result()
                current_node.backpropagate(game_result)

class AbstractNode:
    children = None
    parent = None

    def is_leaf(self):
        return self.children == None or len(self.children) == 0

class AbstractMonteCarloTreeSearchNode(AbstractNode):

    def __init__(self, current_state):
        self.current_state = current_state
        self.value = 0.
        self.number_of_visits = 0.

    def expand(self, N_total):
        self.children = self.compute_child_nodes()
        node = self.choose_node_to_explore(N_total)
        return node

    def choose_node_to_explore(self, N_total, c_param = 2.):
        if self.is_leaf():
            return None
        else:
            choices_weights = [ self._node_choice_metric(c.value, c.number_of_visits, N_total, c_param) for c in self.children]
            return self.children[np.argmax(choices_weights)]

    def rollout(self):
        current_rollout_state = self.current_state
        while(True):
            possible_moves = current_rollout_state.get_legal_actions()
            if len(possible_moves) > 0:
                action = self.rollout_policy(possible_moves)
                current_rollout_state = current_rollout_state.move(action)
            else:
                break
        rollout_result = current_rollout_state.game_result()
        return rollout_result

    def backpropagate(self, rollout_result):
        self.value += rollout_result
        self.number_of_visits += 1.
        if self.parent:
            self.parent.backpropagate(rollout_result)

    def _node_choice_metric(self, value, number_of_visits, N_total, c_param):
        v =  value / (number_of_visits + 1.) + c_param * (np.log(N_total) / (number_of_visits + 1.))
        return v

    def compute_child_nodes(self):
        raise NotImplemented("please implement compute_child_nodes function")

    def rollout_policy(self):
        raise NotImplemented("please implement rollout function")
