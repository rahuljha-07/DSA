class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Helper function to perform in-order traversal to count the total number of nodes in the
# BST
def inorderCount(root, count):
    if not root:
        return
    inorderCount(root.left, count)
    # Increment count for each node visited
    count[0] += 1
    inorderCount(root.right, count)


# Helper function to perform in-order traversal and find the median (odd/even count)
def inorderFindMedian(root, iteration, k, v):
    if not root or iteration[0] >= k:
        return
    inorderFindMedian(root.left, iteration, k, v)
    if iteration[0] >= k:
        return
    # Increment iteration count for each node visited
    iteration[0] += 1
    # Collect the nodes we need for the median calculation
    if len(v) < 2:
        # If the list size is less than 2, just add the value
        v.append(root.data)
    else:
        # If size is 2, shift the elements
        # Move the previous value to index 0
        v[0] = v[1]
        # Add the current value to index 1
        v[1] = root.data
    if iteration[0] == k:
        # Stop once we reach the k-th element
        return
    inorderFindMedian(root.right, iteration, k, v)


# Function to find the median of the BST
def findMedian(root):
    # Step 1: Count the total number of nodes in the BST
    count = [0]
    inorderCount(root, count)
    if count[0] == 0:
        raise ValueError("Tree is empty")
    # Step 2: Perform in-order traversal to find the median
    result = []
    # Find the k-th element (middle element or second middle for even case)
    k = count[0] // 2 + 1
    iteration = [0]
    inorderFindMedian(root, iteration, k, result)
    if count[0] % 2 == 1:
        # If the number of nodes is odd, return the last value
        return result[-1]
    else:
        # If the number of nodes is even, return the average of the two middle values
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
