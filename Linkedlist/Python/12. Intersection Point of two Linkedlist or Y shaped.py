class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def intersectPoint(head1, head2):
    p = head1
    q = head2
    c1 = 0
    c2 = 0
    while p:
        p = p.next
        c1 += 1
    while q:
        q = q.next
        c2 += 1
    diff = abs(c1 - c2)
    p = head1
    q = head2
    if c1 > c2:
        for i in range(diff):
            p = p.next
    elif c2 > c1:
        for i in range(diff):
            q = q.next
    while p is not q:
        p = p.next
        q = q.next
    if p:
        return p.data
    return -1


'''
Let n and m be the lengths of the acyclic input lists.
Time: O(n + m): count both lengths, advance the longer list by their
difference, then walk together. Each node is visited at most a few times.
Space: O(1) auxiliary: only pointers and length counters are stored.
Intersection means the same node object, not merely equal data.
'''
