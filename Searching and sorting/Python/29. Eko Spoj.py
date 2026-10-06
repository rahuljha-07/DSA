# Function to check if it's possible to cut wood to achieve at least 'm' amount of wood
def canAchieveWoodAmount(lengths, requiredAmount, cutHeight):
    # Initialize the total wood collected
    totalWood = 0

    # Loop through each tree length in the array
    for length in lengths:
        # If the tree is taller than the cut height, we can collect some wood
        if length > cutHeight:
            # Add the collected wood
            totalWood += length - cutHeight

    # Check if the total collected wood is at least the required amount
    return totalWood >= requiredAmount


# Function to find the maximum height at which to cut wood to achieve the required amount
def findMaxCutHeight(lengths, requiredAmount):
    # Minimum possible cut height
    low = 0
    high = max(lengths)
    # Variable to store the optimal cut height
    optimalHeight = -1

    # Perform binary search to find the optimal cut height
    while low <= high:
        # Calculate the mid cut height
        mid = low + (high - low) // 2

        # Check if we can achieve the required amount of wood with the current cut height
        if canAchieveWoodAmount(lengths, requiredAmount, mid):
            # Update the optimal height
            optimalHeight = mid
            # Try to find a higher cut height
            low = mid + 1
        else:
            # Reduce the cut height
            high = mid - 1

    # Return the optimal cut height found
    return optimalHeight


lengths = [20, 15, 10, 17]
requiredAmount = 7
print(findMaxCutHeight(lengths, requiredAmount))


'''
Time Complexity: O(n log H)

Reason:
Binary search is performed over possible cut heights up to H, the maximum
tree height. Each feasibility check scans all n trees.

Space Complexity: O(1)

Reason:
Only totalWood and binary-search variables are used.
'''
