class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.random = None


def cloneList(head):
    if head is None:
        return None
    cloneHead = None
    cloneCurr = None
    curr = head
    while curr:
        newNode = Node(curr.data)
        if cloneHead is None:
            cloneHead = cloneCurr = newNode
        else:
            cloneCurr.next = newNode
            # The C++ source omitted this assignment.
            cloneCurr = cloneCurr.next
        curr = curr.next
    curr = head
    cloneCurr = cloneHead
    while curr:
        temp = curr.next
        curr.next = cloneCurr
        cloneCurr.random = curr
        curr = temp
        cloneCurr = cloneCurr.next
    curr = head
    cloneCurr = cloneHead
    while cloneCurr:
        cloneCurr.random = (cloneCurr.random.random.next
                            if cloneCurr.random.random else None)
        cloneCurr = cloneCurr.next
    return cloneHead


'''
Let n be the number of nodes; random must point inside the list or be None.
Time: O(n): three passes create nodes, map originals to clones using
next links, and translate random links. Each pass does O(1) work per node.
Space: O(1) auxiliary for traversal pointers; O(n) output for cloned nodes.
Source behavior is preserved: original next links are overwritten to point
to clones and are NOT restored. No dictionary or extra n-node mapping
is introduced.
'''
