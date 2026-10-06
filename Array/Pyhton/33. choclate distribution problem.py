def cdp(a, n, m):
    # Assumes 1 <= m <= n and n == len(a).
    # Sort packets so any candidate group of m packets is a consecutive window.
    a.sort()
    mdiff = float("inf")

    # Try every group of m packets; the endpoints give its maximum-minus-minimum difference.
    for i in range(n - m + 1):
        diff = a[i + m - 1] - a[i]
        if diff < mdiff:
            mdiff = diff

    return mdiff


a = [7, 3, 2, 4, 9, 12, 56]
m = 3
print(cdp(a, len(a), m))  # 2


# TIME: O(n log n)
# Sorting takes O(n log n); the loop takes O(n).
#
# EXTRA SPACE: O(n) worst case.
# Python's sort may use O(n) temporary memory.
# The loop itself uses O(1) extra space.

'''
Time Complexity: O(n log n)

Reason:
The packets are sorted first. Then a window of size m is checked across
the sorted array in O(n), so sorting dominates.

Space Complexity: O(n) worst case in Python

Reason:
The loop uses O(1), but Python sorting may allocate temporary memory.
'''
