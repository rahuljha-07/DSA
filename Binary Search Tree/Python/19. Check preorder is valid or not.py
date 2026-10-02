class Solution:
    def __init__(self):
        self.index = 0

    def solve(self, arr, N, minVal, maxVal):
        if self.index >= N:
            return
        if arr[self.index] < minVal or arr[self.index] > maxVal:
            return
        curr = arr[self.index]
        self.index += 1
        self.solve(arr, N, minVal, curr)
        self.solve(arr, N, curr, maxVal)

    def canRepresentBST(self, arr, N):
        self.index = 0
        minVal = float("-inf")
        maxVal = float("inf")
        self.solve(arr, N, minVal, maxVal)
        return int(self.index == N)


def canRepresentBSTUsingBranches(arr, n):
    s = []
    parent = float("-inf")
    for i in range(n):
        if not s or arr[i] < s[-1]:
            if parent > arr[i]:
                return 0
            s.append(arr[i])
        else:
            while s and s[-1] < arr[i]:
                parent = s.pop()
            s.append(arr[i])
    return 1


def canRepresentBST(arr, n):
    s = []
    parent = float("-inf")
    for i in range(n):
        if arr[i] < parent:
            return 0
        while s and arr[i] > s[-1]:
            parent = s.pop()
        s.append(arr[i])
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
