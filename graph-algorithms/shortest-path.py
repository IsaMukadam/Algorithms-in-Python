class ShortestPaths:
    def __init__(self, nodes):
        """
        Constructor to initialise the graph.

        :param nodes: A list of nodes in the graph.
        """
        self.nodes = nodes # Store nodes
        self.graph = {node: [] for node in nodes} # Create an adjacency list where each node maps to an empty list (no connection initially)

    def add_edge(self, a, b):
        """
        Adds an undirected edge between 'a' and 'b'.

        :param a: First node
        :param b: Second node
        """
        self.graph[a].append(b) # Add 'a' to 'b's adj list
        self.graph[b].append(a) # Add 'b' to 'a's adj list

    def find_path(self, start_node, end_node):
        """
        Finds shortest path between start_node and end_node using BFS.

        :param start_node: The node where search starts.
        :param end_node: Destination node.
        :return: List representing shortest path from start to end node, or None if no path exists.
        """
        distances = {} # Dict to store shortest path
        previous = {} # Dict to store previous node for path reconstruction

        queue = [start_node] # Initialise queue with start node
        distances[start_node] = 0 # Distance to itself is 0 
        previous[start_node] = None # No previous node for start node
        
        # Using BFS Traversal
        for node in queue:
            distance = distances[node] # Get current nodes distance
            
            # Visit all adjacent nodes
            for next_node in self.graph[node]:
                if next_node not in distances: # If node has not been visited
                    queue.append(next_node) # Add to queue for processing
                    distances[next_node] = distance + 1 # Update distance (1 step further away)
                    previous[next_node] = node
                
            # If end node was never reached, return None (no path to end node)
            if end_node not in distances:
                return None
            
            # Reconstruct path from end_node to start_node
            node = end_node
            path = []
            while node:
                path.append(node) # Add node to path
                node = previous[node] # Move to previous node

            path.reverse() # Reverse the path to get it from start to end
            return path # Return shortest path as list
        
    def find_path_v2(self, start_node, end_node):
        """
        Finds the shortest path between start_node and end_node using BFS.
        Returns a list representing the shortest path or None if no path exists.
        """
        if start_node not in self.graph or end_node not in self.graph:
            return None  # Edge case: If nodes are not in the graph, return None

        distances = {}  # Track shortest distance from start_node
        previous = {}   # Store previous node for path reconstruction
        queue = [start_node]  # BFS queue
        distances[start_node] = 0
        previous[start_node] = None  # No previous node for the start

        # **Fix: Use while-loop for proper BFS traversal**
        while queue:
            node = queue.pop(0)  # Pop the first node in the queue (FIFO behavior)

            # Visit each adjacent node
            for next_node in self.graph[node]:
                if next_node not in distances:  # If not visited
                    queue.append(next_node)
                    distances[next_node] = distances[node] + 1  # Update distance
                    previous[next_node] = node  # Store previous node for path reconstruction

        # If end_node was never reached, return None
        if end_node not in distances:
            return None

        # **Reconstruct the shortest path from end_node to start_node**
        path = []
        node = end_node
        while node is not None:  # Stop when we reach None (the start node)
            path.append(node)
            node = previous[node]

        path.reverse()  # Reverse the path to get correct order
        return path
        

s = ShortestPaths([1, 2, 3, 4, 5, 6])

s.add_edge(1, 2)
s.add_edge(1, 3)
s.add_edge(1, 4)
s.add_edge(2, 4)
s.add_edge(2, 5)
s.add_edge(3, 4)
s.add_edge(4, 5)
s.add_edge(5, 6)

# Method find_path doesn't work for the below
print(s.find_path(2, 4)) # [2, 4]
print(s.find_path(1, 5)) # None
print(s.find_path(5, 1)) # None
print(s.find_path(1, 6)) # None

################ Using Method v2 which solves issue with find_path() ##############

# 🔴 Original Issue in find_path()
# for node in queue:
# The loop only iterates once per element already in the queue at the time of entering the loop.
# New elements added inside the loop aren’t processed.

# ✅ Corrected in find_path_v2()
# while queue:
#   node = queue.pop(0)  # Process nodes in correct order (FIFO)
# Ensures all nodes are explored in the right order.
# BFS correctly finds the shortest path.

# Method find_path doesn't work for the below
print(s.find_path_v2(2, 4)) # [2, 4]
print(s.find_path_v2(1, 5)) # [1, 2, 5]
print(s.find_path_v2(5, 1)) # [5, 2, 1]
print(s.find_path_v2(1, 6)) # [1, 2, 5, 6]
