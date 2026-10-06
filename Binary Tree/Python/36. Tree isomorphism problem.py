class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Recursive function to check if two trees are isomorphic
def isIsomorphic(T1, T2):
    # Base cases
    # Both nodes are None
    if not T1 and not T2:
        return True
    # One node is None, the other is not
    if not T1 or not T2:
        return False
    if T1.data != T2.data:
        return False
    # Check isomorphism without flipping or with flipping children
    withoutFlip = (isIsomorphic(T1.left, T2.left)
                   and isIsomorphic(T1.right, T2.right))
    withFlip = (isIsomorphic(T1.left, T2.right)
                and isIsomorphic(T1.right, T2.left))
    # Return true if either configuration is isomorphic
    return withoutFlip or withFlip


def main():
    T1 = Node(1)
    T1.left = Node(2)
    T1.right = Node(3)
    T1.left.left = Node(4)
    T2 = Node(1)
    T2.left = Node(3)
    T2.right = Node(2)
    T2.right.right = Node(4)
    print("Yes, the trees are isomorphic." if isIsomorphic(T1, T2)
          else "No, the trees are not isomorphic.")


if __name__ == "__main__":
    main()


'''
Let n/m be the two node counts and h1/h2 their heights.
Time: O(n*m) worst-case upper bound: withoutFlip AND withFlip are both
evaluated even if the first succeeds. Equal labels can explore many node
pairings. For equal perfect trees, T(n) = 4*T(n/2) + O(1), giving O(n^2),
not O(n). Unique labels or early mismatches usually prune most calls.
Space: O(min(h1, h2) + 1) auxiliary: branch comparisons run sequentially,
so only one paired recursion path is active; no memo/result tree is stored.
'''
