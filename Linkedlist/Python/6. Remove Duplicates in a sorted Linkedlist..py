def removeDuplicates(head):
    if head is None or head.next is None:
        return head
    current = head
    nextNode = head.next
    while nextNode is not None:
        if current.data != nextNode.data:
            current = nextNode
            nextNode = nextNode.next
        else:
            current.next = nextNode.next
            nextNode = current.next
    return head


'''
Let n be the number of nodes; the input must be sorted.
Time: O(n): nextNode advances to the following node on every iteration.
Adjacent equal values can be removed without searching the rest of the list.
Space: O(1) auxiliary: two pointers suffice; existing links are changed
and no collection or new list is allocated.
'''
