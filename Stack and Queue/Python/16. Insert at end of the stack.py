# Recursive function to insert a value at the end of a stack
def insertAtEndStack(s, val):
    # Base case: If the stack is empty, push the value
    if len(s) == 0:
        s.append(val)
        return

    # Recursive case: Pop the top element
    topElement = s[-1]
    s.pop()

    # Recursive call to insert the value into the remaining stack
    insertAtEndStack(s, val)

    # Push the popped element back onto the stack
    s.append(topElement)


# Function to perform the insertion of a value into the stack
def performInsertion(s, val):
    # Insert value at the end of the stack
    insertAtEndStack(s, val)


# Function to print the elements of the stack (for demonstration)
def printStack(s):
    temp = s.copy()
    while len(temp) != 0:
        print(temp[-1], end=" ")
        temp.pop()
    print()


s = []
s.append(1)
s.append(2)
s.append(3)

print("Stack before insertion:", end=" ")
printStack(s)
performInsertion(s, 4)
print("Stack after inserting 4 at the end:", end=" ")
printStack(s)


'''
Time Complexity: O(n)

Reason:
To insert at the bottom, all n existing stack elements are popped and then
pushed back once.

Space Complexity: O(n)

Reason:
The recursion stack can contain n calls.
'''
