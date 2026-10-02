def val(str):
    if str == 'I':
        return 1
    if str == 'V':
        return 5
    if str == 'X':
        return 10
    if str == 'L':
        return 50
    if str == 'C':
        return 100
    if str == 'D':
        return 500
    if str == 'M':
        return 1000
    return 0


def romanToDecimal(str):
    sum = val(str[0])

    for i in range(1, len(str)):
        if val(str[i]) <= val(str[i - 1]):
            sum += val(str[i])
        else:
            sum += val(str[i]) - (2 * val(str[i - 1]))

    return sum


romanNumeral = "MCMXCIV"
print("The decimal value of", romanNumeral, "is", romanToDecimal(romanNumeral))


'''
Time Complexity: O(n), where n is the Roman numeral length.

Reason:
The loop checks each Roman numeral character once.
For every character, val() returns a value using fixed comparisons,
which is constant time.

Space Complexity: O(1)

Reason:
Only a few variables such as sum and loop index are used.
No extra data structure grows with input size.
'''
