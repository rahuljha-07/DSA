class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


ans = -1


def findKthSmallestHelper(root, k, count):
    global ans
    if not root:
        return
    findKthSmallestHelper(root.left, k, count)
    count[0] += 1
    if count[0] == k:
        ans = root.data
    findKthSmallestHelper(root.right, k, count)


def kthSmallest(root, k):
    global ans
    count = [0]
    ans = -1
    findKthSmallestHelper(root, k, count)
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
