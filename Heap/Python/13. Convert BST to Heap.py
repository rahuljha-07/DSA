from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def inorderTraversal(root, elements):
    if root is None:
        return
    inorderTraversal(root.left, elements)
    elements.append(root.data)
    inorderTraversal(root.right, elements)


def convertBSTToMinHeap(root, elements):
    if not root:
        return
    q = deque([root])
    idx = 0
    while q:
        current = q.popleft()
        current.data = elements[idx]
        idx += 1
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)


def convertToMinHeap(root):
    elements = []
    inorderTraversal(root, elements)
    convertBSTToMinHeap(root, elements)
    return root


def levelOrderTraversal(root):
    if not root:
        return
    q = deque([root])
    while q:
        current = q.popleft()
        print(current.data, end=" ")
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)
    print()


def main():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(15)
    root.right.right = Node(25)
    print("Original BST (level order): ", end="")
    levelOrderTraversal(root)
    root = convertToMinHeap(root)
    print("Converted Min Heap (level order): ", end="")
    levelOrderTraversal(root)


if __name__ == "__main__":
    main()


'''
Let n be the node count, h tree height, and w maximum level width.
Time: O(n): inorder gathers sorted BST values, then BFS assigns one per
node. No sort is needed because the input is a BST.
Space: O(n + h + w), hence O(n), auxiliary for elements, recursion, and
queue. Nodes/shape are reused. This establishes min-heap VALUE order;
the original shape must be complete to be a conventional binary heap.
The wrapper's extra C++ idx argument is removed to match the helper.
'''
