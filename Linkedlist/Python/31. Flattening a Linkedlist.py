def mergeboth(first, second):
    # Dummy node is used to simplify the merge process
    # This will track the last node in the merged list
    tail = None
    if not first:
        return second
    if not second:
        return first
    # If one of the lists is empty, return the other list
    if first.data <= second.data:
        tail = first
        first = first.bottom
    else:
        tail = second
        second = second.bottom
    # Head points to the start of the merged list
    head = tail
    # Merge both lists
    while first and second:
        if first.data <= second.data:
            tail.bottom = first
            first = first.bottom
        else:
            tail.bottom = second
            second = second.bottom
        tail = tail.bottom
    # Attach the remaining part of the non-empty list
    if first:
        tail.bottom = first
    else:
        tail.bottom = second
    # Return the head of the merged list
    return head


# Recursive flatten function to merge the bottom lists
def flatten(head):
    if not head or not head.next:
        # Base case: single node or end of the list
        return head
    # Flatten the next part of the list
    nextNode = flatten(head.next)
    # Merge the current node's bottom list with the flattened next part
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
