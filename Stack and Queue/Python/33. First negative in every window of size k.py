from collections import deque


def printFirstNegativeInteger(arr, n, k):
    ans = []
    q = deque()
    i = 0
    j = 0

    while j < n:
        if arr[j] < 0:
            q.append(arr[j])

        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            if len(q) == 0:
                ans.append(0)
            else:
                ans.append(q[0])
                if arr[i] == q[0]:
                    q.popleft()
            i += 1
            j += 1

    return ans


arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
result = printFirstNegativeInteger(arr, len(arr), k)
for x in result:
    print(x, end=" ")
print()


'''
Time Complexity: O(n)

Reason:
The sliding window moves each pointer forward only. Each negative value is
added to and removed from the queue at most once.

Space Complexity: O(k)

Reason:
The queue stores negative values from the current window, at most k values.
'''
