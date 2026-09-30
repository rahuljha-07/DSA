class Solution:
    def swap_if_greater(self, arr1, arr2, index1, index2):
        if arr1[index1] > arr2[index2]:
            arr1[index1], arr2[index2] = arr2[index2], arr1[index1]

    def merge(self, arr1, arr2, n, m):
        length = n + m

        # Round length / 2 upward, e.g. 7 -> 4 and 8 -> 4.
        gap = (length // 2) + (length % 2)

        while gap > 0:
            left = 0
            right = left + gap

            while right < length:
                # Case 1: Both pointers are in arr1.
                if left < n and right < n:
                    if arr1[left] > arr1[right]:
                        arr1[left], arr1[right] = arr1[right], arr1[left]

                # Case 2: left is in arr1 and right is in arr2.
                elif left < n and right >= n:
                    self.swap_if_greater(arr1, arr2, left, right - n)

                # Case 3: Both pointers are in arr2.
                else:
                    if arr2[left - n] > arr2[right - n]:
                        arr2[left - n], arr2[right - n] = (
                            arr2[right - n], arr2[left - n]
                        )

                left += 1
                right += 1

            # Stop AFTER completing the gap=1 pass.
            # Without this, (1 + 1) // 2 stays 1 forever.
            if gap == 1:
                break

            gap = (gap + 1) // 2


if __name__ == "__main__":
    arr1 = [1, 4, 7, 8, 10]
    arr2 = [2, 3, 9]

    obj = Solution()
    obj.merge(arr1, arr2, len(arr1), len(arr2))

    print("arr1:", arr1)  # [1, 2, 3, 4, 7]
    print("arr2:", arr2)  # [8, 9, 10]


# ---------------------------------------------------------------------------
# HOW IT WORKS
# ---------------------------------------------------------------------------
# Treat both arrays as ONE logical array without actually combining them.
#
# arr1: [1, 4, 7, 8, 10]
# arr2: [2, 3, 9]
#
# Logical positions: 0 through 7.
# - Positions 0 through 4 belong to arr1.
# - Positions 5 through 7 belong to arr2.
#
# To access a logical position in arr2, subtract n:
# Logical position 6 -> arr2[6 - 5] -> arr2[1].
#
# Compare elements that are 'gap' positions apart.
# If the left value is larger, swap them.
# Complete the pass, reduce the gap, and repeat.
#
# For total length 8, the gaps are 4, 2, 1.
#
# Initial:
# arr1 = [1, 4, 7, 8, 10], arr2 = [2, 3, 9]
#
# After gap 4:
# arr1 = [1, 2, 3, 8, 10], arr2 = [4, 7, 9]
#
# After gap 2:
# arr1 = [1, 2, 3, 4, 7], arr2 = [8, 10, 9]
#
# After gap 1:
# arr1 = [1, 2, 3, 4, 7], arr2 = [8, 9, 10]
#
# arr1 holds the smallest n elements; arr2 holds the remaining m elements.
# Both arrays retain their original lengths.
#
# This method relies on the inputs already being sorted.
# It is not a general sorting algorithm for arbitrary unsorted arrays.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O((n + m) log(n + m))
# ---------------------------------------------------------------------------
# Let N = n + m, the combined number of elements.
#
# The gap roughly halves each time:
# N/2, N/4, N/8, ..., 1.
# Therefore, there are O(log N) passes.
#
# For each gap, the inner loop performs N - gap comparisons.
# Each comparison and possible swap takes O(1).
#
# Unlike Quickselect, the ARRAY PORTION does not shrink here.
# Only the DISTANCE between pointers shrinks.
# We still scan across nearly all N elements during each pass.
#
# Total work:
# (N - N/2) + (N - N/4) + ... + (N - 1)
# = O(N log N).
#
# Empty or single-element combined input takes O(1) time.


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(1)
# ---------------------------------------------------------------------------
# We use a fixed number of variables and swap elements directly.
# No combined array, additional list, or recursion is used.
#
# Python's tuple-style swap uses only constant temporary storage.
# Therefore, extra space is O(1).