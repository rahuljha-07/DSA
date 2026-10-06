class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


preorderIndex = 0


# Function to build the binary tree from preorder and inorder traversals
def buildTreeFromPreorderInorder(preorder, leftBound, rightBound, inorderMap):
    global preorderIndex
    # Base case: if the current range is invalid (left > right), return None
    if leftBound > rightBound:
        return None
    # Create a new node with the current value from preorder and increment preorder index
    currentNode = Node(preorder[preorderIndex])
    preorderIndex += 1
    # If there's only one element in the range, it must be a leaf node
    if leftBound == rightBound:
        return currentNode
    # Find the index of the current node in inorder traversal
    inorderIndex = inorderMap[currentNode.data]
    currentNode.left = buildTreeFromPreorderInorder(
        preorder, leftBound, inorderIndex - 1, inorderMap)
    currentNode.right = buildTreeFromPreorderInorder(
        preorder, inorderIndex + 1, rightBound, inorderMap)
    return currentNode


def buildTree(inorder, preorder, n):
    global preorderIndex
    # Reset the preorder index
    preorderIndex = 0
    inorderMap = {}
    # Create a map of inorder values to their indices for quick lookup
    for i in range(n):
        inorderMap[inorder[i]] = i
    # Start building the tree
    return buildTreeFromPreorderInorder(preorder, 0, n - 1, inorderMap)


'''
Let n be the node count and h the constructed height.
Time: O(n) expected: build the dictionary once, then consume each preorder
value once; finding its inorder split uses an O(1) average dictionary lookup.
Space: O(n + h) auxiliary for inorderMap and recursion, plus O(n) output
nodes. Index ranges avoid slicing. Traversals must agree and have unique keys.
'''
