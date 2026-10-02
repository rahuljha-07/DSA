# Function to perform word break and print all possible sentences
def wordBreak(str, ans, mp):

    # If the entire string has been processed
    if len(str) == 0:
        print(ans)
        return

    # Traverse the string to break it into two parts
    for i in range(1, len(str) + 1):

        # Extract left substring
        left = str[:i]

        # Check if left part exists in dictionary
        if left in mp:

            # Recur with remaining right substring
            wordBreak(
                str[i:],
                ans + left + " ",
                mp
            )


# Example dictionary
dictionary = {
    "apple": True,
    "pie": True,
    "pen": True,
    "applepen": True,
    "pine": True,
    "pineapple": True
}

# Input string
input = "pineapplepenapple"

# Function call
wordBreak(input, "", dictionary)


'''
Time Complexity:
O(2^n) approximately in the worst case

Reason:

At each position, we may have multiple valid choices
for where to break the string.

This creates a recursion tree with many possible partitions.

In the worst case, the number of possible segmentations
can grow exponentially.

Also, Python slicing such as:

str[:i]
str[i:]

creates new strings, which adds extra copying cost.

So the practical cost can be higher, but the main
recursive complexity is exponential.


Space Complexity:
O(n)

Reason:

The maximum recursion depth can be O(n).

At each recursive call, we process a smaller suffix.

Ignoring the output strings and temporary slices,
the recursion stack uses O(n) space.

If temporary strings created by slicing are counted,
the actual memory usage can be higher.
'''