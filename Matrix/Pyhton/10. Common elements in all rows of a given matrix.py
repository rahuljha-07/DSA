# =========================================================
# 1. USING DICTIONARY WITH ROW INDEX COUNT
# =========================================================

def commonElements_count(matrix):
    result = []

    if not matrix:
        return result

    elementCount = {}
    n = len(matrix)

    # Initialize dictionary with elements from first row
    for num in matrix[0]:
        elementCount[num] = 1

    # Iterate through remaining rows
    for i in range(1, n):

        for num in matrix[i]:

            # If this element has appeared in every row before current row
            if elementCount.get(num, 0) == i:
                elementCount[num] += 1

    # Collect elements appearing in all rows
    for key, value in elementCount.items():

        if value == n:
            result.append(key)

    return result


'''
Time Complexity:
O(n * m)

Reason:

We traverse every element of the matrix once.

If there are n rows and m columns:

O(n * m)

Dictionary lookup and update are O(1) on average.


Space Complexity:
O(m)

Reason:

The dictionary stores elements from the first row.

In the worst case, all m elements are unique.

Therefore:
O(m)
'''



# =========================================================
# 2. USING DICTIONARY + SEEN IN CURRENT ROW
# =========================================================

def commonElements_map(matrix):
    result = []

    if not matrix:
        return result

    elementCount = {}
    n = len(matrix)

    # Initialize dictionary using first row
    for num in matrix[0]:
        elementCount[num] = 1

    # Iterate through remaining rows
    for i in range(1, n):

        seenInCurrentRow = {}

        for j in range(len(matrix[i])):

            num = matrix[i][j]

            # Check if element exists in elementCount
            # and has not already been counted in this row
            if num in elementCount and not seenInCurrentRow.get(num, False):

                elementCount[num] += 1
                seenInCurrentRow[num] = True

    # Find elements appearing in every row
    for key, value in elementCount.items():

        if value == n:
            result.append(key)

    return result


'''
Time Complexity:
O(n * m)

Reason:

We traverse every element of the matrix.

Dictionary lookup and insertion are O(1) on average.

Therefore:

O(n * m)


Space Complexity:
O(m)

Reason:

elementCount can store up to m unique elements.

seenInCurrentRow can also store up to m elements.

Therefore:

O(m)
'''



# =========================================================
# 3. USING SET
# =========================================================

def commonElements_set(matrix):
    result = []

    if not matrix:
        return result

    # Store elements of first row in a set
    commonElementsSet = set(matrix[0])

    # Iterate through remaining rows
    for i in range(1, len(matrix)):

        currentRowElements = set(matrix[i])
        intersection = set()

        # Find common elements
        for num in commonElementsSet:

            if num in currentRowElements:
                intersection.add(num)

        # Update common set
        commonElementsSet = intersection

    # Convert set into result list
    for num in commonElementsSet:
        result.append(num)

    return result


'''
Time Complexity:
O(n * m) average

Reason:

For every row, we create a set of its elements.

Creating the set takes O(m).

Then we check the current common elements against that set.

Set lookup is O(1) on average.

Therefore:

O(n * m)


Space Complexity:
O(m)

Reason:

commonElementsSet stores at most m elements.

currentRowElements stores at most m elements.

intersection also stores at most m elements.

Therefore:

O(m)
'''



# =========================================================
# EXAMPLE
# =========================================================

matrix = [
    [1, 2, 3, 4],
    [2, 3, 5, 6],
    [2, 3, 7, 8]
]


print("Using Count Dictionary:")
print(commonElements_count(matrix))

print("Using Dictionary + Seen:")
print(commonElements_map(matrix))

print("Using Set:")
print(commonElements_set(matrix))