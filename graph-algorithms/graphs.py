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

print(graph)

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

############################## Depth-first Search ###################################

# Depth-first search or DFS is a technique for iterating through all nodes of a graph
# that can be reached from a given initial node by following edges. Depth-first search
# can be implemented using recursion given the adjacency lists.

# Define the DFS class
class DFS:
    # Constructor to initialize the graph with given nodes
    def __init__(self, nodes):
        self.nodes = nodes  # Store the list of nodes
        # Create an adjacency list where each node maps to an empty list (no edges yet)
        self.graph = {node: [] for node in nodes}

    # Method to add an edge between two nodes in an undirected graph
    def add_edge(self, a, b):
        self.graph[a].append(b)  # Add b to a's adjacency list
        self.graph[b].append(a)  # Add a to b's adjacency list (since it's undirected)
        
    # Recursive DFS traversal method
    def visit(self, node):
        if node in self.visited:  # Base case: If the node is already visited, return
            return 
        self.visited.add(node)  # Mark the node as visited

        # Visit all adjacent nodes (neighbors)
        for next_node in self.graph[node]:  
            self.visit(next_node)  # Recursively visit the next node

    # Method to start the DFS traversal
    def search(self, start_node):
        self.visited = set()  # Initialize an empty set to track visited nodes
        self.visit(start_node)  # Begin DFS from the start node
        

        return self.visited  # Return all visited nodes after DFS completes

d = DFS([1,2,3,4,5])

d.add_edge(1,2)
d.add_edge(1,3)
d.add_edge(1,4)
d.add_edge(2,4)
d.add_edge(2,5)
d.add_edge(3,4)
d.add_edge(4,5)

print(d.search(1))

class Components:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def visit(self, node):
        if node in self.components:
            return
        self.components[node] = self.counter

        for next_node in self.graph[node]:
            self.visit(next_node)

    def find_components(self):
        self.counter = 0 
        self.components = {}

        for node in self.nodes:
            if node not in self.components:
                self.counter += 1
                self.visit(node)

        return self.components
    
c = Components([1,2,3,4,5])

c.add_edge(1,2)
c.add_edge(3,4)
c.add_edge(3,5)
c.add_edge(4,5)

print(c.find_components())