def _leaves(node, leaves=[]):
    if not node.children:
        leaves.append(node)
        return leaves
    else:
        for _, child in node.children.items():
            _leaves(child, leaves)

        return leaves

def pfr(node, path=[]):
    path.insert(0, node)

    if not node.parent:
        return path
    else:
        return pfr(node.parent, path)

def walking_depth_in_order(node, callable, output=[]):  
    output.append(callable(node))  
    if not node.children:
        return output
    else:
        for _, child in node.children.items():
            walking_depth_in_order(child, callable, output)
        return output

class Node:
    def __init__(self, id, data=None):
        self.id = id
        self.data = data
        self.parent = None
        self.children = {}
    
    def add_child(self, node):
        node.parent = self
        self.children[node.id] = node
    
    def add_children(self, nodes):
        for node in nodes:
            self.add_child(node)
    
    def path_from_root(self):
        return pfr(self, path=[])

    def leaves(self):
        return _leaves(self)
    
    def __str__(self):
        return f"<Node {self.id}>"
    
    def __repr__(self):
        return self.__str__()
    

class Tree:
    pass