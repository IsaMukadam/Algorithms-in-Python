# Method to count ways 0 can be on the left and 1 can be on the right

# O(n^2)
def count_ways(bits):
    n = len(bits)
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            if bits[i] == '0' and bits[j] == '1':
                result += 1
    return result

# O(n)
def count_ways2(bits):
    n = len(bits)
    result = 0
    zeros = 0
    for i in range(len(bits)):
        if bits[i] == '0':
            zeros += 1
        if bits[i] == '1':
            result += zeros
    return result

# Checking the time and running the functions
import random
import time

n = 10000
random.seed(1337)

# Generating random set of 0s and 1s
bit_array = [random.randint(0, 1) for _ in range(n)]  # Random 0s and 1s

start_time = time.time()
count_ways(bit_array)
end_time = time.time()

print("time:", round(end_time - start_time, 2), "s")

start_time = time.time()
count_ways2(bit_array)
end_time = time.time()

print("time:", round(end_time - start_time, 2), "s")

# Results #
# time: 1.53 s
# time: 0.0 s