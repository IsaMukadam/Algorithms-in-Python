# Function to check the max profit with time complexity O(n^2)
def max_gain(values):
    no_of_values = len(values)
    highest = 0
    for x in range(no_of_values):
        for y in range(x + 1, no_of_values):
            highest = max(highest, values[y] - values[x])
    return highest

# New function reducing time complexity to O(n)
def max_gain2(values):
    no_of_values = len(values)
    highest_return = 0
    min_price = values[0]
    for i in range(no_of_values):
        min_price = min(min_price, values[i])
        highest_return = max(highest_return, values[i] - min_price)
    return highest_return

# Checking the time and running the functions
import random
import time

# Price list
n = 1000
random.seed(1337)
price_list = [random.randint(1, 10**6) for _ in range(n)]

start_time = time.time()
result = max_gain(price_list)
end_time = time.time()

print(result)
print("time:", round(end_time - start_time, 2), "s")

start_time = time.time()
result2 = max_gain2(price_list)
end_time = time.time()

print(result2)
print("time:", round(end_time - start_time, 2), "s")

##### RESULTS #######
# Method 1
# 999266
# time: 0.06 s

# Method 2
# 999266
# time: 0.0 s
