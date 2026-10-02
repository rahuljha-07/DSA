def threeWayPartition(array, a, b):
    low = 0
    high = len(array) - 1
    mid = 0

    while mid <= high:
        if array[mid] < a:
            # Move elements less than a to the left.
            array[mid], array[low] = array[low], array[mid]
            low += 1
            mid += 1
        elif array[mid] > b:
            # Move elements greater than b to the right.
            array[mid], array[high] = array[high], array[mid]
            high -= 1
            # Check the swapped-in element before advancing mid.
        else:
            # Elements within [a, b] belong in the middle.
            mid += 1


array = [1, 2, 3, 3, 4]
threeWayPartition(array, 1, 2)
print(array)  # [1, 2, 3, 4, 3]


# TIME: O(n)
# Each iteration increases mid or decreases high.
# The unprocessed region shrinks by one, giving n iterations.
#
# EXTRA SPACE: O(1)
# Elements are swapped directly using a fixed number of variables.

'''
Time Complexity: O(n)

Reason:
Each iteration either moves mid forward or high backward, shrinking the
unprocessed region by one.

Space Complexity: O(1)

Reason:
Partitioning happens in place using only low, mid, and high pointers.
'''
