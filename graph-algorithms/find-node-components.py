###################### Class to find connected components in an undirected graph ################################
class Components:
    def __init__(self, nodes):
        """
        Constructor to initialize the graph.
        :param nodes: A list of nodes in the graph.
        """
        self.nodes = nodes  # Store the list of nodes
        # Create an adjacency list where each node maps to an empty list (initially no connections)
        self.graph = {node: [] for node in nodes}

    def add_edge(self, a, b):
        """
        Adds an undirected edge between nodes 'a' and 'b'.
        :param a: First node
        :param b: Second node
        """
        self.graph[a].append(b)  # Add 'b' to 'a's adjacency list
        self.graph[b].append(a)  # Add 'a' to 'b's adjacency list (since the graph is undirected)

    def visit(self, node):
        """
        Recursively visits all connected nodes and assigns them to the same component.
        :param node: The node being visited.
        """
        if node in self.components:  # If the node has already been assigned to a component, return
            return
        self.components[node] = self.counter  # Assign the node to the current component number

        # Visit all adjacent nodes (neighbors) recursively
        for next_node in self.graph[node]:  
            self.visit(next_node)  # Recursively explore the connected component

    def find_components(self):
        """
        Finds and labels all connected components in the graph.

        :return: Dictionary where keys are nodes and values are their component labels.
        """
        self.counter = 0  # Counter to assign unique component IDs
        self.components = {}  # Dictionary to store component assignments

        # Iterate through all nodes in the graph
        for node in self.nodes:
            if node not in self.components:  # If the node is unvisited (not assigned to any component)
                self.counter += 1  # Start a new component
                self.visit(node)  # Perform DFS to mark all nodes in this component

        return self.components  # Return the dictionary mapping nodes to component numbers
    
c = Components([1,2,3,4,5,6,7,8])

# 1 -- 2 | 3 -- 4 -- 5 | 6 -- 7 | 8 (isolated)

c.add_edge(1,2)
c.add_edge(3,4)
c.add_edge(3,5)
c.add_edge(4,5)
c.add_edge(6,7)

# Finds connected components, assigning a new component ID if not visited before.
print(c.find_components()) # {1: 1, 2: 1, 3: 2, 4: 2, 5: 2, 6: 3, 7: 3, 8: 4}


