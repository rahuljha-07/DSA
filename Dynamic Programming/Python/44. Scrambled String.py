class Solution:
    def __init__(self):
        self.m = {}

    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        # Create a unique key for memoization
        key = s1 + " " + s2
        if key in self.m:
            # Return the stored result if it exists
            return self.m[key]
        # Base Case: If the strings are identical, they are scrambled versions
        if s1 == s2:
            self.m[key] = True
            return True
        # Base Case: If the length of the strings is 1 and they are not equal
        if len(s1) <= 1:
            self.m[key] = False
            return False
        # Length of the strings
        n = len(s1)
        # Initialize result to false
        flag = False
        # Try splitting the string at every possible index
        for i in range(1, n):
            if (self.isScramble(s1[:i], s2[:i])
                    and self.isScramble(s1[i:], s2[i:])):
                # The strings are scrambled versions
                flag = True
                break
            if (self.isScramble(s1[:i], s2[n - i:])
                    and self.isScramble(s1[i:], s2[:n - i])):
                flag = True
                break
        # Store the result in the memoization map
        self.m[key] = flag
        return flag


def main():
    sol = Solution()
    s1 = "great"
    s2 = "rgeat"
    if sol.isScramble(s1, s2):
        print(f"Yes, {s2} is a scrambled version of {s1}")
    else:
        print(f"No, {s2} is not a scrambled version of {s1}")


if __name__ == "__main__":
    main()


'''
Let n be the common string length; strings must not contain the key's
space separator, matching the source's intended word-input domain.
Time: O(n^5) conservative bound including slicing/key hashing: for each
length L there are O((n-L+1)^2) substring pairs, each tries O(L) splits
with O(L) string copying/lookup work. Ignoring copies gives O(n^4).
Space: O(n^4) worst-case cached key characters across O(n^3) pairs,
plus O(n^2) active substring/key storage on an O(n)-deep stack.
The substring-key memo approach is retained, not replaced by index DP.
Unequal lengths are rejected before splitting.
'''
