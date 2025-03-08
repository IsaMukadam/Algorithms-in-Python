import collections

# Deque is a list structure where additions and removals at both ends of the list are efficient.
# In Python, deque is available in the module collections and has the following methods:

# append: add an element to the end of the list
# pop: remove the element at the end of the list
# appendleft: add an element to the beginning of the list
# popleft: remove the element at the beginning of the list

# As the code shows, the elements of a deque can be accessed using the indexing operator [] similarly
# to the standard list. However, an access to an element through an index can be inefficient in a deque,
# which is a major weakness of the deque. In the standard list any element can be accessed in O ( 1 ) O(1)
# time, but an access to an element in the middle of a deque takes O ( n ) O(n) time.

items = collections.deque()

items.append(1)
items.append(2)
items.appendleft(3)
items.append(4)
items.appendleft(5)

print(items) # deque([5,3,1,2,4])

print(items[0]) # 5
print(items[1]) # 3
print(items[-1]) # 4

# Stack Class using Deque
class Stack:
    def __init__(self):
        self.stack = collections.deque()

    def push(self, x):
        self.stack.append(x)

    def top(self):
        return self.stack[-1]
    
    def pop(self):
        self.stack.pop()
    
# Queue Class using Deque
class Queue:
    def __init__(self):
        self.queue = collections.deque()
    
    def push(self, x):
        self.queue.append(x)

    def top(self):
        return self.queue[0]
    
    def pop(self):
        self.queue.popleft()

############## Example Usage of Stack Class ##################
# Create a stack instance
stack = Stack()

# Push elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Get the top element of the stack (should return 30)
print("Top element of stack:", stack.top())  # Output: 30

# Pop an element from the stack
stack.pop()

# Get the new top element of the stack (should return 20)
print("Top element of stack after pop:", stack.top())  # Output: 20

# Pop all elements from the stack
stack.pop()
stack.pop()

# Try to access the top element of an empty stack (will raise IndexError if called)
try:
    print("Top element of empty stack:", stack.top())
except IndexError:
    print("The stack is empty.")


################ Example Usage of Queue Class ################
# Create a queue instance
queue = Queue()

# Push elements into the queue
queue.push(10)
queue.push(20)
queue.push(30)

# Get the front element of the queue (should return 10)
print("Front element of queue:", queue.top())  # Output: 10

# Pop an element from the queue
queue.pop()

# Get the new front element of the queue (should return 20)
print("Front element of queue after pop:", queue.top())  # Output: 20

# Pop all elements from the queue
queue.pop()
queue.pop()

# Try to access the front element of an empty queue (will raise IndexError if called)
try:
    print("Front element of empty queue:", queue.top())
except IndexError:
    print("The queue is empty.")