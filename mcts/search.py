from mcts.nodes import MonteCarloTreeSearchNode

class MonteCarloTreeSearch:

    def __init__(self, node: MonteCarloTreeSearchNode):
        self.root = node


    def best_action(self, simulations_number):
        # check root is not terminal
        if self.root.is_terminal_node():
            return self.root  # returns the same node if no action
        else:
            for _ in range(0, simulations_number):
                v = self.tree_policy()
                reward = v.rollout()
                v.backpropagate(reward)
            # exploitation only
            return self.root.best_child(c_param=0.)


    def tree_policy(self):
        current_node = self.root
        while not current_node.is_terminal_node():
            if not current_node.is_fully_expanded():
                return current_node.expand()
            else:
                current_node = current_node.best_child()
        return current_node
