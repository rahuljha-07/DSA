def insertAtEndStack(s, val):
    if len(s) == 0:
        s.append(val)
        return

    topElement = s[-1]
    s.pop()

    insertAtEndStack(s, val)

    s.append(topElement)


def performInsertion(s, val):
    insertAtEndStack(s, val)


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
