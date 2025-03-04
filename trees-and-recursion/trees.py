# The top-most node is called the root. A child of a node is a lower level
# node connected to it. A node is the parent of its children. If a node has
# no children, it is a leaf.

class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children
    
    def __repr__(self):
        return str(self.value)

# Creating nodes and adding values to them. 
node2 = Node(2)
node3 = Node(3)
# node1 is given 2 children node2 and node3.
node1 = Node(1, [node2, node3])

# Printing the nodes
# print(node1)
# print(node2)
# print(node3)

node = Node(1)
# print(node)

# Creating a tree from nodes
tree = Node(1, [Node(4, [Node(3), Node(7)]),
                Node(5),
                Node(2, [Node(6)])])

# You can only see the root of the tree but not its children outputting in this way
# print(tree) # 1

# How to 
def traverse(node):
    print(node)
    for child in node.children:
        traverse(child)

# traverse(tree) # 1 4 3 7 5 2 6
    
def traverse2(node):
    print("enter", node.value)
    for child in node.children:
        traverse2(child)
    print("leave", node.value)

traverse2(tree)
"""
enter 1
enter 4
enter 3
leave 3
enter 7
leave 7
leave 4
enter 5
leave 5
enter 2
enter 6
leave 6
leave 2
leave 1
"""

# Counting information from a tree
def count_nodes(node):
    result = 1
    for child in node.children:
        result += count_nodes(child)
    return result

print("Total nodes:", count_nodes(tree))

# Counting the number of numbers with detail of subtrees
def count_nodes_detailed(node):
    result = 1
    for child in node.children:
        result += count_nodes_detailed(child)
    print("subtree of node", node, "has", result, "nodes")
    return result

print("-------- Total nodes detailed --------")
total_nodes = count_nodes_detailed(tree)
print("Total number of nodes:", total_nodes) # Can just replace total_nodes with count_nodes_detailed(tree) but this means no of nodes variable is stored and can be used

# Counting the height
def count_height(node):
    result = 0
    for child in node.children:
        result = max(result, count_height(child) + 1)
    return result

print("Height of tree:", count_height(tree))

# Computing the depths
def traverse_depth(node, depth):
    print("node", node, "depth", depth)
    for child in node.children:
        traverse_depth(child, depth + 1)

print("----------- Traverse Depth -----------")
traverse_depth(tree, 0)

##### More complicated computation of depth #####

# Helper function traverses the child nodes keeping track of the current node and storing the depth in the depths list. 
def get_depths_helper(node, depth, depths):
    depths.append(depth)
    for child in node.children:
        get_depths_helper(child, depth + 1, depths)

# This function creates a list of depths for storing depths and calls the helper function to add all depths to the list
# It then sorts and return the list
def get_depths(node):
    depths = []
    get_depths_helper(node, 0, depths)
    return sorted(depths)

# Running the get_depths function which outputs a list of the depths of each node
print(get_depths(tree))

####### Alternative method #################

def get_depths(node):
    return(sorted(get_depths_helper(node, 0)))

def get_depths_helper(node, depth):
    depths = [depth]
    for child in node.children:
        depths += get_depths_helper(child, depth + 1)
    return depths

############## Improving the original node class ################

# Version 1
class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def __repr__(self): 
        return str(self.value)

node1 = Node(1)
node2 = Node(2)

node1.children.append(node2)

print(node1.children) # 2
print(node2.children) # 2

# Version 2
class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        return str(self.value)

node1 = Node(1)
node2 = Node(2)

node1.children.append(node2)

print(node1.children) # [2]
print(node2.children) # []

# Only prints the value and nothing about the children
tree = Node(1, [Node(2, [Node(3), Node(4)]), Node(5)])
print(tree) # 1

# Version 3
class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []
    
    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

tree = Node(1, [Node(2, [Node(3), Node(4)]), Node(5)])
print(tree) 

######## Taking this to a realistic scenario - WITH EMPLOYEES ##########

class Employee:
    def __init__(self, name, subordinates=[]):
        self.name = name
        self.subordinates = subordinates

    def __repr__(self):
        return self.name

def list_employees(employee, level=0):
    print(" "*(level*4), employee)
    for subordinate in employee.subordinates:
        list_employees(subordinate, level + 1)

staff = Employee("John",
                 [
                    Employee("Peter"),
                    Employee("Adam", [Employee("Anita")]),
                    Employee("Rico", [Employee("Mina")])
                 ])

list_employees(staff)

########### Another example to find out how many Queens's (n) you can place on a 4x4 board ##########################

# Counts the number of queens
def count_queens(n):
    return count(n, 0, [])


# Takes in n - size of the board, row - the next empty row and queen - the list of queens already placed
def count(n, row, queens):
    # If row is equal to n then return 1
    if row == n:
        return 1
    # Setting result to 0
    result = 0

    # Going through each column in board
    for col in range(n): 
        # Returns a list of attacks
        attacks = [attack(queen, (row, col)) for queen in queens] 
        if not any(attacks): 
            result += count(n, row + 1, queens + [(row, col)]) 
    return result

# Debug runthrough of count method for loop
# 230: (1) col = 0, n = 2 
#      (2) col = 1, n = 2 
# 232: (1) row = 0, col = 0, queens = [] 
#      (2) row = 1, col = 0, queens = [(0, 0)] 
#      (3) attacks = [True], row = 1, col = 1, queens = [(0, 0)]
# 233: (1) attacks = [] 
#      (2) attacks = [True] 
#      (3) attacks = [True] 
# 234: (1) result = 0, n = 2, queens = [], row = 0, col = 0 
#      (2) result = 0, n = 2, queens = [], row = 0, col = 1
# 235: (1) result = 0
#      (2) result = 0

# Handles the attack checks. Takes in queen1 and queen2 
def attack(queen1, queen2):
    # If either x or y co-ords for queen1 or queen2 match then it returns true for attack
    if queen1[0] == queen2[0] or queen1[1] == queen2[1]:
        return True
    if abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1]):
        return True
    # Returns false if either of the above if statements aren't True
    return False  

# Printing for different board sizes
print(count_queens(2)) # 0
print(count_queens(4)) # 2
print(count_queens(8)) # 92
