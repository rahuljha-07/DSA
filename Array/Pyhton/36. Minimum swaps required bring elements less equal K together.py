def minSwap(arr, n, k):
    # Step 1: Count elements less than or equal to k.
    count = 0
    for i in range(n):
        if arr[i] <= k:
            count += 1

    # Step 2: Count "bad" elements in the first window of size count.
    bad = 0
    for i in range(count):
        if arr[i] > k:
            bad += 1

    # Step 3: Slide the window and find the minimum bad count.
    ans = bad
    i = 0

    for j in range(count, n):
        # Remove the element leaving the window.
        if arr[i] > k:
            bad -= 1

        # Add the element entering the window.
        if arr[j] > k:
            bad += 1

        # Update the answer with the minimum "bad" count
        ans = min(ans, bad)
        i += 1

    return ans


arr = [2, 1, 5, 6, 3]
k = 3
print("Minimum swaps required:", minSwap(arr, len(arr), k))  # 1


# Each bad element inside a window can be swapped with a good element
# outside it. Swaps may exchange any two positions, not just adjacent ones.
#
# TIME: O(n)
# Counting, checking the first window, and sliding each take at most O(n).
# Their sequential costs add to O(n).
#
# EXTRA SPACE: O(1)
# Only a fixed number of variables are used.

'''
Time Complexity: O(n)

Reason:
The code counts good elements, checks the first window, then slides the
window once across the array. These linear steps add to O(n).

Space Complexity: O(1)

Reason:
Only count, bad, ans, and pointer variables are used.
'''
