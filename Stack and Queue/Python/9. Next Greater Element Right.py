# Function to find the next greater element for each element in the array
# same for NGL reverse the loop
def nextLargerElement(arr, n):
    # list to store the result (next greater elements)
    v = []
    # Stack to keep track of the next greater elements
    st = []

    # Traverse the array from the end to the beginning
    for i in range(n - 1, -1, -1):
        # If the stack is empty, there is no greater element on the right
        if len(st) == 0:
            # No greater element found, push -1 to result
            v.append(-1)
        # If the stack is not empty and the top element is greater than arr[i]
        elif len(st) > 0 and arr[i] < st[-1]:
            # Top element is the next greater, push it to result
            v.append(st[-1])
        # If the stack is not empty and the top element is not greater than arr[i]
        elif len(st) > 0 and arr[i] >= st[-1]:
            # Pop elements from the stack until finding a greater element or the stack is
            # empty
            while len(st) > 0 and arr[i] >= st[-1]:
                st.pop()

            # If stack is empty, no greater element found
            if len(st) == 0:
                v.append(-1)
            else:
                # Found a greater element, push it to result
                v.append(st[-1])

        # Push the current element onto the stack
        st.append(arr[i])

    # Reverse the result list to match the original array order
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
