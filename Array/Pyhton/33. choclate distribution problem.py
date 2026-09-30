def cdp(a, n, m):
    # Assumes 1 <= m <= n and n == len(a).
    a.sort()
    mdiff = float("inf")

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