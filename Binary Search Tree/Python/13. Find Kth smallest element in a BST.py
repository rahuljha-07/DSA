class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


ans = -1


# Helper function for finding the k-th smallest element in BST
def findKthSmallestHelper(root, k, count):
    global ans
    # Base case: if the node is None, return
    if not root:
        return
    # Traverse the left subtree first (in-order traversal)
    findKthSmallestHelper(root.left, k, count)
    # Increment the count as we visit each node
    count[0] += 1
    # If count matches k, store the result in 'ans'
    if count[0] == k:
        ans = root.data
    # Traverse the right subtree (still part of in-order traversal)
    findKthSmallestHelper(root.right, k, count)


# Public function to find the k-th smallest element in the BST
def kthSmallest(root, k):
    global ans
    # Initialize the count to track how many nodes we've processed
    count = [0]
    # Initialize the answer as -1 (indicating not found yet)
    ans = -1
    findKthSmallestHelper(root, k, count)
    # Return the k-th smallest element (or -1 if not found)
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
    kthSmallestResult = kthSmallest(root, k)
    print(f"The {k}-th smallest element is: {kthSmallestResult}")


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n): the left-root-right traversal visits EVERY node even after
finding position k; this implementation does not stop at the answer.
Space: O(h) auxiliary for recursion plus constant-size count/ans storage.
The one-item count list preserves the C++ reference-counter semantics.
'''
