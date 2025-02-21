# Creating a function to count the number of even numbers (Easier to understand and convert to other langs)
def count_even(numbers):
    # Resetting the result so you can use this function multiple times
    result = 0
    # For x in a list of numbers check if the number is divisible by 2 then add 1 to the result variable
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

#print(count_even([1, 2, 3])) # 1
#print("Method 1: " + str(count_even([2, 2, 2, 2, 2, 4]))) # 6
#print("Method 1: ", count_even([5, 3, 4, 3, 7, 9, 6])) # 2

# The same method but a more compact version
def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)

#print("Method 1:", count_even2([1,2,3,4,5,6,7,8,9]))


# Checking the difference between the smallest and largest numbers - method 1
def max_diff(numbers):
    result = 0
    for x in numbers:
        for y in numbers:
            result = max(result, abs(x-y))
    return result

#print("Max Diff:")
#print(max_diff([1,2,3,4,5,6,7,8,9]))

# Checking the difference between the smallest and largest numbers - method 2
def max_diff2(numbers):
    numbers = sorted(numbers)
    return numbers[-1] - numbers[0]

#print("Max Diff 2: " + str(max_diff2([1,22,3,4,5,6,7,8,9,91])))

# Checking the difference between the smallest and largest numbers - method 3
def max_diff3(numbers):
    return max(numbers) - min(numbers)

#print("Max Diff 3:", max_diff3([13,12,33,44,55,26,37,48,39]))

############## Measuring the efficiency of methods 1-3 #################
import random
import time

n = 1000
# print("n: ", n)
random.seed(1337)
numbers = [random.randint(1, 10**6) for _ in range(n)]

start_time = time.time()
result = max_diff3(numbers)
end_time = time.time()

#print("result:", result)
#print("time:", round(end_time - start_time, 2), "s")

#------------ For 1,000 numbers ------------#
# Max diff 1 - 0.11s
# Max diff 2 - 0.0s
# Max diff 3 - 0.0s

#------------ For 10,000 numbers -----------#
# Max diff 1 - 10.51s
# Max diff 2 - 0.0s
# Max diff 3 - 0.0s

#---------- For 1,000,000 numbers ----------#
# Max diff 1 - Too long
# Max diff 2 - 0.19s
# Max diff 3 - 0.01s

# Time complexity of an Algorithm #

"""
Often we do not need to determine the exact number of steps, but it is enough to know the time complexity,
which gives the magnitude of the number of steps on a given input size.

A time complexity is usually shown in the form O(⋯), where the three dots are replaced by an arithmetic 
expression representing an upper bound on the number of steps. The expression involves a variable n that
 represents the size of the input. For example, if the input is a list, n is the length of the list, and 
if the input is a string, n is the length of the string.

The time complexity expression is typically a simplified form of the expression for the exact number of steps,
obtained by retaining only the fastest growing term of the expression and removing all constants. For example,
the time complexity of the preceding algorithm is O(n) because the exact number of steps is at most 3n+2.

Formally, the time complexity of an algorithm is 

O(f(n)) if we can choose two constants c and n0 so that the algorithm executes at most cf(n) steps when n≥nO.
For example, the preceding algorithm has time complexity O(n) because we can choose c=5 and n0=1. These are
valid choices because 3n+2≤5n when n≥1.

################################################
# Time complexity	# Name of complexity class # 
################################################
#    O(1)	        #        Constant          #
#    O(log n)	    #       Logarithmic        #
#    O(n)	        #         Linear           #
#    O(n log n)	    #            –             #
#    O(n^2)	        #        Quadratic         #
#    O(n^3)	        #          Cubic           #
################################################

"""

# time complexity of O(1)
def middle(numbers):
    n = len(numbers)
    return numbers[n // 2]

# print(middle([1,2,3,4,6,7,8,9]))

# Single loop O(n)
def calc_sum(numbers):
    result = 0
    for x in numbers:
        result += x
    return result

# print(calc_sum([1,2,3,4,6,7,8,9]))

# A nested loop is quadratic O(n^2) [^2 changes depending on number of nested loops]
def has_sum(numbers, x):
    for a in numbers:
        for b in numbers:
            if a + b == x:
                return True
    return False

#print(has_sum([1,2,3,4,6,7,8,9], 2))
#print(has_sum([1,2,3,4,6,7,8,9], 231))

# Sequential Code Segments 0(n)
def count_min(numbers):
    # stage 1 - is O(n)
    min_value = numbers[0]
    for x in numbers:
        if x < min_value:
            min_value = x

    # stage 2 - is O(n)
    result = 0 
    for x in numbers:
        if x == min_value:
            result += 1

    return result

# print(count_min([1,2,3,4,6,7,8,9])) # 1