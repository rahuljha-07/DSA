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


def addTwoLists(first, second):
    first = reverse(first)
    second = reverse(second)
    sum = 0
    carry = 0
    res = None
    while first is not None or second is not None:
        sum = carry + (first.data if first else 0) + (second.data if second else 0)
        carry = sum // 10
        sum = sum % 10
        temp = Node(sum)
        if res is not None:
            temp.next = res
        res = temp
        if first:
            first = first.next
        if second:
            second = second.next
    if carry > 0:
        temp = Node(carry)
        temp.next = res
        res = temp
    return res


'''
Let n and m be the lengths of the most-significant-digit-first input lists.
Time: O(n + m): reversing both lists costs n + m steps; addition processes
at most max(n, m) digit positions, plus one possible final carry.
Space: O(1) auxiliary for pointers and carry; O(max(n, m)) output space
for newly created sum nodes. Like the C++ version, input links are reversed
and are not restored.
'''
