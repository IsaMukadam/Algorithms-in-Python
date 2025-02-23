############################## Dictionaries ###################################

# Example Dict Creation
weights = {}

weights["mango"] = 200
weights["banana"] = 110
weights["pea"] = 2

print("Method 1:", weights)

# Another Method to create the same dict
weights = {"mango": 200, "banana": 110, "pea": 2}

print("Method 2:", weights)

# Printing the value for "banana"
print("Banana Weight:", weights["banana"], "g")

# Changing the weight of the banana
weights["banana"] = 120
print("Banana New Weight:", str(weights["banana"]) + "g")

# Checking if the dict has a specific value
print("banana" in weights) # True
print("banan" in weights) # False

# Random function (Pointless but shows you can make functions to shorten existing functions further which can either take away
# or add complexity unnecessarily)
def check_dict(word, dict):
    return word in dict

print(check_dict("banana", weights))

################## Various ways to use a dictionary #####################

# Items Dict
items = ["Pear", "Pear", "Apple", "Cheeseburger", "Pepper", "Pepper", "Pepper"]

# Setting distinct seen variables to True in the seen dict
seen = {}
for x in items:
    seen[x] = True

print(seen)

# Counting occurences
count = {}
for x in items:
    if x not in count:
        count[x] = 0
    count[x] += 1

print(count)




