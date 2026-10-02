class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def findIntersection(head1, head2):
    first = head1
    second = head2
    res = None
    cur = None
    while first and second:
        if first.data < second.data:
            first = first.next
        elif first.data > second.data:
            second = second.next
        else:
            temp = Node(first.data)
            if res is None:
                res = temp
                cur = temp
            else:
                cur.next = temp
                cur = cur.next
            first = first.next
            second = second.next
    return res


'''
Let n and m be the sorted input lengths and r the number of result nodes.
Time: O(n + m): each iteration advances at least one pointer, and neither
pointer moves backward. Matching values are appended in O(1) using cur.
Space: O(1) auxiliary for pointers; O(r) output space for common-value nodes,
where r <= min(n, m). Neither input list is copied in full.
'''
