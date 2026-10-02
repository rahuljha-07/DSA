def removeLoop(head):
    if head is None or head.next is None:
        return
    slow = head
    fast = head
    hasCycle = False
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if slow is fast:
            hasCycle = True
            break
    if not hasCycle:
        return
    slow = head
    if slow is fast:
        while fast.next is not slow:
            fast = fast.next
    else:
        while slow.next is not fast.next:
            slow = slow.next
            fast = fast.next
    fast.next = None


def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


def splitList(head):
    if head is None or head.next is None:
        return
    removeLoop(head)
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    secondHalf = slow.next
    slow.next = None
    print("First half: ", end="")
    printList(head)
    print("Second half: ", end="")
    printList(secondHalf)


'''
Let n be the number of distinct reachable nodes.
Time: O(n): removing the cycle, finding the midpoint, and printing both
parts each cost at most O(n); a fixed number of passes is still linear.
Space: O(1) auxiliary: all steps are iterative and reuse existing nodes.
Source behavior is preserved: it removes the circle and prints linear
parts, splitting AFTER the second middle for even lengths. It does not
produce two circular lists or necessarily two equally sized halves.
'''
