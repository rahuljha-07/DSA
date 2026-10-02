def minimumSum(arr):
    arr.sort()
    num1 = ""
    num2 = ""
    for i in range(len(arr)):
        if i % 2 == 0:
            num1 += str(arr[i])
        else:
            num2 += str(arr[i])
    sum = int(num1 or "0") + int(num2 or "0")
    return str(sum)


def main():
    arr = [6, 8, 4, 5, 2, 3]
    print("Minimum sum:", minimumSum(arr))


if __name__ == "__main__":
    main()


'''
Let n be the number of single decimal digits.
Time: sorting is O(n log n), followed by n alternating appends.
Under fixed-size numeric arithmetic and amortized string appends this is
O(n log n). Conservatively, repeated immutable-string concatenation can
cost O(n^2) if appends copy growing prefixes. Large Python integer parsing,
addition, and formatting also add digit-length-dependent work.
Space: O(n) auxiliary for strings, sorting workspace, and integer digits,
plus O(n) output characters. Sorting changes arr in place.
Empty/singleton inputs treat a missing number as zero. Very long strings
remain subject to Python's configured integer-string conversion limit.
'''
