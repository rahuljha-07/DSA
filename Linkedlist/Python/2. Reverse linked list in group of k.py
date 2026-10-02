def reverseGroupRecursive(head, k):
    if not head:
        return None
    if k <= 0:
        raise ValueError("k must be positive")
    current = head
    prev = None
    next = None
    count = 0
    while current and count < k:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1
    if next:
        head.next = reverseGroupRecursive(next, k)
    return prev


'''
Let n be the number of nodes and k > 0 the group size.
Time: O(n): each node is visited and reversed once across all groups.
Space: O(ceil(n / k)) auxiliary: there is one recursive call per group,
including a final partial group. Links are changed in place.
'''
