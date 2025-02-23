# Can hash
print(hash(42)) # 42
print(hash(10**100)) # 910685213754167845
print(hash("apina")) # -8392475334940914858

"""
As the above shows, in Python, the hash value of a small integer is the integer itself. Otherwise, the hash values are random looking numbers.
The Python data structures based on hashing are usually efficient, and you can assume that an addition, access or removal takes 
O(1) time. However, there is a possiblity that hashing is slow if the input chosen in a specific way.
"""

# Can't hash
# lists = set()
# lists.add([1, 2, 3]) # TypeError: unhashable type: 'list'
# print(hash([1, 2, 3])) # TypeError: unhashable type: 'list'

lists = {}
lists["apina"] = [1, 2, 3]

"""
If you define your own class, you can apply hashing to it by defining the following methods:

__hash__: returns the hash value of the object (the function hash calls this method)
__eq__: compares if two objects have identical content (the operator == calls this method)
The following shows an example of defining these methods. Here the method __hash__ returns the hash
value of a tuple representing the contents of the object.
"""
class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
    
locations = set()
locations.add(Location(1, 2))
locations.add(Location(3, -5))
locations.add(Location(1, 4))

# Printing the has
for l in locations:
    print(l)

# Printing the values
for l in locations:
    print("x: ", l.x, "y:", l.y)

