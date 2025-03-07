import itertools  # Import itertools for generating all possible sequences

def count_sequences(n):
    """
    Counts the number of valid balanced parentheses sequences of length n.
    A valid sequence has matching opening '(' and closing ')' brackets.
    """
    count = 0  # Initialize a counter for valid sequences

    # Generate all possible sequences of length 'n' using '(' and ')'
    for sequence in itertools.product("()", repeat=n):
        if valid_sequence(sequence):  # Check if the sequence is valid
            count += 1  # Increment count if valid

    return count  # Return the total count of valid sequences


def valid_sequence(sequence):
    """
    Checks if a given sequence of parentheses is valid.
    A sequence is valid if:
    - At no point do closing brackets ')' exceed opening brackets '('.
    - The final depth (balance) is exactly 0.
    """
    depth = 0  # Track the balance of parentheses

    for bracket in sequence:  # Iterate over each bracket in the sequence
        if bracket == "(":  
            depth += 1  # Increase depth for opening bracket '('
        if bracket == ")":
            depth -= 1  # Decrease depth for closing bracket ')'

        if depth < 0:  
            return False  # If depth goes negative, sequence is invalid

    return depth == 0  # Return True if the sequence is balanced (depth is 0)

print(count_sequences(2)) # 1
print(count_sequences(10)) # 42
print(count_sequences(20)) # 16796

########################## Improved count_sequences() method ##############################

def count_sequences_v2(n, d=0):
    """
    Recursively counts the number of valid balanced parentheses sequences of length n.
    
    Parameters:
    - n: Remaining number of brackets to place.
    - d: Current depth (balance of '(' and ')').
    
    A valid sequence must:
    - Never have more ')' than '(' at any point (d >= 0).
    - Finish with a depth of exactly 0.
    
    Base cases:
    - If depth `d` goes negative or exceeds `n`, return 0 (invalid sequence).
    - If `n` reaches 0, return 1 if depth `d` is exactly 0 (valid sequence).
    
    Recursive case:
    - Add an opening '(' (increase depth).
    - Add a closing ')' (decrease depth).
    
    Returns:
    - The count of valid sequences.
    """

    # If depth goes negative or exceeds the remaining brackets, sequence is invalid
    if d < 0 or d > n:
        return 0

    # If no brackets left, check if depth is 0 (valid sequence)
    if n == 0:
        return 1 if d == 0 else 0

    # Recursively try adding '(' (increase depth) and ')' (decrease depth)
    return count_sequences_v2(n - 1, d + 1) + count_sequences_v2(n - 1, d - 1)


# Test cases to demonstrate the function

# For n = 4 (4 brackets), there are 2 valid sequences: ('()', '()')
print(count_sequences_v2(4))  # Output: 2

# For n = 6 (6 brackets), there are 5 valid sequences
print(count_sequences_v2(6))  # Output: 5

# For n = 8 (8 brackets), there are 14 valid sequences
print(count_sequences_v2(8))  # Output: 14

# Edge case: n = 0, no brackets to arrange, hence 1 valid sequence (empty sequence)
print(count_sequences_v2(0))  # Output: 1

# Edge case: n = 2 (smallest valid sequence), only 1 valid sequence '()'
print(count_sequences_v2(2))  # Output: 1

# Invalid test: Try n = 5, which cannot have balanced parentheses
print(count_sequences_v2(5))  # Output: 0
