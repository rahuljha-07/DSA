# Function to find the maximum sum from two increasing integer sequences
def maxSumOfSequences(first, second):
    # Sum of the current path in the first sequence
    sum1 = 0
    # Sum of the current path in the second sequence
    sum2 = 0
    # Maximum sum found
    maxSum = 0

    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            # Add to sum1 if current element in first is smaller
            sum1 += first[i]
            i += 1
        elif first[i] > second[j]:
            # Add to sum2 if current element in second is smaller
            sum2 += second[j]
            j += 1
        else:
            # Found an intersection point
            # Add the maximum of both sums plus the intersection value
            maxSum += max(sum1, sum2) + first[i]
            # Reset sum1 for the next segment
            sum1 = 0
            # Reset sum2 for the next segment
            sum2 = 0
            i += 1
            j += 1

    # Add remaining elements in first sequence
    while i < len(first):
        sum1 += first[i]
        i += 1

    # Add remaining elements in second sequence
    while j < len(second):
        sum2 += second[j]
        j += 1

    # Add the maximum of the last sums to the total
    maxSum += max(sum1, sum2)

    # Return the maximum sum
    return maxSum


first = [3, 5, 7, 9, 20, 25, 30, 40, 55, 56, 57, 60, 62]
second = [1, 4, 7, 11, 14, 25, 44, 47, 55, 57, 100]
print(maxSumOfSequences(first, second))


'''
Time Complexity: O(n + m)

Reason:
Both increasing sequences are scanned once with two pointers. Remaining
elements after the last intersection are also scanned once.

Space Complexity: O(1)

Reason:
Only sums and pointer variables are used.
'''
