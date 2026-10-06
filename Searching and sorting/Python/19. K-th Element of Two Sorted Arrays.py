def kthsmallest(a, b, k):
    n1 = len(a)
    n2 = len(b)

    if n1 > n2:
        return kthsmallest(b, a, k)

    # We can't take more than n1 from a.
    high = min(k, n1)
    # We can't take more than k from b, so we adjust accordingly.
    low = max(0, k - n2)

    while low <= high:
        # Partition positions for both arrays
        mid1 = (low + high) >> 1
        mid2 = k - mid1

        # Edge cases for left and right elements on both sides of the partitions
        # Left element from `a`
        l1 = float('-inf') if mid1 == 0 else a[mid1 - 1]
        # Left element from `b`
        l2 = float('-inf') if mid2 == 0 else b[mid2 - 1]
        # Right element from `a`
        r1 = float('inf') if mid1 == n1 else a[mid1]
        # Right element from `b`
        r2 = float('inf') if mid2 == n2 else b[mid2]

        # Check if we found the correct partition
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        # Adjust search range based on partition conditions
        elif l1 > r2:
            # Move left in `a`
            high = mid1 - 1
        else:
            # Move right in `a`
            low = mid1 + 1

    # In case kth smallest is not found, though logically unreachable
    return 0


a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5
print(kthsmallest(a, b, k))


'''
Time Complexity: O(log(min(n1, n2)))

Reason:
Binary search is done on the smaller array's partition count. Each step
halves the valid partition range and checks boundary values in O(1).

Space Complexity: O(1)

Reason:
Only partition indexes and boundary variables are used.
'''
