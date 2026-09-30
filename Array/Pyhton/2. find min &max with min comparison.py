def find_min_max(arr):
    n = len(arr)

    if n == 0:
        print("Array is empty")
        return

    if n % 2 == 0:
        if arr[0] > arr[1]:
            maximum = arr[0]
            minimum = arr[1]
        else:
            minimum = arr[0]
            maximum = arr[1]
        i = 2
    else:
        minimum = maximum = arr[0]
        i = 1

    while i < n - 1:
        if arr[i] > arr[i + 1]:
            if arr[i] > maximum:
                maximum = arr[i]
            if arr[i + 1] < minimum:
                minimum = arr[i + 1]
        else:
            if arr[i + 1] > maximum:
                maximum = arr[i + 1]
            if arr[i] < minimum:
                minimum = arr[i]

        i += 2

    print("max:", maximum)
    print("min:", minimum)


arr = [1, 4, 3, 2, 6, 5]
find_min_max(arr)