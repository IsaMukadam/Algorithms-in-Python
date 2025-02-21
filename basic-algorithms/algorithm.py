# Creating a function to count the number of even numbers (Easier to understand and convert to other langs)
def count_even(numbers):
    # Resetting the result so you can use this function multiple times
    result = 0
    # For x in a list of numbers check if the number is divisible by 2 then add 1 to the result variable
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

print(count_even([1, 2, 3])) # 1
print("Method 1: " + str(count_even([2, 2, 2, 2, 2, 4]))) # 6
print("Method 1: " + str(count_even([5, 3, 4, 3, 7, 9, 6]))) # 2

# The same method but a more compact version
def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)

print("Method 2: " + str(count_even2([1,2,3,4,5,6,7,8,9])))


# 
