import random

# Brute force method
def best_profit_brute(prices):
    n = len(prices)
    max_profit = 0
    for i in range(n):
        for j in range(i + 1, n):
            max_profit = max(max_profit, prices[j] - prices[i])
    return max_profit

# Optimised Approach
def best_profit_fast(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)  # Track the lowest price
        max_profit = max(max_profit, price - min_price)  # Max profit if sold today
    return max_profit


# Testing 1000 times
for _ in range(1000):  # Run 1000 test cases
    n = random.randint(1, 20)
    prices = [random.randint(1, 10) for _ in range(n)]

    result_brute = best_profit_brute(prices)
    result_fast = best_profit_fast(prices)

    print(prices, result_brute, result_fast)

    if result_brute != result_fast:
        print("ERROR")
        break