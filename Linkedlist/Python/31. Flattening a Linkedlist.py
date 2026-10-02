def mergeboth(first, second):
    tail = None
    if not first:
        return second
    if not second:
        return first
    if first.data <= second.data:
        tail = first
        first = first.bottom
    else:
        tail = second
        second = second.bottom
    head = tail
    while first and second:
        if first.data <= second.data:
            tail.bottom = first
            first = first.bottom
        else:
            tail.bottom = second
            second = second.bottom
        tail = tail.bottom
    if first:
        tail.bottom = first
    else:
        tail.bottom = second
    return head


def flatten(head):
    if not head or not head.next:
        return head
    nextNode = flatten(head.next)
    head = mergeboth(head, nextNode)
    return head


'''
Let N be the total node count and k the number of sorted bottom lists.
Time: O(N*k) worst-case upper bound: this merges one list with the entire
already-flattened suffix, NOT balanced pairs. Nodes in that suffix may be
scanned again by each earlier merge, up to k-1 times.
For k equal-length lists of m nodes, merge work can be m*(2+3+...+k),
which is O(m*k^2) = O(N*k). For k = 1, flatten returns immediately.
Space: O(k) auxiliary for one recursive call per top-level list; merges
are iterative and reuse nodes. Traverse the result through bottom links;
the source does not clear the original next links.
'''
