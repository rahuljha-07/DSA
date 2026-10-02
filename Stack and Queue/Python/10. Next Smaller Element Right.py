def nextSmallerElement(arr, n):
    v = []
    st = []

    for i in range(n - 1, -1, -1):
        if len(st) == 0:
            v.append(-1)
        elif len(st) > 0 and st[-1] < arr[i]:
            v.append(st[-1])
        else:
            while len(st) != 0 and arr[i] <= st[-1]:
                st.pop()

            if len(st) == 0:
                v.append(-1)
            else:
                v.append(st[-1])

        st.append(arr[i])

    v.reverse()
    return v


arr = [4, 8, 5, 2, 25]
print(nextSmallerElement(arr, len(arr)))


'''
Time Complexity: O(n)

Reason:
Each array element is pushed once and popped at most once from the stack.
Nested popping does not make it quadratic because popped elements never return.

Space Complexity: O(n)

Reason:
The stack and result list can each grow to n elements.
'''
