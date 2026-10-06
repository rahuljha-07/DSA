def reverseGroupRecursive(head, k):
    if not head:
        return None
    if k <= 0:
        raise ValueError("k must be positive")
    current = head
    prev = None
    next = None
    count = 0
    # Reverse first k nodes
    while current and count < k:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1
    # Recursively call for the rest of the list
    if next:
        head.next = reverseGroupRecursive(next, k)
    # prev is now the head of the reversed group
    return prev


'''
Let n be the number of nodes and k > 0 the group size.
Time: O(n): each node is visited and reversed once across all groups.
Space: O(ceil(n / k)) auxiliary: there is one recursive call per group,
including a final partial group. Links are changed in place.
'''
