# Function to calculate the product of array elements except itself
def productExceptSelf(nums, n):
    # Create two lists to store the left and right products
    leftProduct = [0] * n
    rightProduct = [0] * n

    # Initialize the first element of the left product list to 1
    leftProduct[0] = 1
    # Initialize the last element of the right product list to 1
    rightProduct[n - 1] = 1

    # Fill the left product list
    for i in range(1, n):
        # Each position leftProduct[i] contains the product of all elements to the left of
        # nums[i]
        leftProduct[i] = leftProduct[i - 1] * nums[i - 1]

    # Fill the right product list
    for i in range(n - 2, -1, -1):
        # Each position rightProduct[i] contains the product of all elements to the right of
        # nums[i]
        rightProduct[i] = rightProduct[i + 1] * nums[i + 1]

    # Calculate the final result by multiplying left and right products
    for i in range(n):
        # Each position nums[i] now contains the product of all elements except nums[i]
        nums[i] = leftProduct[i] * rightProduct[i]

    # Return the modified nums list which contains the result
    return nums


nums = [10, 3, 5, 6, 2]
print(productExceptSelf(nums, len(nums)))


'''
Time Complexity: O(n)

Reason:
One pass builds left products, one pass builds right products, and one pass
combines them. These linear passes add to O(n).

Space Complexity: O(n)

Reason:
The leftProduct and rightProduct lists each store n values.
'''
