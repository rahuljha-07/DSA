class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def reverse(head):
    prev = None
    curr = head
    nextNode = None
    while curr is not None:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    return prev


def addOne(head):
    head = reverse(head)
    carry = True
    p = head
    while p is not None and carry:
        if p.next is None and p.data == 9:
            p.data = 0
            temp = Node(1)
            p.next = temp
            p = temp
            carry = False
        elif p.data == 9:
            p.data = 0
            p = p.next
        else:
            p.data = p.data + 1
            p = p.next
            carry = False
    head = reverse(head)
    return head


def addOneUtil(head):
    if head is None:
        return 1
    carry = addOneUtil(head.next)
    sum = head.data + carry
    head.data = sum % 10
    return sum // 10


# Separate name keeps the recursive C++ alternative from replacing addOne.
def addOneRecursive(head):
    carry = addOneUtil(head)
    if carry:
        newHead = Node(carry)
        newHead.next = head
        head = newHead
    return head


'''
Let n be the number of digit nodes, stored most significant digit first.
addOne time: O(n): two full reversals plus at most n carry updates.
addOne space: O(1) auxiliary, with at most one new node for a final carry.
addOneRecursive time: O(n): visits all nodes on descent and updates them
on return. Space: O(n) auxiliary for n pending calls, plus at most one node.
The iterative method preserves the source's empty-input result (None);
the recursive method represents an empty-input increment as a node with 1.
'''
