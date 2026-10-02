class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


isBalancedFlag = 1


def height(root):
    global isBalancedFlag
    if not root:
        return 0
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    if abs(leftHeight - rightHeight) > 1:
        isBalancedFlag = 0
        return 0
    return max(leftHeight, rightHeight) + 1


def isBalanced(root):
    global isBalancedFlag
    isBalancedFlag = 1
    height(root)
    return bool(isBalancedFlag)


def printBalanceStatus(root):
    print("The tree is balanced." if isBalanced(root)
          else "The tree is not balanced.")


def main():
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.right.right = Node(6)
    printBalanceStatus(root1)
    root2 = Node(1)
    root2.left = Node(2)
    root2.left.left = Node(3)
    root2.left.left.left = Node(4)
    printBalanceStatus(root2)


if __name__ == "__main__":
    main()


'''
Let n be the node count and h tree height.
Time: O(n): each node is processed once with O(1) work per visit.
Space: O(h) auxiliary for recursion: O(log n) on balanced trees and
O(n) on skewed trees. No new result tree is allocated.
Height and balance are checked together in postorder, so height is not
recomputed for every subtree. The flag is reset for each public call.
'''
