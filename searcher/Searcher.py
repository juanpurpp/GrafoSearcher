from searcher.State import State
from functools import cmp_to_key
import time

class Searcher:
    def __init__(self, problem):
        self.problem = problem

    def order_by_f(self, states, final_node):
        return sorted(states,key=cmp_to_key(lambda item1, item2: item1.get_f(final_node)-item2.get_f(final_node)))

    def order_by_h(self, states, final_node):
        return sorted(states,key=cmp_to_key(lambda item1, item2: item1.get_h(final_node)-item2.get_h(final_node)))

    def order_by_g(self, states, final_node):
        return sorted(states,key=cmp_to_key(lambda item1, item2: item1.get_g()-item2.get_g()))


    async def start_a(self, from_node_name, to_node_name, on_iteration):
        start_time = time.time()
        initial_node = self.problem.get_node(from_node_name)
        final_node = self.problem.get_node(to_node_name)
        initial = State(initial_node, None)
        final = State(final_node, None)
        current = initial
        explored = [current]
        left = []
        iterations = 0
        while current != final:
            iterations += 1
            choices = current.get_choices()
            for new_state in self.order_by_f(choices, final_node):
                print('statsito')
                print(new_state)
                if new_state not in explored:
                    explored.append(new_state)
                    left.append(new_state)
            current = left.pop(0)
            await on_iteration({
                "path": current.get_path(),
                "visited": len(explored),
                "left": len(left),
                "iterations": iterations,
                "time": time.time() - start_time,
                "current_depth": current.get_depth(),
                "cost": current.get_g(),
            })
        
        current.print_path()
    
    async def start_greedy(self, from_node_name, to_node_name, on_iteration):
        start_time = time.time()
        initial_node = self.problem.get_node(from_node_name)
        final_node = self.problem.get_node(to_node_name)
        initial = State(initial_node, None)
        final = State(final_node, None)
        current = initial
        explored = [current]
        left = []
        iterations = 0
        while current != final:
            iterations += 1
            choices = current.get_choices()
            for new_state in self.order_by_h(choices, final_node):
                print('statsito')
                print(new_state)
                if new_state not in explored:
                    explored.append(new_state)
                    left.append(new_state)
            current = left.pop(0)
            await on_iteration({
                "path": current.get_path(),
                "visited": len(explored),
                "left": len(left),
                "iterations": iterations,
                "time": time.time() - start_time,
                "current_depth": current.get_depth(),
                "cost": current.get_g(),
            })
        current.print_path()

    async def start_uniform(self, from_node_name, to_node_name, on_iteration):
        start_time = time.time()
        initial_node = self.problem.get_node(from_node_name)
        final_node = self.problem.get_node(to_node_name)
        initial = State(initial_node, None)
        final = State(final_node, None)
        current = initial
        explored = [current]
        left = []
        iterations = 0
        while current != final:
            iterations += 1
            choices = current.get_choices()
            for new_state in self.order_by_g(choices, final_node):
                print('statsito')
                print(new_state)
                if new_state not in explored:
                    explored.append(new_state)
                    left.append(new_state)
            current = left.pop(0)
            await on_iteration({
                "path": current.get_path(),
                "visited": len(explored),
                "left": len(left),
                "iterations": iterations,
                "time": time.time() - start_time,
                "current_depth": current.get_depth(),
                "cost": current.get_g(),
            })
        
        current.print_path()

