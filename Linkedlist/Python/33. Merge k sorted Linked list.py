def mergesort(first, second):
    if first is None:
        return second
    if second is None:
        return first
    third = None
    last = None
    if first.data < second.data:
        third = last = first
        first = first.next
        last.next = None
    else:
        third = last = second
        second = second.next
        last.next = None
    while first is not None and second is not None:
        if first.data < second.data:
            last.next = first
            last = first
            first = first.next
            last.next = None
        else:
            last.next = second
            last = second
            second = second.next
            last.next = None
    if first is not None:
        last.next = first
    else:
        last.next = second
    return third


def mergeKLists(arr, k):
    if k <= 0:
        return None
    last = k - 1
    while last != 0:
        i = 0
        j = last
        while i < j:
            arr[i] = mergesort(arr[i], arr[j])
            i += 1
            j -= 1
            if i >= j:
                last = j
    return arr[0]


'''
Let N be the total node count and k the number of sorted input lists.
Time: O(N log k) for k >= 2: each round pairs lists and approximately
halves the number of active lists. There are O(log k) rounds, with at
most O(N) node visits per round. k = 1 returns its head in O(1).
Space: O(1) auxiliary beyond the supplied O(k) array of list heads:
merges are iterative, update arr in place, and reuse existing nodes.
Empty lists and k = 0 are handled without dereferencing missing nodes.
'''
