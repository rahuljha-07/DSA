def longestCommonPrefix(v):
    # Variable to store the longest common prefix
    ans = ""
    # Sort the list of strings
    v.sort()

    # Get the number of strings in the list
    n = len(v)
    # The first string in the sorted order
    first = v[0]
    # The last string in the sorted order
    last = v[n - 1]

    # Compare characters of the first and last string to find the common prefix
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            # Return the common prefix found so far if characters differ
            return ans
        # Append the matching character to ans
        ans += first[i]
    # Return the longest common prefix
    return ans


v = ["geeksforgeeks", "geeks", "geek", "geezer"]
print(longestCommonPrefix(v))


'''
Time Complexity: O(n log n * m), where n is number of strings and m is average string length.

Reason:
The list of strings is sorted first.
Sorting n strings costs O(n log n) comparisons, and each comparison
can inspect up to m characters.

After sorting, only the first and last strings need to be compared
to find the common prefix, which takes O(m).
Sorting dominates the total complexity.

Space Complexity: O(1), excluding output.

Reason:
The algorithm uses only a few variables and builds the answer string.
The answer string is the required output.
'''
