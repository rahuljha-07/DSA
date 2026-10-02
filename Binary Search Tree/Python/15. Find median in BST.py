class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def inorderCount(root, count):
    if not root:
        return
    inorderCount(root.left, count)
    count[0] += 1
    inorderCount(root.right, count)


def inorderFindMedian(root, iteration, k, v):
    if not root or iteration[0] >= k:
        return
    inorderFindMedian(root.left, iteration, k, v)
    if iteration[0] >= k:
        return
    iteration[0] += 1
    if len(v) < 2:
        v.append(root.data)
    else:
        v[0] = v[1]
        v[1] = root.data
    if iteration[0] == k:
        return
    inorderFindMedian(root.right, iteration, k, v)


def findMedian(root):
    count = [0]
    inorderCount(root, count)
    if count[0] == 0:
        raise ValueError("Tree is empty")
    result = []
    k = count[0] // 2 + 1
    iteration = [0]
    inorderFindMedian(root, iteration, k, result)
    if count[0] % 2 == 1:
        return result[-1]
    else:
        return (result[0] + result[1]) / 2.0


def main():
    root = Node(5)
    root.left = Node(3)
    root.right = Node(8)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(9)
    median = findMedian(root)
    print("The median of the BST is:", median)


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n): counting scans all nodes; the second inorder pass reaches
the middle position in at most another O(n) work.
Space: O(h) auxiliary for recursion; result keeps only the last two
visited values, and counters are constant-size reference holders.
Stopping is propagated through all calls so later nodes cannot overwrite
the median; the singleton case uses the only collected value.
'''
