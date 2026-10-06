class Node:
    # Constructor for creating a new node
    def __init__(self, value):
        self.data = value
        self.next = None


# Function to find the intersection point of two linked lists
def intersectPoint(head1, head2):
    # Initialize pointers for both linked lists
    p = head1
    q = head2
    c1 = 0
    c2 = 0
    # Step 1: Calculate the length of the first linked list (head1)
    while p:
        p = p.next
        # Increment the length of list 1
        c1 += 1
    # Step 2: Calculate the length of the second linked list (head2)
    while q:
        q = q.next
        # Increment the length of list 2
        c2 += 1
    # Variables to store the lengths of both linked lists
    # Step 3: Calculate the difference in lengths of the two lists
    # Absolute difference between the lengths
    diff = abs(c1 - c2)
    # Reset the pointers to the heads of the lists
    p = head1
    q = head2
    # Step 4: Align both lists by moving the pointer of the longer list ahead by the
    # difference in lengths
    if c1 > c2:
        # Move pointer p (head1) forward by the difference in length
        for i in range(diff):
            p = p.next
    elif c2 > c1:
        # Move pointer q (head2) forward by the difference in length
        for i in range(diff):
            q = q.next
    # Step 5: Traverse both lists simultaneously and check for intersection
    while p is not q:
        # Move pointer p to the next node
        p = p.next
        # Move pointer q to the next node
        q = q.next
    if p:
        return p.data
    # No intersection found, return -1
    return -1


'''
Let n and m be the lengths of the acyclic input lists.
Time: O(n + m): count both lengths, advance the longer list by their
difference, then walk together. Each node is visited at most a few times.
Space: O(1) auxiliary: only pointers and length counters are stored.
Intersection means the same node object, not merely equal data.
'''
