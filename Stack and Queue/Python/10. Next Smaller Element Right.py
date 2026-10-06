# Function to find the next smaller element for each element in the array
# same for NSL reverse the loop
def nextSmallerElement(arr, n):
    # list to store the result (next smaller elements)
    v = []
    # Stack to keep track of the next smaller elements
    st = []

    # Traverse the array from the end to the beginning
    for i in range(n - 1, -1, -1):
        # If the stack is empty, there is no smaller element on the right
        if len(st) == 0:
            # No smaller element found, push -1 to result
            v.append(-1)
        # If the stack is not empty and the top element is smaller than arr[i]
        elif len(st) > 0 and st[-1] < arr[i]:
            # Top element is the next smaller, push it to result
            v.append(st[-1])
        # If the stack is not empty and the top element is not smaller than arr[i]
        else:
            # Pop elements from the stack until finding a smaller element or the stack is
            # empty
            while len(st) != 0 and arr[i] <= st[-1]:
                st.pop()

            # If stack is empty, no smaller element found
            if len(st) == 0:
                v.append(-1)
            else:
                # Found a smaller element, push it to result
                v.append(st[-1])

        # Push the current element onto the stack
        st.append(arr[i])

    # Reverse the result list to match the original array order
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
