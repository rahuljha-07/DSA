def canMakeParathas(cookingTimes, par, timeLimit):
    totalParathas = 0

    for i in range(len(cookingTimes)):
        time = cookingTimes[i]
        multiplier = 2

        while time <= timeLimit:
            totalParathas += 1
            time += cookingTimes[i] * multiplier
            multiplier += 1

        if totalParathas >= par:
            return 1

    return 0


def findMinimumTime(cookingTimes, par):
    lowerBound = 0
    upperBound = int(1e8)
    ans = 0

    while lowerBound <= upperBound:
        mid = (lowerBound + upperBound) // 2

        if canMakeParathas(cookingTimes, par, mid):
            ans = mid
            upperBound = mid - 1
        else:
            lowerBound = mid + 1

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
