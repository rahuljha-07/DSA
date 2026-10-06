from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Function to check if all levels of two trees are anagrams
def areAnagrams(root1, root2):
    # Both trees are empty
    if not root1 and not root2:
        return True
    # Only one of the trees is empty
    if not root1 or not root2:
        return False

    q1 = deque()
    q2 = deque()
    q1.append(root1)
    q2.append(root2)

    # Perform level-order traversal for both trees simultaneously
    while len(q1) != 0 and len(q2) != 0:
        size1 = len(q1)
        size2 = len(q2)

        # If the number of nodes at current level are different
        if size1 != size2:
            return False

        level1 = []
        level2 = []

        # Process all nodes at the current level for tree 1
        for i in range(size1):
            node1 = q1[0]
            q1.popleft()
            level1.append(node1.val)

            if node1.left:
                q1.append(node1.left)
            if node1.right:
                q1.append(node1.right)

        # Process all nodes at the current level for tree 2
        for i in range(size2):
            node2 = q2[0]
            q2.popleft()
            level2.append(node2.val)

            if node2.left:
                q2.append(node2.left)
            if node2.right:
                q2.append(node2.right)

        # Sort and compare both levels
        level1.sort()
        level2.sort()

        if level1 != level2:
            return False

    # Check if both queues are empty (same structure)
    return len(q1) == 0 and len(q2) == 0


# Helper function to create a new tree node
def newNode(data):
    return TreeNode(data)


root1 = newNode(1)
root1.left = newNode(2)
root1.right = newNode(3)
root1.left.left = newNode(4)

root2 = newNode(1)
root2.left = newNode(3)
root2.right = newNode(2)
root2.left.right = newNode(4)

if areAnagrams(root1, root2):
    print("All levels of both trees are anagrams.")
else:
    print("All levels of both trees are not anagrams.")


'''
Time Complexity: O(n log n) worst case

Reason:
Every node is visited once level by level. At each level, values are sorted;
in the worst case, a level can contain O(n) nodes, causing O(n log n) sorting work.

Space Complexity: O(n)

Reason:
The queues and level lists can store up to the maximum width of the trees,
which is O(n) in the worst case.
'''
