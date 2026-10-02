def inOrderTraversal(tree, inOrder, index):
    if index >= len(tree):
        return
    inOrderTraversal(tree, inOrder, 2 * index + 1)
    inOrder.append(tree[index])
    inOrderTraversal(tree, inOrder, 2 * index + 2)


def minSwaps(nums):
    N = len(nums)
    v = [(nums[i], i) for i in range(N)]
    v.sort()
    c = 0
    i = 0
    while i < N:
        if v[i][1] == i:
            i += 1
        else:
            c += 1
            # Save the destination: the first assignment changes v[i].
            index = v[i][1]
            v[i], v[index] = v[index], v[i]
    return c


def minSwapsToConvertToBST(tree):
    inOrder = []
    inOrderTraversal(tree, inOrder, 0)
    return minSwaps(inOrder)


def main():
    tree = [5, 3, 8, 2, 4, 6, 9]
    print("Minimum swaps required to convert binary tree to BST:",
          minSwapsToConvertToBST(tree))


if __name__ == "__main__":
    main()


'''
Let n be the array-represented complete tree's node count.
Time: O(n log n): inorder collection is O(n), sorting value/index pairs
is O(n log n), and cycle-fixing takes at most O(n) swaps.
Space: O(n) auxiliary for inorder values, pairs, and sorting workspace;
array-index traversal adds O(log n) recursion depth.
As in the source, minimum-swap correctness assumes distinct values.
With duplicates, fixing the chosen value/index order may overcount swaps.
'''
