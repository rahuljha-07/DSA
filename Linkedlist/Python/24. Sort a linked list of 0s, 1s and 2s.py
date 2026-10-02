class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def segregate(head):
    count = [0, 0, 0]
    temp = head
    while temp:
        count[temp.data] += 1
        temp = temp.next
    temp = head
    i = 0
    while temp:
        if count[i] == 0:
            i += 1
        else:
            temp.data = i
            count[i] -= 1
            temp = temp.next
    return head


def segregateUsingDummy(head):
    zeroDummy = Node(0)
    oneDummy = Node(0)
    twoDummy = Node(0)
    zero = zeroDummy
    one = oneDummy
    two = twoDummy
    curr = head
    while curr:
        if curr.data == 0:
            zero.next = curr
            zero = zero.next
        elif curr.data == 1:
            one.next = curr
            one = one.next
        else:
            two.next = curr
            two = two.next
        curr = curr.next
    two.next = None
    # Skip an empty one-list rather than disconnecting the two-list.
    zero.next = oneDummy.next if oneDummy.next else twoDummy.next
    one.next = twoDummy.next
    sortedHead = zeroDummy.next
    return sortedHead


'''
Let n be the number of nodes; data must be 0, 1, or 2.
Counting time: O(n): one pass counts values, one pass overwrites data,
and i advances only twice. Space: O(1) auxiliary for exactly three counters.
Dummy-list time: O(n): one pass separates nodes, then O(1) links join them.
Space: O(1) auxiliary: exactly three dummy nodes and a fixed set of pointers.
Neither approach allocates a new n-node result list.
'''
