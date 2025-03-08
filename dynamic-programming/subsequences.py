def find_longest(items):
    """
    Finds the length of the longest increasing subsequence in a given list.
    This uses a dynamic programming approach.

    Args:
    items (list): A list of numbers.

    Returns:
    int: The length of the longest increasing subsequence.
    """

    result = {}  # Dictionary to store the length of the longest subsequence ending at each index

    max_len = 0  # Variable to track the overall longest increasing subsequence length

    # Iterate through each element in the list
    for i in range(len(items)):
        result[i] = 1  # By default, the longest subsequence ending at i is 1 (the item itself)

        # Compare with all previous elements
        for j in range(i):
            if items[j] < items[i]:  # Ensure we maintain an increasing order
                result[i] = max(result[i], result[j] + 1)  # Extend the sequence if possible

        # Update the maximum length found so far
        max_len = max(max_len, result[i])

    return max_len  # Return the length of the longest increasing subsequence

print(find_longest([4, 1, 5, 6, 3, 4, 1, 8])) # 4

"""
The time complexity of the algorithm is O ( n 2 ) O(n 2 ), because it has two nested loops.
Since the number of all possible subsequences is O ( 2 n ) O(2 n ), this algorithm is much
faster than a brute force algorithm that iterates through all subsequences.
"""