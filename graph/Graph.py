from graph.Node import Node
class Graph:
    def __init__(self, name = 'graph', ):
        self.nodes = []
        self.edges = []
        self.name = name
    
    def add_node(self, x, y, name):
        new_node = Node(x,y,name, self)
        self.nodes.append(new_node)
        return new_node

    def add_edge(self, new_edge):
        self.edges.append(new_edge)

    def get_node(self, target):
        for node in self.nodes:
            if node.name == target:
                return node
        return None

    def get_raw_edges(self):
        return [ [edge.get_start().get_pos() , edge.get_end().get_pos(), edge.get_weight(), edge.get_start_name()] for edge in self.edges ]