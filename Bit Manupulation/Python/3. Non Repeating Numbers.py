def findNonRepeatingNumbers(arr):
    xxory = 0
    for val in arr:
        xxory ^= val
    rsbm = xxory & -xxory
    x = 0
    y = 0
    for val in arr:
        if (val & rsbm) == 0:
            x ^= val
        else:
            y ^= val
    result = [x, y]
    result.sort()
    return result


def main():
    arr = [36, 50, 24, 56, 36, 24, 42, 50]
    result = findNonRepeatingNumbers(arr)
    print(f"The two non-repeating numbers are: {result[0]} and {result[1]}")


if __name__ == "__main__":
    main()


'''
Let n be the array length, using fixed-width-sized integers.
Time: O(n): two full XOR scans; sorting just two results takes O(1).
Space: O(1): a few XOR accumulators and a two-element output list.
Assumes exactly two values occur once and every other value occurs twice.
'''
