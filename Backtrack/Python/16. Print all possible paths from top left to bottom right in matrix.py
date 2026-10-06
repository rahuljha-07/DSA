# Recursive function to find all paths
def findPaths(matrix, i, j, path, result):
    rows = len(matrix)
    cols = len(matrix[0])
    # Return if the current cell is out of bounds
    if i >= rows or j >= cols:
        return
    # Add the current cell to the path
    path.append(matrix[i][j])
    # If we have reached the bottom-right corner, store the path
    if i == rows - 1 and j == cols - 1:
        result.append(list(path))
    else:
        # Call the function for moving down
        # Call the function for moving right
        findPaths(matrix, i + 1, j, path, result)
        findPaths(matrix, i, j + 1, path, result)
    path.pop()


def allPaths(matrix):
    result = []
    path = []
    if matrix and matrix[0]:
        findPaths(matrix, 0, 0, path, result)
    return result


def main():
    matrix = [[1, 2, 3], [4, 5, 6]]
    paths = allPaths(matrix)
    for path in paths:
        print(path)


if __name__ == "__main__":
    main()


'''
Let R/C be matrix dimensions, L=R+C-1 path length, and
P=binomial(R+C-2, R-1) the number of down/right paths.
Time: O(P*L): copying each completed path costs L; recursive prefixes
and boundary attempts also fit this bound. Every path must be enumerated.
Space: O(L) auxiliary current path/stack plus O(P*L) output copies.
Copying path at the base case prevents later backtracking from clearing results.
'''
