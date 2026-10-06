class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


ancestor = -1


# Helper function to find Kth ancestor
def findKthAncestor(root, node, K):
    global ancestor
    # Base case: If the node is None, return false
    if root is None:
        return False
    if root.data == node:
        return True
    # Check both left and right subtrees
    foundInLeft = findKthAncestor(root.left, node, K)
    foundInRight = findKthAncestor(root.right, node, K)
    # If either left or right subtree contains the node
    if foundInLeft or foundInRight:
        # Decrease K because we are going back up the tree
        K[0] -= 1
        # If K becomes 0, we found the Kth ancestor
        if K[0] == 0:
            ancestor = root.data
            # stop further recursion
            return False
        # Continue looking for the Kth ancestor
        return True
    # Node is not found in either subtree
    return False


# Function to find Kth ancestor of a given node
def kthAncestor(root, node, K):
    global ancestor
    # Reset the global ancestor variable
    ancestor = -1
    findKthAncestor(root, node, [K])
    # Return the ancestor
    return ancestor


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    node = 5
    K = 2
    result = kthAncestor(root, node, K)
    if result == -1:
        print("No such ancestor exists.")
    else:
        print(f"The {K}th ancestor is: {result}")


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n): each node is processed once with O(1) work per visit.
Space: O(h) auxiliary for recursion: O(log n) on balanced trees and
O(n) on skewed trees. No new result tree is allocated.
K is decremented only while returning through ancestors of the target.
The one-item K holder preserves C++ reference semantics; the public
wrapper resets ancestor. Assumes unique keys and K >= 1.
'''
