def reverse_array(arr):
    n = len(arr)

    # Swap elements from opposite ends
    for i in range(n // 2): # or for i in range(int(n / 2)):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]


arr = [1, 4, 3, 2, 6, 5]
reverse_array(arr)
print(*arr)