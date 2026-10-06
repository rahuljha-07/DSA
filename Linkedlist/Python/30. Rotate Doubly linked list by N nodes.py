class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


# Function to find the length of the doubly linked list
def length(head):
    len = 0
    temp = head
    while temp is not None:
        len += 1
        temp = temp.next
    return len


# Function to rotate the doubly linked list by N nodes
def rotate(head, N):
    if head is None or head.next is None or N == 0:
        # No rotation needed for empty or single-node list, or N=0
        return head
    # Step 1: Find the length of the list
    len = length(head)
    # Step 2: If N is greater than the length of the list, take N % length to avoid extra
    # rotations
    N = N % len
    # No rotation needed if N is a multiple of length
    if N == 0:
        return head
    # Step 3: Traverse till N node
    newTail = head
    for i in range(1, N):
        newTail = newTail.next
    # Step 4: The (N + 1)th node becomes the new head
    newHead = newTail.next
    # Step 5: Update the pointers to rotate the list
    # New tail points to None
    newTail.next = None
    # New head's previous pointer becomes None
    newHead.prev = None
    # Find the last node of the list (old tail)
    oldTail = newHead
    while oldTail.next is not None:
        oldTail = oldTail.next
    # The old tail's next pointer should now point to the old head
    oldTail.next = head
    head.prev = oldTail
    # Step 6: Return the new head of the list
    return newHead


# Function to print the doubly linked list
def printList(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


# Helper function to insert nodes at the end of the doubly linked list
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
