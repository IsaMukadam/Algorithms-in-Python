################################# Breadth-first Search ####################################

# Breadth-first search or BFS is another technique for iterating through the nodes of a graph. Similarly to depth-first search,
# breadth-first search starts at a given node and visits all nodes that are reachable from the start node using edges of the graph.
# The difference between the two techniques is the order in which the nodes are visited.

# Class to perform Breadth-First Search (BFS) on an undirected graph
class BFS:
    def __init__(self, nodes):
        """
        Constructor to initialise the graph.

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

    def search(self, start_node):
        """
        Performs Breadth-First Search (BFS) starting from a given node.

        :param start_node: The node from which the BFS traversal begins.
        :return: A set of visited nodes in the order they were discovered.
        """
        visited = set()  # Set to keep track of visited nodes

        queue = [start_node]  # Initialise the queue with the start node
        visited.add(start_node)  # Mark the start node as visited

        print("Graph:", self.graph)

        # Iterate through the queue (BFS traversal)
        for node in queue:
            # Explore all adjacent nodes (neighbors)
            for next_node in self.graph[node]:
                if next_node not in visited:  # If the neighbor hasn't been visited
                    queue.append(next_node)  # Add it to the queue for future processing
                    visited.add(next_node)  # Mark it as visited
                    print("Visited:", visited)

        return visited  # Return the set of visited nodes


b = BFS([1,2,3,4,5])

b.add_edge(1,2)
b.add_edge(1,3)
b.add_edge(1,4)
b.add_edge(2,4)
b.add_edge(2,5)
b.add_edge(3,4)
b.add_edge(4,5)

print(b.search(1)) # {1, 2, 3, 4, 5}