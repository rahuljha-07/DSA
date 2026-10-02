def fourSum(arr, targetSum):
    arr.sort()

    result = []
    uniqueQuadruplets = set()
    n = len(arr)

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left = j + 1
            right = n - 1

            while left < right:
                currentSum = arr[i] + arr[j] + arr[left] + arr[right]

                if currentSum == targetSum:
                    uniqueQuadruplets.add((arr[i], arr[j], arr[left], arr[right]))
                    left += 1
                    right -= 1
                elif currentSum < targetSum:
                    left += 1
                else:
                    right -= 1

    for quad in sorted(uniqueQuadruplets):
        result.append(list(quad))

    return result


arr = [1, 0, -1, 0, -2, 2]
target = 0

quadruplets = fourSum(arr, target)

for quad in quadruplets:
    print("{", end=" ")
    for num in quad:
        print(num, end=" ")
    print("}", end=" ")
print()


'''
Time Complexity: O(n^3)

Reason:
There are two nested loops for the first two elements. For each pair,
the remaining two elements are found using a two-pointer scan, which is O(n).
Sorting costs O(n log n), but O(n^3) dominates.

Space Complexity: O(q)

Reason:
The set stores q unique quadruplets. Apart from output storage, only a
few pointer variables are used.
'''
