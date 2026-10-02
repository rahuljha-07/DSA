class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


def divide(N, head):
    if not head or not head.next:
        return head
    evenDummy = Node(0)
    oddDummy = Node(0)
    even = evenDummy
    odd = oddDummy
    current = head
    while current:
        if current.data % 2 == 0:
            even.next = current
            even = even.next
        else:
            odd.next = current
            odd = odd.next
        current = current.next
    even.next = oddDummy.next
    odd.next = None
    head = evenDummy.next
    return head


'''
Let n be the actual number of nodes; N is unused, as in the source.
Time: O(n): each node is visited once and attached to either the even
or odd chain in O(1); joining the chains is also O(1).
Space: O(1) auxiliary: two dummy nodes and a fixed number of pointers.
Original nodes are reused, preserving order within each parity group.
'''
