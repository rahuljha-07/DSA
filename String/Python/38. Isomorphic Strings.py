def areIsomorphic(str1, str2):
    if len(str1) != len(str2):
        return False

    mapping1 = {}
    mapping2 = {}

    for i in range(len(str1)):
        if str1[i] in mapping1 and mapping1[str1[i]] != str2[i]:
            return False
        mapping1[str1[i]] = str2[i]

        if str2[i] in mapping2 and mapping2[str2[i]] != str1[i]:
            return False
        mapping2[str2[i]] = str1[i]

    return True


print("Are 'paper' and 'title' isomorphic?", "Yes" if areIsomorphic("paper", "title") else "No")
print("Are 'foo' and 'bar' isomorphic?", "Yes" if areIsomorphic("foo", "bar") else "No")


'''
Time Complexity: O(n), where n is string length.

Reason:
Both strings are scanned together once.
For every position, dictionary lookups and assignments are constant time.

Space Complexity: O(k)

Reason:
The two maps store character mappings.
If k distinct characters appear, the maps store O(k) entries.
'''
