class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def findmiddle(cur):
    slow = cur
    # Starting fast one node ahead ensures a two-node list actually splits.
    fast = cur.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    first = cur
    second = slow.next
    slow.next = None
    return first, second


def mergeboth(first, second):
    dummy = Node(0)
    tail = dummy
    while first and second:
        if first.data <= second.data:
            tail.next = first
            first = first.next
        else:
            tail.next = second
            second = second.next
        tail = tail.next
    tail.next = first if first else second
    result = dummy.next
    return result


def mergesorting(head):
    cur = head
    if not cur or not cur.next:
        return head
    first, second = findmiddle(cur)
    first = mergesorting(first)
    second = mergesorting(second)
    head = mergeboth(first, second)
    return head


def mergeSort(head):
    head = mergesorting(head)
    return head


'''
Let n be the number of nodes.
Time: O(n log n): splitting and merging together scan O(n) nodes per
recursion level. Halving each list gives O(log n) levels.
Space: O(log n) auxiliary: balanced recursive calls stay on the stack.
Merging is iterative, reuses input nodes, and needs one temporary dummy
node per active merge rather than an O(n) copied array.
'''
