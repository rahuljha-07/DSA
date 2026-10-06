class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


ans = -1


# Helper function for finding the k-th largest element in BST
def findKthLargestHelper(root, k, count):
    global ans
    # Base case: if the node is None, return
    if not root:
        return
    # Traverse the right subtree first (reverse in-order traversal)
    findKthLargestHelper(root.right, k, count)
    # Increment the count as we visit each node
    count[0] += 1
    # If count matches k, store the result in 'ans'
    if count[0] == k:
        ans = root.data
    # Traverse the left subtree (still part of reverse in-order traversal)
    findKthLargestHelper(root.left, k, count)


# Public function to find the k-th largest element in the BST
def kthLargest(root, k):
    global ans
    # Initialize the count to track how many nodes we've processed
    count = [0]
    # Initialize the answer as -1 (indicating not found yet)
    ans = -1
    findKthLargestHelper(root, k, count)
    # Return the k-th largest element (or -1 if not found)
    return ans


def main():
    root = Node(5)
    root.left = Node(3)
    root.right = Node(8)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(9)
    k = 3
    kthLargestResult = kthLargest(root, k)
    print(f"The {k}-th largest element is: {kthLargestResult}")


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n): the right-root-left traversal visits EVERY node even after
finding position k; this implementation does not stop at the answer.
Space: O(h) auxiliary for recursion plus constant-size count/ans storage.
The one-item count list preserves the C++ reference-counter semantics.
'''
