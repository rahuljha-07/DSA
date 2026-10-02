def countSquares(n):
    count = 0

    # Count perfect squares less than n
    i = 1
    while i * i < n:
        count += 1
        i += 1

    return count


n = 10
print("Number of perfect squares less than", n, "is:", countSquares(n))


'''
Time Complexity: O(sqrt(n))

Reason:
The loop checks i * i for values of i starting at 1 until i * i reaches n.
The largest checked i is about sqrt(n).

Space Complexity: O(1)

Reason:
Only count and i variables are used.
'''
