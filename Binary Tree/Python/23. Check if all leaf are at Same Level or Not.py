class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


ans = 1


# Helper function to check if all leaves are at the same level
def checkLeavesAtSameLevel(root, currentHeight, leafLevel):
    global ans
    # If the current node is None, return
    # If the answer is already false, no need to proceed further
    if not root or ans == 0:
        return
    # First recursively check the left and right subtrees
    checkLeavesAtSameLevel(root.left, currentHeight + 1, leafLevel)
    checkLeavesAtSameLevel(root.right, currentHeight + 1, leafLevel)
    if not root.left and not root.right:
        # If it's the first leaf found, record its level
        if leafLevel[0] == -1:
            leafLevel[0] = currentHeight
        # If it's not the first leaf, compare level with the first leaf's level
        elif leafLevel[0] != currentHeight:
            # Set answer to false if leaf levels don't match
            ans = 0


def check(root):
    global ans
    # Initialize answer flag to true
    ans = 1
    # Leaf level initially not set
    leafLevel = [-1]
    # Start from height 0
    checkLeavesAtSameLevel(root, 0, leafLevel)
    # Return the final result
    return bool(ans)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print("Are all leaves at the same level?", "Yes" if check(root) else "No")


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n): each node is processed once with O(1) work per visit.
Space: O(h) auxiliary for recursion: O(log n) on balanced trees and
O(n) on skewed trees. No new result tree is allocated.
The first leaf sets a single shared leafLevel; later leaves compare
against it in O(1). A mismatch may stop traversal before all nodes are read.
'''
