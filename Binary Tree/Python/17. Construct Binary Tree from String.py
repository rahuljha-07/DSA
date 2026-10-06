class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


start = 0


# Function to construct a binary tree from a string
def constructTree(s):
    global start
    start = 0
    if not s:
        return None
    return stringToTree(s)


# Helper function to recursively build the tree
def stringToTree(s):
    global start
    if start >= len(s):
        return None
    if s[start] == ')':
        start += 1
        return None
    neg = False
    if s[start] == '-':
        neg = True
        start += 1
    num = 0
    while start < len(s) and s[start].isdigit():
        num = num * 10 + (ord(s[start]) - ord('0'))
        # Skip '('
        start += 1
    # If the number is negative
    if neg:
        num = -num
    root = Node(num)
    # If the string has no more characters, return the root end node
    if start >= len(s):
        return root
    # If the next character is '(', it indicates a left child
    # If the next character is ')', it indicates the end of left child
    if start < len(s) and s[start] == '(':
        start += 1
        root.left = stringToTree(s)
    # If the next character is '(', it indicates a right child
    if start < len(s) and s[start] == ')':
        start += 1
        return root
    if start < len(s) and s[start] == '(':
        start += 1
        root.right = stringToTree(s)
    # If the next character is ')', it indicates the end of right child
    if start < len(s) and s[start] == ')':
        start += 1
        return root
    return root


# Function to print the tree (in-order traversal)
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.value, end=" ")
    inorder(root.right)


def main():
    s = "1(2(4)(5))(3(6)(7))"
    root = constructTree(s)
    inorder(root)


if __name__ == "__main__":
    main()


'''
Let L be the string length, n the parsed node count, and h tree height.
Time: O(L) under fixed-size integer arithmetic: the shared start index
moves forward and each digit/parenthesis is read only a constant number
of times. No substrings are copied. Very large numeric tokens additionally
incur Python arbitrary-precision arithmetic costs.
Space: O(h) auxiliary for parser recursion, plus O(n) output nodes.
start resets per parse; empty child brackets produce None.
'''
