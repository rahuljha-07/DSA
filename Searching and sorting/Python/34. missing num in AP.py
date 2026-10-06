# Function to determine if B can be reached from A by adding C repeatedly.
# A: starting number, B: target number, C: common difference
def isInArithmeticSequence(start, target, difference):
    # If the starting number is equal to the target number, return true (1)
    if start == target:
        return 1

    # If the common difference is 0, we cannot reach the target unless they are the same
    if difference == 0:
        return 0

    # Check if moving from start to target is possible with the given difference
    # If the difference in numbers is of opposite sign to the common difference, return
    # false (0)
    if (target - start > 0 and difference < 0) or (target - start < 0 and difference > 0):
        return 0

    # Return true (1) if the difference between target and start is a multiple of the common
    # difference
    return 1 if (target - start) % difference == 0 else 0


print(isInArithmeticSequence(1, 7, 2))
print(isInArithmeticSequence(1, 8, 2))


'''
Time Complexity: O(1)

Reason:
The function performs only a fixed number of arithmetic and comparison
operations, independent of input size.

Space Complexity: O(1)

Reason:
No extra data structure is used.
'''
