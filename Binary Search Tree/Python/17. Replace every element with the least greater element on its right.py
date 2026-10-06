class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class _SetNode(Node):
    def __init__(self, val):
        super().__init__(val)
        self.height = 1


class _OrderedSet:
    # AVL balancing keeps insert and upper_bound logarithmic, like std::set.
    def __init__(self):
        self.root = None

    @staticmethod
    def _height(root):
        return root.height if root else 0

    def _update(self, root):
        root.height = 1 + max(self._height(root.left), self._height(root.right))

    def _rotate_left(self, root):
        right = root.right
        root.right = right.left
        right.left = root
        self._update(root)
        self._update(right)
        return right

    def _rotate_right(self, root):
        left = root.left
        root.left = left.right
        left.right = root
        self._update(root)
        self._update(left)
        return left

    def _insert(self, root, key):
        if root is None:
            return _SetNode(key)
        if key < root.data:
            root.left = self._insert(root.left, key)
        elif key > root.data:
            root.right = self._insert(root.right, key)
        else:
            return root
        self._update(root)
        balance = self._height(root.left) - self._height(root.right)
        if balance > 1:
            if key > root.left.data:
                root.left = self._rotate_left(root.left)
            return self._rotate_right(root)
        if balance < -1:
            if key < root.right.data:
                root.right = self._rotate_right(root.right)
            return self._rotate_left(root)
        return root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def upper_bound(self, key):
        root = self.root
        it = None
        while root:
            if root.data > key:
                it = root.data
                root = root.left
            else:
                root = root.right
        return it


def replaceWithLeastGreater(arr):
    n = len(arr)
    # Initialize the result with -1
    result = [-1] * n
    s = _OrderedSet()
    # Traverse the array from right to left
    for i in range(n - 1, -1, -1):
        # Find the first element greater than arr[i]
        it = s.upper_bound(arr[i])
        if it is not None:
            # Assign the least greater element
            result[i] = it
        # Insert the current element into the set
        s.insert(arr[i])
    return result


# Function to insert a node in BST and find the least greater element
def insert(root, key, successor):
    if root is None:
        return Node(key)
    if key < root.data:
        successor[0] = root.data
        root.left = insert(root.left, key, successor)
    else:
        root.right = insert(root.right, key, successor)
    return root


def replaceWithLeastGreaterUsingBST(arr):
    n = len(arr)
    result = [-1] * n
    root = None
    for i in range(n - 1, -1, -1):
        successor = [-1]
        root = insert(root, arr[i], successor)
        result[i] = successor[0]
    return result


def main():
    arr = [8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]
    result = replaceWithLeastGreater(arr)
    print(*result)


if __name__ == "__main__":
    main()


'''
Let n be the array length.
Ordered-set time: O(n log n) worst case. Each of n elements performs an
upper-bound lookup and an insertion in an AVL tree of height O(log n).
Rotations keep the tree balanced, so sorted inputs cannot create long chains.
BST time: O(n log n) for balanced insertions, O(n^2) worst case for a skewed
unbalanced BST, because insertion follows a path of up to n nodes.
Space: both use O(n) auxiliary tree storage plus O(n) output. AVL insertion
uses O(log n) recursive stack space. The alternate unbalanced BST uses O(h)
recursive stack space, bounded by O(n).
'''
