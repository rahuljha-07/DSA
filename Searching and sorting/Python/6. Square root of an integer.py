# Function to count the number of perfect squares less than a given number 'n'
def countSquares(n):
    # Initialize count of squares to 0
    count = 0

    # Count perfect squares less than n
    i = 1
    while i * i < n:
        # Increment count for each perfect square found
        count += 1
        i += 1

    # Return the final count of perfect squares
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
