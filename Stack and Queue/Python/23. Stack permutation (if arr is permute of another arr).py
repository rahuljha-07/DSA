def isStackPermutation(arr1, arr2):
    s = []
    n = len(arr1)
    j = 0

    for i in range(n):
        s.append(arr1[i])

        while len(s) != 0 and j < n and s[-1] == arr2[j]:
            s.pop()
            j += 1

    return j == n


arr1 = [1, 2, 3]
arr2 = [2, 1, 3]
print("YES" if isStackPermutation(arr1, arr2) else "Not Possible")

arr1 = [1, 2, 3]
arr2 = [3, 1, 2]
print("YES" if isStackPermutation(arr1, arr2) else "Not Possible")


'''
Time Complexity: O(n)

Reason:
Each element is pushed once and popped at most once while matching the target
permutation.

Space Complexity: O(n)

Reason:
The temporary stack can store up to n elements.
'''
