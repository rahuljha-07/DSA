class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


# Function to reverse the linked list
def reverse(head):
    prev = None
    curr = head
    nextNode = None
    while curr is not None:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    # New head after reversing
    return prev


# Function to add one to the number represented by the linked list
def addOne(head):
    # Step 1: Reverse the linked list
    head = reverse(head)
    # To track carry over
    carry = True
    # Pointer to traverse the list
    p = head
    while p is not None and carry:
        if p.next is None and p.data == 9:
            # Set the last node to 0 (carry)
            p.data = 0
            # Create a new node for carry
            temp = Node(1)
            # Link the new node
            p.next = temp
            # Move to the new node
            p = temp
            # No more carry, we are done
            carry = False
        # If the current node is 9, set it to 0 and move to the next
        elif p.data == 9:
            # Set current node to 0
            p.data = 0
            # Move to the next node
            p = p.next
        # If it's not 9, just add 1 and stop
        else:
            # Add 1 to the current node
            p.data = p.data + 1
            p = p.next
            # No carry is left, so break the loop
            carry = False
    # Step 2: Reverse the list back to original order
    head = reverse(head)
    # Return the modified list
    return head


# using recursion
# Recursive function to add +1 to the linked list
def addOneUtil(head):
    # Base case: If the list is empty, return carry as 1
    if head is None:
        return 1
    # Recur for the next node
    carry = addOneUtil(head.next)
    # Add carry to the current node's data
    sum = head.data + carry
    # Update the current node's data
    head.data = sum % 10
    # Return carry for the previous node
    return sum // 10


# Separate name keeps the recursive C++ alternative from replacing addOne.
def addOneRecursive(head):
    # Add one to the list and get the final carry
    carry = addOneUtil(head)
    # If there's a carry remaining, add a new node at the beginning
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
