def findMinOps(arr):
    # Assumes positive integers. Modifies the input array.
    ans = 0
    n = len(arr)
    i = 0
    j = n - 1

    while i <= j:
        # Equal ends: move both pointers inward.
        if arr[i] == arr[j]:
            i += 1
            j -= 1

        # Left is greater: merge two elements on the right.
        elif arr[i] > arr[j]:
            j -= 1
            arr[j] += arr[j + 1]
            ans += 1

        # Right is greater: merge two elements on the left.
        else:
            i += 1
            arr[i] += arr[i - 1]
            ans += 1

    return ans


arr = [1, 4, 5, 1]
print("Minimum operations to make the array palindrome:", findMinOps(arr))
# Output: Minimum operations to make the array palindrome: 1
# Merge 4 and 5 to get the logical array [1, 9, 1].


# TIME: O(n)
# Each iteration moves at least one pointer inward.
# The pointers cross after at most O(n) iterations.
#
# EXTRA SPACE: O(1)
# Merges update the array directly using a fixed number of variables.
# The array is not physically shortened; pointers track the active portion.

'''
Time Complexity: O(n)

Reason:
The two pointers move inward after every comparison or merge. They cross
after a linear number of operations.

Space Complexity: O(1)

Reason:
The array is updated in place and only pointers plus the answer counter are used.
'''
