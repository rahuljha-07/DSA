import sys


# Function to find the smallest number with the given sum of digits and number of digits
def findSmallest(s, d):
    if d <= 0 or s < 0:
        # Not possible
        return "-1"
    # Case 1: If the sum of digits is 0 and we need only 1 digit, the answer is "0"
    if s == 0:
        return "0" if d == 1 else "-1"
    # Case 2: If the sum of digits exceeds the maximum possible sum for d digits, return -1
    if s > 9 * d:
        return "-1"
    # Array to store digits of the result
    result = [0] * d
    # Subtract 1 from the sum to ensure the most significant digit is not zero
    s -= 1
    # Fill the digits from the least significant position
    for i in range(d - 1, 0, -1):
        if s > 9:
            result[i] = 9
            s -= 9
        else:
            result[i] = s
            s = 0
            break
    # Assign the remaining sum to the most significant digit
    result[0] = s + 1
    # Convert the result to a string
    smallestNumber = ""
    for digit in result:
        smallestNumber += str(digit)
    return smallestNumber


def main():
    tokens = iter(map(int, sys.stdin.read().split()))
    s = next(tokens)
    d = next(tokens)
    smallestNumber = findSmallest(s, d)
    if smallestNumber == "-1":
        print("Not possible")
    else:
        print(smallestNumber)


if __name__ == "__main__":
    main()


'''
Let d be the requested number of digits.
Time: O(d) to allocate and fill the digit array. The retained repeated
string concatenation has a conservative O(d^2) worst-case bound in Python
because each append can copy the accumulated prefix. Implementations that
optimize local += concatenation can make this O(d) in practice.
Impossible inputs rejected before allocation take O(1) time.
Space: O(d) auxiliary/output for result and the final d-character string;
even with prefix copying, only O(d) characters are live at once.
'''
