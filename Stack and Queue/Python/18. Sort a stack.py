# Function to print the elements of the stack (for demonstration)
def printStack(s):
    temp = s.copy()
    while len(temp) != 0:
        print(temp[-1], end=" ")
        temp.pop()
    print()


# Recursive function to insert an element in sorted order into a stack
def sortedInsert(s, element):
    # Base case: If the stack is empty or the top element is less than or equal to the
    # element
    if len(s) == 0 or s[-1] <= element:
        s.append(element)
        return

    # Recursive case: Pop the top element and store it
    topElement = s[-1]
    s.pop()

    # Recursive call to insert the element in the remaining stack
    sortedInsert(s, element)

    # Push the popped element back onto the stack
    s.append(topElement)


# Recursive function to sort the stack
def sortStack(s):
    # Base case: If the stack is empty, return
    if len(s) == 0:
        return

    # Recursive case: Pop the top element
    topElement = s[-1]
    s.pop()

    # Recursive call to sort the remaining stack
    sortStack(s)

    # Insert the popped element in sorted order
    sortedInsert(s, topElement)


s = []
s.append(3)
s.append(1)
s.append(4)
s.append(2)

print("Stack before sorting:", end=" ")
printStack(s)
sortStack(s)
print("Stack after sorting:", end=" ")
printStack(s)


'''
Time Complexity: O(n^2)

Reason:
Each element is removed once by sortStack, and sortedInsert may scan through
already sorted elements. This creates quadratic work in the worst case.

Space Complexity: O(n)

Reason:
The recursion stack can grow to n calls.
'''
