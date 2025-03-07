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
