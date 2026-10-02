def reverse(head):
    p = head
    q = None
    r = None
    while p is not None:
        r = q
        q = p
        p = p.next
        q.next = r
    head = q
    return head


def compute(head):
    head = reverse(head)
    if head is None:
        return None
    cur = head
    max = head.data
    prev = head
    cur = cur.next
    while cur:
        if cur.data >= max:
            max = cur.data
            prev = cur
            cur = cur.next
        else:
            prev.next = cur.next
            cur = prev.next
    head = reverse(head)
    return head


def deleteNodesUtil(head, maxi):
    if head is None:
        maxi[0] = float("-inf")
        return None
    if head.next is None:
        maxi[0] = head.data
        return head
    newHead = deleteNodesUtil(head.next, maxi)
    if head.data < maxi[0]:
        return newHead
    maxi[0] = head.data
    head.next = newHead
    return head


def deleteNodes(head):
    maxi = [float("-inf")]
    return deleteNodesUtil(head, maxi)


'''
Let n be the number of nodes.
compute time: O(n): reverse, scan while tracking the maximum, then reverse
again. Each pass is linear. Space: O(1) auxiliary for pointers and maximum.
deleteNodes time: O(n): recursion visits each node once, and each returning
call either keeps or skips its node in O(1).
Recursive space: O(n) auxiliary for the call stack. maxi is a one-element
holder for the C++ reference parameter, not an n-element collection.
Both approaches relink existing nodes without creating an output list.
'''
