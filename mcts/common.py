import numpy as np
from collections import defaultdict
from mcts.tictactoe import *
from games.tictactoe import *

class MonteCarloTreeSearchSimulation:

    def __init__(self, starting_node):
        self.starting_node = starting_node

    def simulate(self, number_of_simulations):
        for n_total in range(1, number_of_simulations):
            current_node = self.starting_node
            while(True):
                if current_node.is_leaf():
                    break
                else:
                    current_node = current_node.choose_node_to_explore(n_total)

            expanded_node = current_node.expand(n_total)
            if expanded_node:
                game_result = expanded_node.rollout()
                expanded_node.backpropagate(game_result)
            else:
                game_result = current_node.state.game_result()
                current_node.backpropagate(game_result)


class AbstractNode:
    children = None
    parent = None

    def is_leaf(self):
        return self.children == None or len(self.children) == 0

class AbstractMonteCarloTreeSearchNode(AbstractNode):

    def __init__(self, state, parent):
        self.state = state
        self.number_of_visits = 0.
        self.results = defaultdict(lambda  : 0)
        self.parent = parent

    def expand(self, N_total):
        self.children = self.compute_child_nodes()
        node = self.choose_node_to_explore(N_total)
        return node

    def choose_node_to_explore(self, N_total, c_param = 2.):
        if self.is_leaf():
            return None
        else:
            choices_weights = [
                self._node_choice_metric(
                    c.results[self.state.player_to_move.game_result_winning_value] if self.state.player_to_move.game_result_winning_value in c.results else 0,
                    c.number_of_visits,
                    N_total,
                    c_param
                )
                for c in self.children
            ]
            return self.children[np.argmax(choices_weights)]

    def rollout(self):
        current_rollout_state = self.state
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
        self.results[rollout_result] += 1
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
