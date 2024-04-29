from graph.Edge import Edge
class Node:
    def __init__(self, x, y, name, graph):
        self.x = x
        self.y = y
        self.name = name
        self.graph = graph
        self.edges = []
    
    def connect_to(self, goal_node, w, bidirectional = True):
        #creating new edge
        new_edge = Edge(self, goal_node, w)
        self.edges.append(new_edge)
        self.graph.add_edge(new_edge)
        if bidirectional:
            new_bidirectional_edge = Edge(goal_node, self, w)
            goal_node.edges.append(new_bidirectional_edge)
            self.graph.add_edge(new_bidirectional_edge)
        
    def get_pos(self):
        return [self.x, self.y]

    def get_name(self):
        return self.name
    
