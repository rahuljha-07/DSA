# Function to initialize the mapping of each character to its corresponding numeric keypad
# sequence
def initializeKeypadMapping():
    keypad = {}
    keypad['A'] = "2"; keypad['B'] = "22"; keypad['C'] = "222"
    keypad['D'] = "3"; keypad['E'] = "33"; keypad['F'] = "333"
    keypad['G'] = "4"; keypad['H'] = "44"; keypad['I'] = "444"
    keypad['J'] = "5"; keypad['K'] = "55"; keypad['L'] = "555"
    keypad['M'] = "6"; keypad['N'] = "66"; keypad['O'] = "666"
    keypad['P'] = "7"; keypad['Q'] = "77"; keypad['R'] = "777"; keypad['S'] = "7777"
    keypad['T'] = "8"; keypad['U'] = "88"; keypad['V'] = "888"
    keypad['W'] = "9"; keypad['X'] = "99"; keypad['Y'] = "999"; keypad['Z'] = "9999"
    # Space maps to 0
    keypad[' '] = "0"
    return keypad


# Function to convert a sentence to its equivalent mobile numeric keypad sequence
def convertToKeypadSequence(sentence):
    keypad = initializeKeypadMapping()
    result = ""

    # Traverse each character in the sentence
    for c in sentence:
        # Convert character to uppercase if it's lowercase
        upperChar = c.upper()
        # Append the keypad sequence corresponding to the character
        result += keypad.get(upperChar, "")

    return result


input = "HELLO WORLD"
print("Input:", input)
print("Output:", convertToKeypadSequence(input))

input = "GEEKSFORGEEKS"
print("\nInput:", input)
print("Output:", convertToKeypadSequence(input))


'''
Time Complexity: O(n), where n is sentence length.

Reason:
Each character of the sentence is visited once.
For every character, dictionary lookup and appending its keypad code
are constant-time operations.

Space Complexity: O(1), excluding output.

Reason:
The keypad dictionary always has a fixed number of entries
for alphabets and space, so it does not grow with input size.
The result string is the required output.
'''
