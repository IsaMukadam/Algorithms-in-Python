# A common way to represent a graph in programming is to have an adjacency list for each node. 
# The adjacency list of a node x contains all nodes connected to x by an edge.
# In Python, we can store a graph using a dictionary, where the keys are nodes and the values are adjacency lists.

graph = {
    1: [2, 3, 4],
    2: [1, 4, 5],
    3: [1, 4],
    4: [1, 2, 3, 5],
    5: [2, 4]
}

print(graph) # {1: [2, 3, 4], 2: [1, 4, 5], 3: [1, 4], 4: [1, 2, 3, 5], 5: [2, 4]}

############################## Graph Class ###################################

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

g = Graph([1, 2, 3, 4, 5])

g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,4)
g.add_edge(2,5)
g.add_edge(3,4)
g.add_edge(4,5)

print(g.graph) # Same thing as above {1: [2, 3, 4], 2: [1, 4, 5], 3: [1, 4], 4: [1, 2, 3, 5], 5: [2, 4]}