class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


head = None
tail = None


def bToDLL(root):
    global head, tail
    if not root:
        return None
    bToDLL(root.left)
    if not tail:
        head = root
        root.left = None
    else:
        root.left = tail
        tail.right = root
    tail = root
    bToDLL(root.right)
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
