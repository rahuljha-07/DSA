class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, root1, root2):
        tree1Nodes = []
        tree2Nodes = []
        self.inorderTraversal(root1, tree1Nodes)
        self.inorderTraversal(root2, tree2Nodes)
        mergedNodes = self.mergeSortedArrays(tree1Nodes, tree2Nodes)
        return self.buildBalancedBST(mergedNodes, 0, len(mergedNodes) - 1)

    def inorderTraversal(self, root, sortedNodes):
        if not root:
            return
        self.inorderTraversal(root.left, sortedNodes)
        sortedNodes.append(root.data)
        self.inorderTraversal(root.right, sortedNodes)

    def mergeSortedArrays(self, arr1, arr2):
        merged = []
        i = 0
        j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        while i < len(arr1):
            merged.append(arr1[i])
            i += 1
        while j < len(arr2):
            merged.append(arr2[j])
            j += 1
        return merged

    def buildBalancedBST(self, sortedNodes, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = Node(sortedNodes[mid])
        root.left = self.buildBalancedBST(sortedNodes, start, mid - 1)
        root.right = self.buildBalancedBST(sortedNodes, mid + 1, end)
        return root


def inorderPrint(root):
    if not root:
        return
    inorderPrint(root.left)
    print(root.data, end=" ")
    inorderPrint(root.right)


def main():
    root1 = Node(3)
    root1.left = Node(1)
    root1.right = Node(5)
    root2 = Node(4)
    root2.left = Node(2)
    root2.right = Node(6)
    solution = Solution()
    mergedRoot = solution.mergeTrees(root1, root2)
    print("Inorder Traversal of Merged Balanced BST: ", end="")
    inorderPrint(mergedRoot)
    print()


if __name__ == "__main__":
    main()


'''
Let n and m be the two node counts.
Time: O(n + m): two inorder traversals, a linear two-pointer merge, and
one new node per merged value. No comparison sort is needed.
Space: O(n + m) auxiliary for the arrays and traversal stacks, plus
O(n + m) output nodes. Balanced construction has O(log(n + m)) stack depth.
'''
