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