def maxSumOfSequences(first, second):
    sum1 = 0
    sum2 = 0
    maxSum = 0

    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            sum1 += first[i]
            i += 1
        elif first[i] > second[j]:
            sum2 += second[j]
            j += 1
        else:
            maxSum += max(sum1, sum2) + first[i]
            sum1 = 0
            sum2 = 0
            i += 1
            j += 1

    while i < len(first):
        sum1 += first[i]
        i += 1

    while j < len(second):
        sum2 += second[j]
        j += 1

    maxSum += max(sum1, sum2)

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
