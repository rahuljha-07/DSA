# Function to count the number of triplets in the array such that their sum is less than a
# given value x
def countTriplets(arr, n, x):
    # Sort the array to enable the two-pointer technique
    arr.sort()
    # Variable to store the count of valid triplets
    count = 0

    # Iterate through the array with the first element of the triplet
    for i in range(n - 2):
        # Pointer for the second element
        left = i + 1
        # Pointer for the third element
        right = n - 1

        # Use the two-pointer technique to find pairs of elements that sum with arr[i] to
        # less than x
        while left < right:
            # Check if the sum of the triplet is less than x
            if arr[i] + arr[left] + arr[right] < x:
                # If the sum is less than x, all elements between left and right are valid
                # pairs
                # Count all pairs (left,...,right-1 ,right)
                count += right - left
                # Move the left pointer to the right
                left += 1
            else:
                # If the sum is greater than or equal to x, move the right pointer to the
                # left
                right -= 1

    # Return the total count of valid triplets
    return count


arr = [5, 1, 3, 4, 7]
x = 12
print("Count of triplets:", countTriplets(arr, len(arr), x))


'''
Time Complexity: O(n^2)

Reason:
Sorting takes O(n log n). After that, each fixed first element uses a
left/right two-pointer scan over the remaining array, giving O(n^2).

Space Complexity: O(1) auxiliary

Reason:
Only pointers and count variables are used. Python sorting may use internal
temporary memory, but the algorithm does not create another array.
'''
