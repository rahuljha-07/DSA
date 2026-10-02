def nextLargerElement(arr, n):
    v = []
    st = []

    for i in range(n - 1, -1, -1):
        if len(st) == 0:
            v.append(-1)
        elif len(st) > 0 and arr[i] < st[-1]:
            v.append(st[-1])
        elif len(st) > 0 and arr[i] >= st[-1]:
            while len(st) > 0 and arr[i] >= st[-1]:
                st.pop()

            if len(st) == 0:
                v.append(-1)
            else:
                v.append(st[-1])

        st.append(arr[i])

    v.reverse()
    return v


arr = [1, 3, 2, 4]
print(nextLargerElement(arr, len(arr)))


'''
Time Complexity: O(n)

Reason:
Each element is pushed to the stack once and popped at most once. The total
number of stack operations is linear.

Space Complexity: O(n)

Reason:
The result list and stack can each store up to n elements.
'''
