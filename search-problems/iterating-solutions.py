import itertools  # Import the itertools module for combinatorial functions

# Generate all possible products (with repetition) of length 2 using elements [1, 2, 3]
# Output: (1,1), (1,2), (1,3), (2,1), (2,2), (2,3), etc.
for repetition in itertools.product([1,2,3], repeat=2):
    print(repetition)

# Generate all possible **permutations** (unique orderings) of [1, 2, 3]
# Output: (1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)
for permutation in itertools.permutations([1, 2, 3]):
    print(permutation)

# Generate all **combinations** (unordered subsets of size 2) from [1, 2, 3, 4]
# Output: (1,2), (1,3), (1,4), (2,3), (2,4), (3,4)
for combination in itertools.combinations([1, 2, 3, 4], 2):
    print(combination)


###################### Orderings #############################

def count_orders(n):
    """
    Counts the number of valid orderings of numbers from 1 to n,
    where adjacent numbers do not have a difference of 1.
    """
    items = range(1, n + 1)  # Generate numbers from 1 to n
    count = 0  # Counter for valid orderings

    # Generate all possible permutations of the numbers
    for order in itertools.permutations(items):
        if valid_order(order):  # Check if the ordering is valid
            print(order)
            count += 1  # Increment count if valid

    return count  # Return the total number of valid orders


def valid_order(order):
    """
    Checks if an order is valid by ensuring no adjacent elements have
    an absolute difference of 1.
    """
    for i in range(len(order) - 1):  # Iterate through the order
        if abs(order[i] - order[i + 1]) == 1:  # Check absolute adjacent differences
            return False  # Invalid order if adjacent numbers differ by 1
    return True  # Return True if no invalid adjacent pairs found

print(count_orders(4)) # 2
print(count_orders(5)) # 14
# print(count_orders(10)) # 479306



