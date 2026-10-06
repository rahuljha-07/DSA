class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


head = None
tail = None


# Function to convert the binary tree to a doubly linked list
def bToDLL(root):
    global head, tail
    # Base case: if the tree is empty, return None
    if not root:
        return None
    # Recursively convert the left subtree to DLL
    bToDLL(root.left)
    # If the tail is None, it means this is the first node, so set the head to it
    if not tail:
        head = root
        root.left = None
    else:
        # Otherwise, link the current root node to the DLL
        # Set the previous pointer of the current node to the tail
        root.left = tail
        # Set the next pointer of the tail node to the current root
        tail.right = root
    # Move the tail to the current node after processing
    tail = root
    # Recursively convert the right subtree to DLL
    bToDLL(root.right)
    # Return the head of the doubly linked list
    return head


'''
Let n be the node count and h tree height.
Time: O(n): each node is processed once with O(1) work per visit.
Space: O(h) auxiliary for recursion: O(log n) on balanced trees and
O(n) on skewed trees. No new result tree is allocated.
Inorder relinks existing nodes as left=previous/right=next; output
requires no new nodes. Like the source, reset head and tail to None before
converting a separate tree, and do not reuse the mutated tree as a tree.
'''
