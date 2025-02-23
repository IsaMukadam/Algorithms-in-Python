# To create a file in windows use echo # set-vs-list.py > set-vs-list.py
# Use dir set-vs-list.py to check it was created

# Creating a set
a_set = set()

# Adding values
a_set.add(1)
a_set.add(2)
a_set.add(3)

print(a_set)

# Creating set outright
b_set = set([1,2,3])

print(b_set)

# True or False if value is in the set
print(3 in b_set)
print(6 in b_set)

# Removing value from set
b_set.remove(2)
print(b_set)

#################################### Lists vs Sets ##########################################
# A list and a set are similar data structures in that both maintain a collection
# of elements and support additions and removals. However, there are significant
# differences in their efficiency and other properties.
##################################### Efficiency ##############################################
# Adding an element to a list is efficient, but finding an element and removing it can be slow.
# With a set, adding elements, finding elements and removing elements are all efficient operations.

# List
c_list = [1,2,3,4,5]
print(c_list[1])

# Set
c_set = set([1,2,3,4,5])
# print(c_set[1]) # TypeError: 'set' object is not subscriptable

# Appending same number multiple times to a list
d_list = []

d_list.append(5)
d_list.append(5)
d_list.append(5)

print(d_list) # [5,5,5]

# Appending same number multiple times to a set
d_set = set()

d_set.add(5)
d_set.add(5)
d_set.add(5)

print(d_set) # {5}

############# Checking the amount of distinct numbers #################

# Example list
example_list = [1,2,3,4,5,63,56,6,546,654,645,65,456,6,45,465,645,456,564]
# Example Set
example_set = set([1,23,123,123,1,234,23,213,12,3,312,3,12,23,12,3,132,23,21])

# Slow Solution using a List O(n^2)
def count_distinct_list(numbers):
    seen = []
    for x in numbers:
        if x not in seen:
            seen.append(x)
    return len(seen)

# Efficient Solution using a Set O(n)
def count_distinct1(numbers):
    seen = set()
    for x in numbers:
        if x not in seen:
            seen.add(x)
    return len(seen)

# Testing List Solution
print("Distinct Count in List: ", count_distinct_list(example_list))
# Testing Set Solution
print("Method 1 Distinct Count in Set: ", count_distinct1(example_set))


# Efficient Solution Simplified
def count_distinct2(numbers):
    seen = set()
    for x in numbers:
        seen.add(x)
    return len(seen)

# Testing Set Efficient Solution Simplified
print("Method 2 Distinct Count in Set: ", count_distinct2(example_set))

# Shortest Efficient Solution
def count_distinct3(numbers):
    return len(set(numbers))

# Testing Set Shortest Efficient Solution
print("Method 3 Distinct Count in Set: ", count_distinct3(example_set))

