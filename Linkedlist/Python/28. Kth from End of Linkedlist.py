def findKthFromEnd(head, k):
    if head is None:
        return None
    node = findKthFromEnd(head.next, k)
    k[0] -= 1
    if k[0] == 0:
        return head
    return node


def getKthFromEnd(head, k):
    return findKthFromEnd(head, [k])


def getNthFromLast(head, n):
    if head is None or n <= 0:
        return -1
    primary = head
    follower = head
    count = 1
    while count < n:
        if primary.next is None:
            return -1
        primary = primary.next
        count += 1
    while primary.next is not None:
        primary = primary.next
        follower = follower.next
    return follower.data


'''
Let L be the number of nodes and k/n the requested position from the end.
Recursive time: O(L): reaches the tail and decrements k once per returning
call. Space: O(L) auxiliary for the stack; [k] is a constant-size reference
holder so all calls share the same counter, like C++ int&.
Iterative time: O(L): primary advances at most L-1 times overall, first
to create the gap and then alongside follower. Space: O(1) auxiliary.
Neither method allocates result nodes.
'''
