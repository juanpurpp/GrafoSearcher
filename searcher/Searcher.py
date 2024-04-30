from searcher.State import State
from functools import cmp_to_key


class Searcher:
    def __init__(self, problem):
        self.problem = problem

    def order_by_f(self, states, final_node):
        return sorted(states,key=cmp_to_key(lambda item1, item2: item2.get_f(final_node)-item1.get_f(final_node)))

    def start_a(self, from_node_name, to_node_name, on_iteration):
        initial_node = self.problem.get_node(from_node_name)
        final_node = self.problem.get_node(to_node_name)
        initial = State(initial_node, None)
        final = State(final_node, None)
        current = initial
        explored = [current]
        left = []
        while current != final:
            choices = current.get_choices()
            for new_state in self.order_by_f(choices, final_node):
                print('statsito')
                print(new_state)
                if new_state not in explored:
                    explored.append(new_state)
                    left.append(new_state)
            current = left.pop(0)
        
        current.print_path()
        
        
