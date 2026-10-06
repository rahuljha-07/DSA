# Function to determine if it's possible to make 'par' parathas within 'timeLimit'
def canMakeParathas(cookingTimes, par, timeLimit):
    # Count of total parathas made
    totalParathas = 0

    # Loop through each cook's speed
    for i in range(len(cookingTimes)):
        # Time taken by the current cook to make the first paratha
        time = cookingTimes[i]
        # Multiplier for subsequent parathas
        multiplier = 2

        # While the time required is within the time limit
        while time <= timeLimit:
            # Increment the count of parathas made
            totalParathas += 1
            # Calculate the time for the next paratha
            time += cookingTimes[i] * multiplier
            # Increase the multiplier for the next paratha
            multiplier += 1

        # If the total number of parathas made meets or exceeds the required amount
        if totalParathas >= par:
            # Return success
            return 1

    # Return failure
    return 0


# Function to find the minimum time required to make 'par' parathas using binary search
def findMinimumTime(cookingTimes, par):
    # Lower bound for binary search
    lowerBound = 0
    # Upper bound for binary search (large enough to cover max time)
    upperBound = int(1e8)
    # Variable to store the final answer
    ans = 0

    # Perform binary search to find the minimum time required to make 'par' parathas
    while lowerBound <= upperBound:
        # Calculate the mid point
        mid = (lowerBound + upperBound) // 2

        # Check if it's possible to make 'par' parathas in 'mid' time
        if canMakeParathas(cookingTimes, par, mid):
            # Update the answer to the current mid time
            ans = mid
            # Try for a smaller time
            upperBound = mid - 1
        else:
            # Increase time limit to try again
            lowerBound = mid + 1

    # Return the minimum time required
    return ans


cookingTimes = [1, 2, 3, 4]
par = 10
print(findMinimumTime(cookingTimes, par))


'''
Time Complexity: O(c * p * log T) worst case

Reason:
Binary search runs over the time range T. For each candidate time, every
cook may simulate making parathas until the needed count is reached; in the
worst case this is bounded by p parathas per cook.

Space Complexity: O(1)

Reason:
Only counters and binary-search variables are used.
'''
