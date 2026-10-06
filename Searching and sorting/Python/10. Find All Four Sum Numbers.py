# Function to find all unique quadruplets in the array that sum up to a given target value
def fourSum(arr, targetSum):
    # Sort the input array to facilitate the two-pointer technique
    arr.sort()

    # To store the unique quadruplets
    result = []
    # To avoid duplicates
    uniqueQuadruplets = set()
    # Get the size of the array
    n = len(arr)

    # Iterate through the array to find quadruplets
    # First element
    for i in range(n - 3):
        # Second element
        for j in range(i + 1, n - 2):
            # Left pointer
            left = j + 1
            # Right pointer
            right = n - 1

            # Use two pointers to find the remaining two elements
            while left < right:
                # Calculate current sum
                currentSum = arr[i] + arr[j] + arr[left] + arr[right]

                # Check if the current sum matches the target
                if currentSum == targetSum:
                    # Insert the quadruplet into the set to ensure uniqueness
                    uniqueQuadruplets.add((arr[i], arr[j], arr[left], arr[right]))
                    # Move the left pointer to the right
                    left += 1
                    # Move the right pointer to the left
                    right -= 1
                # If the current sum is less than the target, move the left pointer to the
                # right
                elif currentSum < targetSum:
                    left += 1
                # If the current sum is greater than the target, move the right pointer to
                # the left
                else:
                    right -= 1

    # Convert the set of unique quadruplets to a list
    for quad in sorted(uniqueQuadruplets):
        # Add each quadruplet to the result list
        result.append(list(quad))

    # Return the result containing all unique quadruplets
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
