# Approach
# Sort the Array: Sorting helps to handle the smallest and largest elements systematically.
# Initial Difference: Calculate the initial difference between the tallest and shortest
# towers before any operations.
# Iterate and Adjust Heights: For each tower, calculate the new possible heights after
# either increasing or decreasing by K. Ensure that no height becomes negative.
# Minimize the Difference: While iterating, we compute the difference between the maximum
# and minimum tower heights after the operation and keep track of the minimum possible
# difference.
# Key Points:
# We have to add or subtract K from each element.
# After sorting, the minimum difference will depend on the difference between the largest
# and smallest possible heights after the operations.
def get_min_diff(arr, k):
    n = len(arr)
    if n <= 1:
        return 0

    # Sort the array to handle elements in order.
    arr.sort()

    # Initialize the result as the difference between the max and min height in the sorted
    # array.
    result = arr[n - 1] - arr[0]
    # The smallest possible height and largest possible height after adjusting with k
    smallest = arr[0] + k
    largest = arr[n - 1] - k

    # Traverse through the array to explore the different possibilities
    for i in range(n - 1):
        # Increase towers up to i; decrease towers after i.
        min_height = min(smallest, arr[i + 1] - k)
        max_height = max(largest, arr[i] + k)

        # Skip adjustments that produce a negative height.
        if min_height < 0:
            continue

        # Update the result with the minimum possible difference
        result = min(result, max_height - min_height)

    return result


arr = [1, 5, 8, 10]
k = 2
print(get_min_diff(arr, k))  # 5


# TIME: O(n log n)
# Sorting: O(n log n).
# Loop: n - 1 iterations with O(1) work each = O(n).
# Total: O(n log n) + O(n) = O(n log n).
#
# EXTRA SPACE: O(n) worst case.
# Variables use O(1), but Python's sort may use O(n) temporary memory.

'''
Time Complexity: O(n log n)

Reason:
The array is sorted first, which takes O(n log n). After sorting, one
linear scan checks every split point, so sorting dominates.

Space Complexity: O(n) worst case in Python

Reason:
The algorithm itself uses O(1) variables, but Python sorting may use
extra temporary memory proportional to n.
'''
