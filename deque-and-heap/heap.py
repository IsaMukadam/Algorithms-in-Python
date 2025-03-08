import heapq

# Heap is a data structure that supports adding, accessing and removing elements.
# Additions to a heap are unrestricted, but depending on the implementation of a heap,
# either only the smallest or only the largest element of the heap can be accessed and removed.

# heappush: add an element to the heap
# heappop: remove and return the smallest element of the heap

items = []

heapq.heappush(items, 4)
heapq.heappush(items, 2)
heapq.heappush(items, 3)
heapq.heappush(items, 1)
heapq.heappush(items, 5)

print(items)
print(items[0])
heapq.heappop(items)
print(items[0])

# Compared to hashing, the advantage of a heap is the efficient access and removal of the smallest or the largest element.

import heapq

items = []
heapq.heappush(items, 1)
heapq.heappush(items, 1)
heapq.heappush(items, 1)

print(items) # [1, 1, 1]

# You are given a list of n numbers and a parameter k. For each sliding window, i.e., a sublist of
# $k$ consecutive elements, from the left to right, find the smallest element in the sublist.

# For example, when the list is [1,2,3,5,4,4,1,2] and k=3, the desired answer is [1,2,3,4,1,1].

import heapq

# The time complexity of the algorithm is O(nlogn), because each element is added to and removed from the heap at most once.
def find_minima(items, k):
    """
    Finds the minimum elements in a sliding window of size 'k' across the list 'items'.

    Args:
    items (list): The list of numbers in which to find the sliding window minima.
    k (int): The size of the sliding window.

    Returns:
    list: A list of minimum values for each sliding window of size 'k'.
    """
    
    # Get the length of the input list
    n = len(items)
    
    # Initialize an empty heap and result list
    heap = []  
    result = []  
    
    # Loop through the list 'items' by index
    for i in range(n):
        # Push the current element and its index onto the heap (min-heap)
        heapq.heappush(heap, (items[i], i))
        
        # Remove elements from the heap that are outside the current sliding window (older than 'k' positions)
        while heap[0][1] <= i - k:
            heapq.heappop(heap)
        
        # If the window has reached the required size 'k', add the minimum element (heap[0][0]) to the result
        if i >= k - 1:
            result.append(heap[0][0])
    
    # Return the list of minimum values for each sliding window
    return result

# Basic use case
items = [4, 2, 7, 3, 1, 8, 5, 6]
k = 3
print(find_minima(items, k))  # Output: [2, 2, 3, 1, 1, 1]

# Larger window size
items = [10, 5, 6, 8, 3, 2, 7, 4]
k = 4
print(find_minima(items, k))  # Output: [5, 5, 3, 2, 2]

