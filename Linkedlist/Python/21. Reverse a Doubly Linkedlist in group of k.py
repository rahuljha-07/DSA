class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


def reverseGroup(head, k):
    if not head:
        return None
    if k <= 0:
        raise ValueError("k must be positive")
    curr = head
    temp = None
    prev = None
    count = 0
    # Detach the group boundary before swapping next/prev.
    head.prev = None
    # Step 1: Reverse the first 'k' nodes using your logic
    while curr is not None and count < k:
        # Store previous node
        temp = curr.prev
        # Swap pointers
        curr.prev = curr.next
        # Complete swap
        curr.next = temp
        # Update 'prev' (new head for the group)
        prev = curr
        # Move to next node (using swapped pointer)
        curr = curr.prev
        count += 1
    prev.prev = None
    # Step 2: Connect with the next group (recursive call)
    if curr is not None:
        # Recurse for next group
        head.next = reverseGroup(curr, k)
        if head.next is not None:
            # Maintain doubly link
            head.next.prev = head
    # 'prev' is the new head of this group
    return prev


# Function to print the doubly linked list
def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print("NULL")


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next
    head.next.next.next.next = Node(5)
    head.next.next.next.next.prev = head.next.next.next
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.prev = head.next.next.next.next
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.prev = head.next.next.next.next.next
    head.next.next.next.next.next.next.next = Node(8)
    head.next.next.next.next.next.next.next.prev = head.next.next.next.next.next.next
    print("Original list: ", end="")
    printList(head)
    k = 3
    head = reverseGroup(head, k)
    print(f"Reversed in groups of {k}: ", end="")
    printList(head)


if __name__ == "__main__":
    main()


'''
Let n be the number of nodes and k > 0 the group size.
Time: O(n): each node's two links are swapped once; reconnecting each
group costs O(1). The final partial group is also reversed.
Space: O(ceil(n / k)) auxiliary: one recursive call per group waits on
the stack. Nodes are reused, and boundary links are fixed in place.
'''
