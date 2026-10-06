# function to reverse an array
def reverse_array(arr):
    n = len(arr)

    # Swap elements from opposite ends
    for i in range(n // 2): # or for i in range(int(n / 2)):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]


arr = [1, 4, 3, 2, 6, 5]
reverse_array(arr)
print(*arr)

'''
Time Complexity: O(n)

Reason:
The loop runs for n // 2 positions and swaps one pair each time.
Each swap is O(1), so the total work grows linearly with n.

Space Complexity: O(1)

Reason:
The array is reversed in place using only index variables and temporary swap storage.
'''
