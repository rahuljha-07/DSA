def longestCommonPrefix(v):
    ans = ""
    v.sort()

    n = len(v)
    first = v[0]
    last = v[n - 1]

    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return ans
        ans += first[i]
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
