class Stack: 
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
    
    def top(self):
        # Stops error occurring when top is requested but the stack is empty
        if len(self.stack) == 0:
            raise IndexError("Top attemped from empty stack. Please add some values first.")
        return self.stack[-1]
    
    def pop(self):
        # Stops error occurring when stack is empty
        if len(self.stack) == 0:
            raise IndexError("Pop attempted from empty stack. Please add some values first.")
        return self.stack.pop()
        
    def __repr__(self):
        return str(self.stack)

    def __len__(self):
        return len(self.stack)

# Creating a stack by creating an instance of the class
st = Stack()
# Pushing to the stack
st.push(1)
st.push(2)
st.push(3)
# Printing the value at the top of the stack (Last in)
print(st.top()) #3
print(st.top()) #3
# Removing last value in
st.pop()
print(st.top()) #2

# Pushing again to same stack
st.push(1)
st.push(2)
st.push(3)
# Output is the previous values + new ones added
print(st.stack) # [1,2,1,2,3]

# Creating a new stack and outputting the value alone (Only works because the __repr__() method has been added)
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s)

# Checking the len of the stack (Only work because the __len__() method has been added)
print(len(s)) # 3

# Trying to pop from empty stack (Same will happen for top method)
s = Stack()
s.push(1)
s.pop()
# s.pop() # IndexError raised here

class SuperStack:
    def __init__(self):
        self.stack = []
        
    def push(self, x):
        self.stack.append((1, x))
        
    def push_many(self, k, x):
        self.stack.append((k, x))
        
    def top(self):
        return self.stack[-1][1]
        
    def pop(self):
        last = self.stack[-1]
        if last[0] == 1:
            self.stack.pop()
        else:
            self.stack[-1] = (last[0] - 1, last[1])

s = SuperStack()
s.push_many(3, 8)
s.push(4)
s.push_many(2, 5)

# Poping from the stack 
print(s.stack)
s.pop()
print(s.stack)
print(s.top())
s.pop()
print(s.stack)
print(s.top())

# Mode class example
class Mode:
    def __init__(self):
        self.count = {}
        self.status = (0, 0)

    def add(self, x):
        if x not in self.count:
            self.count[x] = 0
        self.count[x] += 1
        self.status = max(self.status, (self.count[x], x))

    def mode(self):
        return self.status[1]        
        
# Making an instance of the Mode class and using the add method
m = Mode()
m.add(1)
m.add(1)
m.add(3)
print(m.mode())
# The mode changes when the number of 3's overtakes
m.add(3)
m.add(3)
print(m.mode())