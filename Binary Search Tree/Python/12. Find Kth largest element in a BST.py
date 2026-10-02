class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


ans = -1


def findKthLargestHelper(root, k, count):
    global ans
    if not root:
        return
    findKthLargestHelper(root.right, k, count)
    count[0] += 1
    if count[0] == k:
        ans = root.data
    findKthLargestHelper(root.left, k, count)


def kthLargest(root, k):
    global ans
    count = [0]
    ans = -1
    findKthLargestHelper(root, k, count)
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
