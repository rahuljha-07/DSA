# Function to check if arr2 is a stack permutation of arr1
def isStackPermutation(arr1, arr2):
    # Stack to hold elements temporarily
    s = []
    n = len(arr1)
    # Pointer for output array (arr2)
    j = 0

    # Iterate through each element in arr1
    for i in range(n):
        # Push current element onto the stack
        s.append(arr1[i])

        # While the stack is not empty and the top of the stack matches arr2[j]
        while len(s) != 0 and j < n and s[-1] == arr2[j]:
            # Pop from the stack
            s.pop()
            # Move to the next element in arr2
            j += 1

    # If we've matched all elements in arr2, then it's a valid permutation
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
