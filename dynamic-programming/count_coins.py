def count_coins(x, coins):
    """
    Counts the number of different ways to make up the amount 'x' using the given coin denominations.
    This uses a dynamic programming approach to solve the Coin Change problem.

    Args:
    x (int): The total amount to be formed.
    coins (list): A list of available coin denominations.

    Returns:
    int: The total number of ways to form 'x' using the given coins.
    """

    result = {}  # Dictionary to store the number of ways to form each amount

    result[0] = 1  # Base case: There is 1 way to make amount 0 (by using no coins)

    # Iterate through all amounts from 1 to x
    for s in range(1, x + 1):
        result[s] = 0  # Initialize with 0 ways

        # Check for each coin denomination
        for coin in coins:
            if s - coin >= 0:  # Ensure we don't go below zero
                result[s] += result[s - coin]  # Add ways from the remaining amount

    return result[x]  # Return the total number of ways to form 'x'

print(count_coins(13, [1, 2, 5])) # 634
print(count_coins(13, [1, 4, 5])) # 88
print(count_coins(42, [1, 5, 6, 17])) # 1103532