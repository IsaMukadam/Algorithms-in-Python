############################# EXAMPLE TASK ########################################
#  You have access to an unbounded number of coins with values 1, 2 and 5. 
# What is the minimum number of coins needed to form the sum x? 
# For example, when x = 13, the desired answer is 4, because we can choose
# the coins 1,2,5,5 and there is no solution with fewer coins.

# BRUTE FORCE METHOD
def find_coins(x):
    # Initialize a list called 'solutions' with an empty list inside.
    # This will keep track of the different ways to make change for the amount 'x'.
    solutions = [[]]
    
    # Iterate over each solution (which starts with an empty list).
    for solution in solutions:
        # Check if the sum of the current solution is equal to 'x'.
        # If so, return the length of the solution (the number of coins in it).
        if sum(solution) == x:
            return len(solution)
        
        # For each coin denomination (1, 2, or 5), 
        # create a new solution by appending the coin to the current solution and add it to the 'solutions' list.
        for coin in [1, 2, 5]:
            solutions.append(solution + [coin])

print(find_coins(3))

# ALTERNATIVE BRUTE FORCE METHOD 
def find_coins(x):
    """
    Finds the minimum number of coins needed to make up the given amount `x`
    using denominations of 5, 2, and 1.

    Args:
    x (int): The amount to be converted into coins.

    Returns:
    int: The minimum number of coins required.
    """
    count = 0  # Initialize coin counter
    
    # Iterate through the largest to smallest coin denominations
    for coin in [5, 2, 1]:
        while coin <= x:  # While we can still use this coin
            x -= coin  # Deduct the coin value from the total amount
            count += 1  # Increase the count of coins used
            
    return count  # Return the minimum number of coins

# Example usage
print(find_coins(3))  # Expected output: 2 (2 + 1)

####################################### ALGORITHM CHECKING #############################################

coins = [1, 4, 5]

def find_coins_brute(x):
    solutions = [[]]
    
    for solution in solutions:
        if sum(solution) == x:
            return len(solution)
        for coin in coins:
            solutions.append(solution + [coin])

def find_coins_greedy(x):
    count = 0
    for coin in reversed(coins):
        while coin <= x:
            x -= coin
            count += 1
    return count

x = 1  # Start checking from 1

while True:
    # Compute the number of coins using two different methods
    result_brute = find_coins_brute(x)  # Brute-force approach
    result_greedy = find_coins_greedy(x)  # Greedy approach

    # Check if both methods produce different results
    if result_brute != result_greedy:
        print("Different answer for", x, "coins")
        print("Brute-force result:", result_brute)
        print("Greedy result:", result_greedy)
        break  # Stop execution when a discrepancy is found

    x += 1  # Increment x and check the next number
