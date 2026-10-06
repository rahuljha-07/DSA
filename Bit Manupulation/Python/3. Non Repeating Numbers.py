def findNonRepeatingNumbers(arr):
    xxory = 0
    # Step 1: XOR all numbers in the array
    for val in arr:
        xxory ^= val
    # Step 2: Find the rightmost set bit (RMSB)
    rsbm = xxory & -xxory
    x = 0
    y = 0
    # Step 3: Split numbers into two groups and XOR within each group
    for val in arr:
        if (val & rsbm) == 0:
            # Group 1: Numbers where RMSB is 0
            x ^= val
        else:
            # Group 2: Numbers where RMSB is 1
            y ^= val
    # Step 4: Sort the results to ensure the output is in increasing order
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
