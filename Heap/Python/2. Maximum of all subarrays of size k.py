from collections import deque


def maximumOfAllSubarrays(arr, k):
    # To store the results (maximum of each window)
    ans = []
    window = deque()
    i = 0
    j = 0
    size = len(arr)
    if k <= 0:
        raise ValueError("k must be positive")
    while j < size:
        # Include EVERY incoming value, including the one completing a window.
        while window and window[-1] < arr[j]:
            window.pop()
        window.append(arr[j])
        # If the size of the window is less than k
        if j - i + 1 < k:
            # Expand the window by moving 'j' forward
            j += 1
        # When the window size reaches k
        elif j - i + 1 == k:
            # The element at the front of the list is the maximum for this window
            ans.append(window[0])
            # If the element at the front of the list is out of the window, pop it
            if arr[i] == window[0]:
                window.popleft()
            # Slide the window by incrementing 'i' and 'j'
            i += 1
            # This should be outside the `else if` block to ensure it's executed in every
            # loop
            j += 1
    return ans


def main():
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = maximumOfAllSubarrays(arr, k)
    print(f"Maximums of all subarrays of size {k}:", *result)


if __name__ == "__main__":
    main()


'''
Let n be the array length and k > 0 the window size.
Time: O(n): each value is appended once and removed at most once from
the deque, so the nested removal loop is amortized linear.
Space: O(min(n, k)) auxiliary deque, plus O(max(0, n-k+1)) output.
Equal values are retained (strict < removal) because storing values rather
than indices needs duplicate counts when an old maximum leaves the window.
When k > n, no complete window exists and the result is empty.
'''
