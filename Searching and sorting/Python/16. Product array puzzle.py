def productExceptSelf(nums, n):
    leftProduct = [0] * n
    rightProduct = [0] * n

    leftProduct[0] = 1
    rightProduct[n - 1] = 1

    for i in range(1, n):
        leftProduct[i] = leftProduct[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        rightProduct[i] = rightProduct[i + 1] * nums[i + 1]

    for i in range(n):
        nums[i] = leftProduct[i] * rightProduct[i]

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
