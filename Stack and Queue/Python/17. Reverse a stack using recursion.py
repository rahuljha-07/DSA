# Function to print the elements of the stack without modifying it
def printStack(s):
    # Create a copy to preserve the original stack
    temp = s.copy()
    while len(temp) != 0:
        print(temp[-1], end=" ")
        temp.pop()
    print()


# Recursive function to insert an element at the bottom of the stack
def insertAtBottom(s, element):
    if len(s) == 0:
        s.append(element)
        return

    topElement = s[-1]
    s.pop()
    insertAtBottom(s, element)
    s.append(topElement)


# Recursive function to reverse the stack
def performReverse(s):
    if len(s) == 0:
        return

    topElement = s[-1]
    s.pop()
    performReverse(s)
    insertAtBottom(s, topElement)


# Function to reverse the stack using recursion
def reverseStack(s):
    performReverse(s)


s = []
s.append(1)
s.append(2)
s.append(3)

print("Stack before reverse:", end=" ")
printStack(s)
reverseStack(s)
print("Stack after reverse:", end=" ")
printStack(s)


'''
Time Complexity: O(n^2)

Reason:
For each popped element, insertAtBottom may traverse the remaining stack.
The total work is 1 + 2 + ... + n.

Space Complexity: O(n)

Reason:
Recursive calls can go n levels deep.
'''
