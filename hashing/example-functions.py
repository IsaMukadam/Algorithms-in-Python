# Method to find the mode O(n)
def find_mode(numbers):
    count = {}
    # Setting mode variable to the first number
    mode = numbers[0]

    # Runs through the list of numbers input and counts how many of each there are and then the mode is the one with the highest repetition
    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1

        if count[x] > count[mode]:
            mode = x

    return mode

# Example Variables
some_numbers = [1,2,3,45423,432,4,43,4,234,43,234,4,4334,43,43121,331,3,32,3,45,6,7,8,65,3,3,33,3,3,4]
print(find_mode(some_numbers))

# Slow Solution (list) to count the number of rounds O(n^2)
def count_rounds(numbers):
    n = len(numbers)
    
    rounds = 1
    for i in range(1, n):
        if numbers.index(i + 1) < numbers.index(i):
            rounds += 1
            
    return rounds

num_list = [1,2,4,5,6,3,8,7,10,9]
print(count_rounds(num_list))

# Efficient Solution (dictionary) to count the number of rounds O(n)
def count_rounds1(numbers):
    n = len(numbers)

    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i

    rounds = 1
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1

    return rounds

print(count_rounds1(num_list))
