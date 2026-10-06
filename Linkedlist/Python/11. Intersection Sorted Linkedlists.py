class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def findIntersection(head1, head2):
    # Initialize two pointers for traversing both lists
    first = head1
    second = head2
    # Initialize the result list
    res = None
    cur = None
    # Traverse both lists until one is exhausted
    while first and second:
        if first.data < second.data:
            first = first.next
        # If second list node's data is smaller, move the second pointer
        elif first.data > second.data:
            second = second.next
        # If both nodes have the same data, add to result list
        else:
            # Create a new node with the common value
            temp = Node(first.data)
            # If result list is empty, initialize it with the new node
            if res is None:
                res = temp
                cur = temp
            # Otherwise, append to the result list
            else:
                cur.next = temp
                cur = cur.next
            # Move both pointers to the next node
            first = first.next
            second = second.next
    # Return the head of the intersection list
    return res


'''
Let n and m be the sorted input lengths and r the number of result nodes.
Time: O(n + m): each iteration advances at least one pointer, and neither
pointer moves backward. Matching values are appended in O(1) using cur.
Space: O(1) auxiliary for pointers; O(r) output space for common-value nodes,
where r <= min(n, m). Neither input list is copied in full.
'''
