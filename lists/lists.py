a = 1
b = 2
c = [1,2,3,4,5]
d = 99

######## List starts from 0 ########

# print(c[0]) # 1
# print(c[1]) # 2

########## Length of list ##########

# print(len(c)) # 5

########## Searching a list ########

# print(3 in c) # True
# print(123 in c) # False

# Position
# print(c.index(3)) # 2
# How many of the value are in the list
# print(c.count(3)) # 1

####### Appending & Inserting #######
num_list = [1,2,3,4]

# num_list.append(5)
# print(num_list)

# num_list.insert(0, 5)
# print(num_list)

######## Removing Elements ##########

# num_list.pop()
# print(num_list)

# num_list.pop()
# print(num_list)

# num_list.remove(3)
# print(num_list)

######### Reference & Copying ##########

num_list2 = num_list.copy()
num_list.append(5)

# print(num_list) # [1, 2, 3, 4, 5]
# print(num_list2) # [1, 2, 3, 4]

######### Side Effects of Functions #########

def double(numbers):
    result = numbers
    for i in range(len(result)):
        result[i] *= 2
    return result

# print(double(num_list2))
# print(num_list2) # [2, 4, 6, 8]

################ Slicing & Concatenation ##################

# Slicing
numbs = [1,2,3,4,5,6,7,8,9]
# print(numbs[2:6])

# Concatenating
a_list = [1,2,3,4]
b_list = [5,6,7,8,9,10]

# print(a_list+b_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



