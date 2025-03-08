# Brute-force approach to count balanced parenthesis sequences
def count_sequences(n, d=0):
    """
    Counts the number of valid balanced parenthesis sequences of length 2n 
    using a recursive brute-force approach.

    Args:
    n (int): The number of steps left to place parentheses.
    d (int): The balance factor (difference between open and close brackets).

    Returns:
    int: The number of valid balanced sequences.
    """
    # If balance goes negative or exceeds n, it's invalid
    if d < 0 or d > n:
        return 0

    # If no more parentheses are left to place and balance is 0, it's a valid sequence
    if n == 0:
        return 1

    # Recursively explore adding an opening '(' or a closing ')'
    return count_sequences(n - 1, d + 1) + count_sequences(n - 1, d - 1)

# Optimized dynamic programming approach to count balanced parenthesis sequences and store in a dictionary
def count_sequences(n, d=0, result={}):
    """
    Uses memoization (dynamic programming) to avoid redundant computations 
    and efficiently count the number of balanced parenthesis sequences.

    Args:
    n (int): The number of steps left to place parentheses.
    d (int): The balance factor (difference between open and close brackets).
    result (dict): A cache to store computed values for reuse.

    Returns:
    int: The number of valid balanced sequences.
    """
    # If balance goes negative or exceeds n, it's invalid
    if d < 0 or d > n:
        return 0

    # If no more parentheses are left to place and balance is 0, it's a valid sequence
    if n == 0:
        return 1

    # If the result for (n, d) is already computed, return the cached value
    if (n, d) not in result:
        # Store the computed result to avoid redundant recursion
        result[(n, d)] = count_sequences(n - 1, d + 1, result) + count_sequences(n - 1, d - 1, result)

    return result[(n, d)]  # Return the cached result

# Since each call of the function needs O ( 1 ) O(1) time and the number of parameter combinations
# is O ( n 2 ) O(n 2 ), the time complexity of the algorithm is O ( n 2 ) O(n 2 ).

print(count_sequences(100)) # 1978261657756160653623774456


########################## Another dynamic programming approach ################################
# In this algorithm, each function call takes O ( n ) O(n) time and the number of parameter
# combinations is O ( n ) O(n). Thus the time complexity of this algorithm too is
# O ( n 2 ) O(n 2 ), even though the algorithm logic is quite different.

def count_sequences(n, result={}):
    """
    Calculates the number of valid sequences (balanced parentheses) using dynamic programming
    with momoization to optimize redundant calculation.

    Args:
    n (int): The number of parentheses to form a balanced sequence (n must be even).
    result (dict): A dictionary used for momoization to store previously computed results.

    Returns:
    int: The number of valid balanced sequences for a given n.
    """

    # Base case: when is 0, there is exactly 1 valid sequence (the empty sequence)
    if n == 0:
        return 1
    
    # If the result for n is already computed, return the cached value to avoid redundant calculations
    if n not in result:
        count = 0 # Initialise a variable to accumulate the valid sequence count

        # Loop through even numbers from 2 to n (step size of 2) to divide the sequence into pairs
        for i in range(2, n + 1, 2):
            # Recursively count sequences for the left side (i-2) and right side (n-i)
            # The multiplication comes from the Cartesian product of the left and right sequence
            count += count_sequences(i - 2) * count_sequences(n - i)

        # Store the computed result for n in the dictionary to reuse it later (memoization)
        result[n] = count

    # Return the computed or cached result for n
    return result[n]

print(count_sequences(100)) # 1978261657756160653623774456

# print(count_sequences(2000)) # RecursionError: maximum recursion depth exceeded in comparison”, which means that there are too many nested recursive calls.
import sys
sys.setrecursionlimit(5000)

print(count_sequences(2000)) # 2046105521468021692642519982997827217179245642339057975844538099572176010191891863964968026156453752449015750569428595097318163634370154637380666882886375203359653243390929717431080443509007504772912973142253209352126946839844796747697638537600100637918819326569730982083021538057087711176285777909275869648636874856805956580057673173655666887003493944650164153396910927037406301799052584663611016897272893305532116292143271037140718751625839812072682464343153792956281748582435751481498598087586998603921577523657477775758899987954012641033870640665444651660246024318184109046864244732001962029120

# Changing the recursion limit can be problematic as it can cause problems with python execution environment.
# A better solution is to use loops instead of recursion

def count_sequences(n):
    """
    Calculates the number of valid sequences (balanced parentheses) using dynamic programming.
    This version uses a table to keep track of valid sequences for each state (n, j), where
    n is the number of parentheses to place and j is the balance of parentheses.

    Args:
    n (int): The number of parentheses to form a balanced sequence (n must be even).

    Returns:
    int: The number of valid balanced sequences for a given n.
    """
    
    # Initialize the result dictionary to store the number of valid sequences for each (i, j) pair
    result = {}

    # Base case: There is one valid sequence when no parentheses are placed and the balance is 0
    result[(0, 0)] = 1

    # Initialize invalid cases for j > 0 when no parentheses are placed (no valid sequences here)
    for i in range(1, n + 1):
        result[(0, i)] = 0

    # Fill the result table for all states (i, j) where i is the number of steps left to place parentheses
    # and j is the current balance of parentheses.
    for i in range(1, n + 1):
        for j in range(0, n + 1):
            # Initialize the current state (i, j) to 0
            result[(i, j)] = 0

            # If adding an opening parenthesis '(' increases the balance, calculate the new value
            if j + 1 <= n:
                result[(i, j)] += result[(i - 1, j + 1)]
            
            # If adding a closing parenthesis ')' decreases the balance, calculate the new value
            if j - 1 >= 0:
                result[(i, j)] += result[(i - 1, j - 1)]

    # Return the final number of valid balanced sequences when all parentheses are placed and balance is 0
    return result[(n, 0)]

print(count_sequences(10)) # 42
print(count_sequences(100)) # 1978261657756160653623774456
