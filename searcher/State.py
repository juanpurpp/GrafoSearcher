class State:
    def __init__(self, node, father, last_weight=0):
        self.father = father
        self.node = node
        self.depth = 0 if father is None else father.get_depth()+1
        self.g = (0 if father is None else father.get_g() )+ last_weight
    
    def get_node(self):
        return self.node
    
    def get_choices(self):
        return [State(edge[0],self, edge[1]) for edge in self.node.get_choices()]

    def get_g(self):
        return self.g
    
    def get_h(self, final):
        #using euclidean distance
        [current_x, current_y] = self.node.get_pos()
        [final_x, final_y] = final.get_pos()
        return ( (final_x - current_x)**2 + (final_y - current_y)**2)**0.5
    
    def get_f(self, final):
        return self.get_g() + self.get_h(final)

    def get_depth(self):
        return self.depth

    def print_path(self):
        current = self
        while current is not None:
            print(current.node.get_name()+'->')
            current = current.father

    def get_path(self):
        current = self
        result= []
        while current is not None:
            result.append(current.node.get_name())
            current = current.father
        return list(reversed(result))


    def __eq__(self, other):
        return self.node == other.node