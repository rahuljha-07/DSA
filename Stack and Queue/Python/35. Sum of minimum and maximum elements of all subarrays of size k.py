from collections import deque


def sumOfMinAndMax(arr, k):
    n = len(arr)
    if n < k or k <= 0:
        return 0

    maxDeque = deque()
    minDeque = deque()
    sum = 0

    i = 0
    j = 0

    while j < n:
        while len(maxDeque) != 0 and maxDeque[-1] < arr[j]:
            maxDeque.pop()
        maxDeque.append(arr[j])

        while len(minDeque) != 0 and minDeque[-1] > arr[j]:
            minDeque.pop()
        minDeque.append(arr[j])

        if j - i + 1 == k:
            sum += maxDeque[0] + minDeque[0]

            if maxDeque[0] == arr[i]:
                maxDeque.popleft()
            if minDeque[0] == arr[i]:
                minDeque.popleft()

            i += 1
        j += 1

    return sum


arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = sumOfMinAndMax(arr, k)
print("Sum of min and max of all subarrays of size", str(k) + ":", result)


'''
Time Complexity: O(n)

Reason:
Each element is inserted and removed from the max deque and min deque at most
once while the sliding window moves.

Space Complexity: O(k)

Reason:
Each deque stores candidates from the current window, bounded by k elements.
'''
