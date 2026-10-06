# Function to return the integer value of a Roman numeral character
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


# Function to convert a Roman numeral string to its decimal equivalent
def romanToDecimal(str):
    # Initialize sum with the value of the first character
    sum = val(str[0])

    # Iterate through the Roman numeral string starting from the second character
    for i in range(1, len(str)):
        # If the current character's value is less than or equal to the previous character's
        # value
        if val(str[i]) <= val(str[i - 1]):
            # Add the current value to the sum
            sum += val(str[i])
        else:
            # If the current character's value is greater than the previous character's
            # value,
            # it indicates a subtraction scenario (e.g., IV = 4, IX = 9)
            # Adjust the sum for the subtraction
            sum += val(str[i]) - (2 * val(str[i - 1]))

    # Return the final computed decimal value
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
