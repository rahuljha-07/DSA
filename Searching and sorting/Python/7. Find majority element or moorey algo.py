def majorityElement(arr):
    count = 0
    candidate = 0

    if len(arr) == 1:
        return arr[0]

    # First pass: Find the candidate for majority element
    for i in range(len(arr)):
        if count == 0:
            candidate = arr[i]

        if candidate == arr[i]:
            count += 1
        else:
            count -= 1

    # Second pass: Verify if the candidate is majority
    count = 0
    for i in range(len(arr)):
        if candidate == arr[i]:
            count += 1

    return candidate if count > len(arr) // 2 else -1


arr = [3, 1, 3, 3, 2]
print(majorityElement(arr))


'''
Time Complexity: O(n)

Reason:
Moore's voting pass scans the array once to find a candidate. A second
scan verifies whether that candidate appears more than n / 2 times.

Space Complexity: O(1)

Reason:
Only candidate and count variables are used.
'''
