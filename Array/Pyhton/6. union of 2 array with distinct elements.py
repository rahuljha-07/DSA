def find_union(a, b):
    # A set stores each distinct value only once.
    # Use unique_elements as the name so we do not shadow Python's set().
    unique_elements = set()
    i = 0
    j = 0

    # Add elements from both lists until one list is exhausted.
    while i < len(a) and j < len(b):
        unique_elements.add(a[i])
        unique_elements.add(b[j])
        i += 1
        j += 1

    # Add any remaining elements from a.
    while i < len(a):
        unique_elements.add(a[i])
        i += 1

    # Add any remaining elements from b.
    while j < len(b):
        unique_elements.add(b[j])
        j += 1

    # Return the number of distinct values, not the set itself.
    return len(unique_elements)


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [3, 4, 5, 6, 7]

    print("Union size:", find_union(a, b))

    # Output: Union size: 7


# ---------------------------------------------------------------------------
# HOW IT WORKS: UNION OF TWO ARRAYS
# ---------------------------------------------------------------------------
# The union contains all distinct elements appearing in either array.
#
# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]
#
# Distinct values: 1, 2, 3, 4, 5, 6, 7
# Union size: 7
#
# Adding a duplicate to a set does not create another entry.
# Duplicates within one array or across both arrays are counted only once.
# The arrays do not need to be sorted, and neither array is modified.
#
# If one array is shorter, the remaining loops process the other array.
# If both arrays are empty, the result is 0.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n + m) EXPECTED
# ---------------------------------------------------------------------------
# Time complexity describes how work grows with input size.
# Let n = len(a) and m = len(b).
#
# The first loop processes min(n, m) pairs of elements.
# The remaining loops process the leftover elements.
#
# Every element is added to the set exactly once:
# Total insertion attempts = n + m.
#
# A hash-set insertion takes O(1) on average.
# Therefore, expected total time = (n + m) × O(1) = O(n + m).
#
# These loops run sequentially, so we ADD their costs.
# Having three loops does not mean O(n³).
#
# Pathological worst case: O((n + m)²).
# If many distinct values have colliding hashes, a set insertion can
# take linear time instead of constant time.


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(n + m) WORST CASE
# ---------------------------------------------------------------------------
# Extra space measures additional memory beyond the input arrays.
#
# If there are u distinct values, the set stores u entries: O(u) space.
# In the worst case, all values are distinct, so u = n + m.
# Therefore, worst-case extra space is O(n + m).
#
# The two index variables use only O(1) additional space.

'''
Time Complexity: O(n + m) expected

Reason:
Every element from both arrays is inserted into a set once. Hash-set insert
is O(1) on average, so the total expected work is linear in both lengths.

Space Complexity: O(n + m)

Reason:
In the worst case, all values are distinct and the set stores all elements
from both arrays.
'''
