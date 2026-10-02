def printStack(s):
    temp = s.copy()
    while len(temp) != 0:
        print(temp[-1], end=" ")
        temp.pop()
    print()


def sortedInsert(s, element):
    if len(s) == 0 or s[-1] <= element:
        s.append(element)
        return

    topElement = s[-1]
    s.pop()

    sortedInsert(s, element)

    s.append(topElement)


def sortStack(s):
    if len(s) == 0:
        return

    topElement = s[-1]
    s.pop()

    sortStack(s)

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
