# Function to check if it's possible to place cows in the stalls such that the minimum
# distance is at least minDist
def canPlaceCows(stalls, numCows, minDist):
    # Start by placing the first cow
    countCows = 1
    # First stall is already used
    lastPlaced = stalls[0]

    # Iterate through the stalls
    for i in range(1, len(stalls)):
        # Distance from last placed cow
        gap = stalls[i] - lastPlaced

        # Check if the gap is sufficient
        if gap >= minDist:
            # Place cow
            countCows += 1
            # Update position
            lastPlaced = stalls[i]

            # If all cows are placed, return true
            if countCows == numCows:
                return True

    # Not all cows could be placed with the required minimum distance
    return False


# Function to find the largest minimum distance between cows
def largestMinDistance(stalls, numCows):
    # Sort stall positions
    stalls.sort()

    # Minimum possible distance
    low = 1
    # Maximum possible distance
    high = stalls[-1] - stalls[0]
    # To store the largest minimum distance found
    result = 0

    # Perform binary search to find the largest minimum distance
    while low <= high:
        # Calculate the mid distance
        mid = low + (high - low) // 2

        # Check if cows can be placed with at least mid distance apart
        if canPlaceCows(stalls, numCows, mid):
            # Update result with current mid distance
            result = mid
            # Try for a larger distance
            low = mid + 1
        else:
            # Reduce the distance
            high = mid - 1

    # Return the largest minimum distance found
    return result


stalls = [1, 2, 4, 8, 9]
numCows = 3
print(largestMinDistance(stalls, numCows))


'''
Time Complexity: O(n log n + n log R)

Reason:
Stalls are sorted first. Then binary search runs on the distance range R,
and each feasibility check scans all n stalls.

Space Complexity: O(1) auxiliary

Reason:
The placement check uses only counters and positions. Sorting is in place
from the algorithm point of view.
'''
