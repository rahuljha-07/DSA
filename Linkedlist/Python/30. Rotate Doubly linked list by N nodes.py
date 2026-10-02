class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


def length(head):
    len = 0
    temp = head
    while temp is not None:
        len += 1
        temp = temp.next
    return len


def rotate(head, N):
    if head is None or head.next is None or N == 0:
        return head
    len = length(head)
    N = N % len
    if N == 0:
        return head
    newTail = head
    for i in range(1, N):
        newTail = newTail.next
    newHead = newTail.next
    newTail.next = None
    newHead.prev = None
    oldTail = newHead
    while oldTail.next is not None:
        oldTail = oldTail.next
    oldTail.next = head
    head.prev = oldTail
    return newHead


def printList(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


def insert(head, data):
    newNode = Node(data)
    if head is None:
        return newNode
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = newNode
    newNode.prev = temp
    return head


def main():
    head = None
    head = insert(head, 1)
    head = insert(head, 2)
    head = insert(head, 3)
    head = insert(head, 4)
    head = insert(head, 5)
    print("Original List: ", end="")
    printList(head)
    N = 2
    head = rotate(head, N)
    print(f"List after rotating by {N} nodes: ", end="")
    printList(head)


if __name__ == "__main__":
    main()


'''
Let n be the number of nodes and N >= 0 the requested left rotation.
Time: O(n): length scans all n nodes. After N %= n, finding newTail and
oldTail together walks at most another n nodes. Link updates are O(1).
Space: O(1) auxiliary: only pointers, a length, and counters are stored.
Existing nodes are relinked. Demo setup is O(n^2) from repeated insert scans.
'''
