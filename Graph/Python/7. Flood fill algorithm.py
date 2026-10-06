from collections import deque


def dfs(image, x, y, newColor, originalColor):
    if (x < 0 or x >= len(image) or y < 0 or y >= len(image[0])
            or image[x][y] != originalColor or image[x][y] == newColor):
        return
    # Change the color
    image[x][y] = newColor
    dfs(image, x + 1, y, newColor, originalColor)
    # Perform DFS in all 4 directions
    # Down
    dfs(image, x - 1, y, newColor, originalColor)
    # Right
    # Left
    dfs(image, x, y + 1, newColor, originalColor)
    dfs(image, x, y - 1, newColor, originalColor)


def floodFillDFS(image, sr, sc, color):
    originalColor = image[sr][sc]
    if originalColor != color:
        dfs(image, sr, sc, color, originalColor)
    return image


def floodFillBFS(image, sr, sc, color):
    originalColor = image[sr][sc]
    if originalColor == color:
        return image
    rows = len(image)
    cols = len(image[0])
    # Start BFS from the given pixel
    q = deque([(sr, sc)])
    image[sr][sc] = color
    # Directions for 4-connected neighbors
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        x, y = q.popleft()
        # Process all 4 neighbors
        for dir in directions:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < rows and 0 <= ny < cols and image[nx][ny] == originalColor:
                image[nx][ny] = color
                # Add the neighbor to the queue
                q.append((nx, ny))
    return image


'''
Let R/C be image dimensions and A the filled component size.
Time: O(A), at most O(R*C): each filled cell is processed once and checks
four neighbors. Equal old/new colors return in O(1).
Space: O(A) worst-case auxiliary recursion/queue; image is updated in
place without copying. A nonempty rectangular image and valid seed are required.
'''
