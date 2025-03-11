class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class TreeSet:
    def __init__(self):
        self.root = None
    
    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return
        
        node = self.root
        while True:
            if node.value == value:
                return
            if node.value > value:
                if not node.left:
                    node.left = Node(value)
                    # Continue here
                




s = TreeSet()

s.add(1)
s.add(2)
s.add(3)

print(2 in s) # True
print(4 in s) # False

print(s) # [1, 2, 3]