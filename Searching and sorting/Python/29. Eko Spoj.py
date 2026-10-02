def canAchieveWoodAmount(lengths, requiredAmount, cutHeight):
    totalWood = 0

    for length in lengths:
        if length > cutHeight:
            totalWood += length - cutHeight

    return totalWood >= requiredAmount


def findMaxCutHeight(lengths, requiredAmount):
    low = 0
    high = max(lengths)
    optimalHeight = -1

    while low <= high:
        mid = low + (high - low) // 2

        if canAchieveWoodAmount(lengths, requiredAmount, mid):
            optimalHeight = mid
            low = mid + 1
        else:
            high = mid - 1

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
