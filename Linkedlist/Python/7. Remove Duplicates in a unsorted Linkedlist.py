def removeDuplicates(head):
    if head is None:
        return None
    seen = set()
    current = head
    nextNode = head.next
    seen.add(current.data)
    while nextNode is not None:
        if nextNode.data in seen:
            current.next = nextNode.next
        else:
            seen.add(nextNode.data)
            current = nextNode
        nextNode = nextNode.next
    return head


'''
Let n be the number of nodes and u the number of unique values.
Time: O(n) expected: each node is visited once, and set membership/insertion
takes O(1) on average. Pathological hash collisions can make it O(n^2).
Space: O(u), at most O(n), auxiliary: seen stores each unique value once.
No new result nodes are created.
'''
