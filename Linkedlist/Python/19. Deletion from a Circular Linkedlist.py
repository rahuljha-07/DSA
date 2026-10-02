def deleteNode(head, value):
    if head is None:
        return head
    if head.next is head and head.data == value:
        head = None
        return head
    temp = head
    prev = None
    if head.data == value:
        last = head
        while last.next is not head:
            last = last.next
        last.next = head.next
        temp = head
        head = head.next
        return head
    while True:
        if temp.data == value:
            prev.next = temp.next
            return head
        prev = temp
        temp = temp.next
        if temp is head:
            break
    return head


'''
Let n be the number of nodes in a list circular back to head.
Time: O(n) worst case: finding the tail when deleting head or searching
for value visits at most one complete circle. Unlinking takes O(1).
Space: O(1) auxiliary: only pointers are used; no new nodes are created.
Return the updated head because Python has no C++ Node*& parameter.
'''
