from bisect import bisect_left, bisect_right

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def replaceWithLeastGreater(arr):
    n = len(arr)
    result = [-1] * n
    # Sorted unique values emulate std::set without an external dependency.
    s = []
    for i in range(n - 1, -1, -1):
        it = bisect_right(s, arr[i])
        if it != len(s):
            result[i] = s[it]
        pos = bisect_left(s, arr[i])
        if pos == len(s) or s[pos] != arr[i]:
            s.insert(pos, arr[i])
    return result


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
Sorted-container time: O(n^2) worst case in Python: binary searches cost
O(log n), but list insertion shifts O(n) items. The C++ balanced std::set
version is O(n log n); ordering/uniqueness and upper-bound logic are retained.
BST time: O(n log n) for balanced insertions, O(n^2) worst case for a skewed
unbalanced BST, because insertion follows a path of up to n nodes.
Space: both use O(n) auxiliary container/tree storage plus O(n) output; the BST
also uses O(h) recursive stack space, bounded by O(n).
'''
