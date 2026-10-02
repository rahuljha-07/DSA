def moveLastToFront(head):
    if head is None or head.next is None:
        return head
    secondLast = None
    last = head
    while last.next is not None:
        secondLast = last
        last = last.next
    secondLast.next = None
    last.next = head
    head = last
    return head


'''
Let n be the number of nodes.
Time: O(n): finding the last and second-last nodes requires one traversal;
the final pointer updates take O(1).
Space: O(1) auxiliary: only two pointers are needed and nodes are reused.
'''
