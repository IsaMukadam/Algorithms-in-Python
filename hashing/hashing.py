# Can hash
print(hash(42))
print(hash(10**100))
print(hash("apina"))

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


