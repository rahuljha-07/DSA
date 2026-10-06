def majorityElement(arr):
    # Variable to count occurrences and hold the candidate for majority element
    # Counter for occurrences
    count = 0
    # Potential majority element
    candidate = 0

    # Edge case: if the array contains only one element
    if len(arr) == 1:
        return arr[0]

    # First pass: Find the candidate for majority element
    for i in range(len(arr)):
        # If count is zero, select the current element as the candidate
        if count == 0:
            candidate = arr[i]

        # Increment or decrement the count based on the candidate
        if candidate == arr[i]:
            # Increase count if the current element is the candidate
            # Decrease count if the current element is not the candidate
            count += 1
        else:
            count -= 1

    # Second pass: Verify if the candidate is majority
    count = 0
    for i in range(len(arr)):
        if candidate == arr[i]:
            # Count the occurrences of the candidate
            count += 1

    # Check if the count of the candidate is greater than n/2
    # Return candidate if it is the majority, else -1
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
