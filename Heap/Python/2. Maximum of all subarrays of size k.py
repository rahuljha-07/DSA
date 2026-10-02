from collections import deque


def maximumOfAllSubarrays(arr, k):
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
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            ans.append(window[0])
            if arr[i] == window[0]:
                window.popleft()
            i += 1
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
