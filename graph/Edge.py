class Edge:
    def __init__(self, a, b, w):
        self.node_a = a
        self.node_b = b
        self.weight = w
    
    def get_start(self):
        return self.node_a
    
    def get_end(self):
        return self.node_b
    
    def get_weight(self):
        return self.weight
    
    def get_start_name(self):
        return self.node_a.get_name()
    