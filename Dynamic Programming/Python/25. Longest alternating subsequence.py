# another O(n)
def AlternatingMaxLength(a):
    n = len(a)
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Length of increasing subsequence
    inc = 1
    # Length of decreasing subsequence
    dec = 1
    for i in range(1, n):
        if a[i] > a[i - 1]:
            # Current element is greater, so extend the decreasing sequence
            inc = dec + 1
        elif a[i] < a[i - 1]:
            # Current element is smaller, so extend the increasing sequence
            dec = inc + 1
    # The result is the maximum length of either an increasing or decreasing sequence
    return max(inc, dec)


def main():
    a = [1, 5, 4, 9, 2]
    print("Length of Longest Alternating Subsequence:", AlternatingMaxLength(a))


if __name__ == "__main__":
    main()


'''
Let n be array length.
Time: O(n): scan each adjacent pair once, updating the best increasing
and decreasing ending lengths. Equal neighbors require no update.
Space: O(1) auxiliary: only inc, dec, and indices are maintained.
The added empty-array base case returns 0 instead of the source's 1.
'''
