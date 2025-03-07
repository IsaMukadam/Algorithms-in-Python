class Distances:
    def __init__(self, nodes):
        """
        Constructor to initialise the graph.

        :param nodes: A list of nodes in the graph.
        """
        self.nodes = nodes # Store a list of nodes
        self.graph = {node: [] for node in nodes} # Create an adjacency list where each node maps to an empty list (initially no connections)

    def add_edge(self, a, b):
        """
        Adds an undirected edge between nodes 'a' and 'b'.

        :param a: First node
        :param b: Second node
        """
        self.graph[a].append(b) # Add 'b' to 'a's adjacency list
        self.graph[b].append(a) # Add 'a' to 'b's adjacency list

    def find_distances(self, start_node):
        """
        Finds the shortest distance from the start_node to all other nodes using BFS.

        :param start_node: The node from which distances are calculated.
        :return: A dictionary where keys are nodes and values are their distances from the start_node.
        """
        distances = {start_node: 0} # Dictionary to store distances, start_node has a distance of 0.
        queue = [start_node] # Initialises the queue with the start node

        # Perform shortest distances search
        for node in queue: 
            distance = distances[node] # Get current nodes distance

            # Visit all adjacent nodes
            for next_node in self.graph[node]:
                if next_node not in distances: # If node hasn't been visited
                    queue.append(next_node) # Add to queue for processing
                    distances[next_node] = distance + 1 # Update the distance (1 step further)
            
        return distances # Return dict containing the shortest distances
        


d = Distances([1,2,3,4,5,6])

d.add_edge(1,2)
d.add_edge(1,3)
d.add_edge(1,4)
d.add_edge(2,4)
d.add_edge(2,5)
d.add_edge(3,4)
d.add_edge(4,5)
d.add_edge(5,6)


print(d.find_distances(1)) # {1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 3}
print(d.find_distances(5)) # {5: 0, 2: 1, 4: 1, 6: 1, 1: 2, 3: 2}