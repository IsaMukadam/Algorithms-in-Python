# Basics of the sort function
numbers = [4, 2, 1, 2]

numbers.sort()
print(numbers) # 1, 2, 2, 4

numbers = [4, 2, 1, 2]
print(sorted(numbers)) # 1, 2, 2, 4

# Method to find the min diff
def min_diff(numbers):
    numbers = sorted(numbers)

    result = numbers[1] - numbers[0]
    for i in range(2, len(numbers)):
        result = min(result, numbers[i] - numbers[i - 1])

    return result

print(min_diff(numbers))

numbers2 = [1,32,23,45,54]
print(min_diff(numbers2))

#################################### Note that: #########################################
# You can use the sort() function in the method instead but this would modify the list  #
# outside of the function and if you don't want this you must use the sorted() function #
#########################################################################################

########################### HASHING vs SORTING ####################################

# Using Hashing to count distinct variables
def count_distinct(numbers):
    seen = set()
    
    for x in numbers:
        seen.add(x)

    return len(seen)

print(count_distinct(numbers))

# Using Sorting to count distinct variables
def count_distinct1(numbers):
    numbers = sorted(numbers)

    result = 1
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1]:
            result += 1
    return result

print(count_distinct(numbers))

# Result - Hashing is more efficient time wise

############## Sorting in reverse order ###############

# Sort numbers into reverse order
numbers = [2,3,5,7,2,4,45,6,7,31,1,2]
numbers.sort(reverse=True)
print(numbers)

# Sorting multipart elements
pairs = [(2,3), (1,5), (5,4), (3,4)]
pairs.sort()
print(pairs)

# Element Comparisons
numbers = [4, -1, 6, 2, -7, 8, 3, -4]
numbers.sort(key=abs)
print(numbers)

# Sorting Location in own class
class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
    
    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)
    
    def __repr__(self):
        return str((self.x, self.y))

# Initialising a variable to store locations    
locations = []
# Appending some locations
locations.append(Location(1, 4))
locations.append(Location(4, 6))
locations.append(Location(3, 2))
locations.append(Location(1, 2))

locations.sort()

print(locations)

######## Function to track total customers in a restaurant at peak time ######### 
def max_customers(arrivals, departures):
    events = []

    # Appending the arrival times and departure times
    for time in arrivals:
        events.append((time, 1))
    for time in departures:
        events.append((time, 2))

    events.sort()

    counter = 0
    result = 0

    # Counting the number of concurrent customers as they arrive and leave and storing the highest number in result
    for event in events:
        if event[1] == 1:
            counter += 1
        if event[1] == 2:
            counter -= 1
        result = max(result, counter)
    
    return result

# Example inputs
arrivals = [6,3,6,1,2,5,6,7]
departures = [8,5,8,3,5,8,8,9]

# Running function on example inputs
print(max_customers(arrivals, departures)) # 5

####################### What happens during sorting #########################
import functools 

def cmp(a, b):
    print("compare", a, b)
    return a - b

numbers = [4, 1, 3, 2, 5, 9]
numbers.sort(key=functools.cmp_to_key(cmp))
print(numbers)

