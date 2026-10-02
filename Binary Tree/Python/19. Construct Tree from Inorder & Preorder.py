class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


preorderIndex = 0


def buildTreeFromPreorderInorder(preorder, leftBound, rightBound, inorderMap):
    global preorderIndex
    if leftBound > rightBound:
        return None
    currentNode = Node(preorder[preorderIndex])
    preorderIndex += 1
    if leftBound == rightBound:
        return currentNode
    inorderIndex = inorderMap[currentNode.data]
    currentNode.left = buildTreeFromPreorderInorder(
        preorder, leftBound, inorderIndex - 1, inorderMap)
    currentNode.right = buildTreeFromPreorderInorder(
        preorder, inorderIndex + 1, rightBound, inorderMap)
    return currentNode


def buildTree(inorder, preorder, n):
    global preorderIndex
    preorderIndex = 0
    inorderMap = {}
    for i in range(n):
        inorderMap[inorder[i]] = i
    return buildTreeFromPreorderInorder(preorder, 0, n - 1, inorderMap)


'''
Let n be the node count and h the constructed height.
Time: O(n) expected: build the dictionary once, then consume each preorder
value once; finding its inorder split uses an O(1) average dictionary lookup.
Space: O(n + h) auxiliary for inorderMap and recursion, plus O(n) output
nodes. Index ranges avoid slicing. Traversals must agree and have unique keys.
'''
