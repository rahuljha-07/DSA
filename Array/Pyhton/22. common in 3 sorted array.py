def common_elements(a, b, c):
    common = set()  # Stores unique common values.
    i = j = k = 0

    n1 = len(a)
    n2 = len(b)
    n3 = len(c)

    while i < n1 and j < n2 and k < n3:
        if a[i] == b[j] and b[j] == c[k]:
            common.add(a[i])
            i += 1
            j += 1
            k += 1
        else:
            # Advance the pointer with the smallest current value.
            if a[i] <= b[j] and a[i] <= c[k]:
                i += 1
            elif b[j] <= a[i] and b[j] <= c[k]:
                j += 1
            else:
                k += 1

    # Convert the set to a sorted list.
    return sorted(common)


if __name__ == "__main__":
    a = [1, 5, 10, 20, 40, 80]
    b = [6, 7, 20, 80, 100]
    c = [3, 4, 15, 20, 30, 70, 80, 120]

    print("Common elements:", common_elements(a, b, c))
    # Output: Common elements: [20, 80]

    print(common_elements([1, 1, 2], [1, 1, 3], [1, 1, 4]))
    # Output: [1] — duplicates appear only once.


# ---------------------------------------------------------------------------
# HOW IT WORKS
# ---------------------------------------------------------------------------
# Use one pointer for each sorted array.
#
# If all three current values match:
# - Add the value to the set.
# - Move all three pointers forward.
#
# Otherwise, move the pointer with the smallest value.
#
# Why move the smallest?
# Suppose the current values are 5, 7, and 10.
# The arrays are sorted, so the remaining values in the third array
# are all at least 10. The current 5 cannot match them.
# We can safely skip it and advance its pointer.
#
# If two values tie for smallest, advancing either one is safe.
# The next iteration will compare the new current values.
#
# Stop as soon as any array is exhausted:
# no further value can be found in all three arrays.
#
# The set removes duplicates; sorted(common) returns an ordered list.
# If any input is empty, the result is [].
# The input arrays are not modified.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n1 + n2 + n3 + u log u) EXPECTED
# ---------------------------------------------------------------------------
# n1, n2, n3 are the input lengths.
# u is the number of DISTINCT common values.
#
# Each iteration advances at least one pointer.
# No pointer moves backward, so the total scan is O(n1 + n2 + n3).
# Set insertion takes O(1) on average.
#
# Sorting the u unique common values takes O(u log u) worst-case time.
#
# Add these sequential costs:
# O(n1 + n2 + n3) + O(u log u).
#
# Pathological hash collisions can make set insertions slower;
# the expected bound assumes average O(1) set operations.


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(u)
# ---------------------------------------------------------------------------
# The set stores u unique common values.
# The returned sorted list also stores u values.
# Sorting may use O(u) temporary memory.
#
# Total: O(u), with O(1) additional pointer variables.

'''
Time Complexity: O(n1 + n2 + n3 + u log u)

Reason:
The three pointers only move forward, so scanning costs O(n1 + n2 + n3).
The unique common values are sorted at the end, costing O(u log u).

Space Complexity: O(u)

Reason:
The set and returned list store u unique common elements.
'''
