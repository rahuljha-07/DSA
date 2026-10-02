def countTriplets(arr, n, x):
    arr.sort()
    count = 0

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            if arr[i] + arr[left] + arr[right] < x:
                count += right - left
                left += 1
            else:
                right -= 1

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
