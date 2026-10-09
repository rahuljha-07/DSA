class Solution:
    def __init__(self):
        self.index = 0

    # Recursive helper function to verify BST preorder condition
    def solve(self, arr, N, minVal, maxVal):
        # If all elements are processed, return
        if self.index >= N:
            return
        # Check if the current element falls within the allowed range
        if arr[self.index] < minVal or arr[self.index] > maxVal:
            return
        # Set current element as root for this subtree
        curr = arr[self.index]
        # Move to the next element
        self.index += 1
        # Recursively check left subtree with updated max bound
        self.solve(arr, N, minVal, curr)
        # Recursively check right subtree with updated min bound
        self.solve(arr, N, curr, maxVal)

    def canRepresentBST(self, arr, N):
        self.index = 0
        minVal = float("-inf")
        maxVal = float("inf")
        # Begin recursive validation of BST conditions
        self.solve(arr, N, minVal, maxVal)
        # Check if all elements in the array were processed correctly
        return int(self.index == N)


# kashish mahendatta video
def canRepresentBST(arr, n):
    # Stack to track nodes while constructing BST
    s = []
    # Keeps track of the last removed node (lower bound for the right subtree)
    parent = float("-inf")
    # Iterate through the given preorder array
    for i in range(n):
        if arr[i] < parent:
            # Invalid BST Preorder
            return 0
        # If current element is greater than stack top, we are in the right subtree
        while s and arr[i] > s[-1]:
            # Update parent (last popped element)
            # Remove elements that are smaller than the current element
            parent = s.pop()
        # Push the element into the stack (part of left subtree)
        # Push the current element as a new node
        s.append(arr[i])
    # If all elements are processed without issue, it's a valid BST preorder
    return 1


def main():
    arr1 = [40, 30, 35, 80, 100]
    n1 = len(arr1)
    arr2 = [40, 30, 35, 20, 80]
    n2 = len(arr2)
    print("Test 1 (Valid BST):", "YES" if canRepresentBST(arr1, n1) else "NO")
    print("Test 2 (Invalid BST):", "YES" if canRepresentBST(arr2, n2) else "NO")


if __name__ == "__main__":
    main()


'''
Let n be the preorder length.
Time: O(n) for all three methods. Recursive bounds consume each value
once. Stack methods push each value once and pop it at most once, so
nested while loops are amortized linear rather than O(n^2).
Space: O(n) auxiliary worst case for recursion/explicit stacks.
The recursive variant resets index for reuse. Negative values are valid;
the branch variant's initial lower bound is corrected from 0 to -infinity.
Inclusive bounds/comparisons retain the source's acceptance of duplicates.
'''
