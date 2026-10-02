def isInArithmeticSequence(start, target, difference):
    if start == target:
        return 1

    if difference == 0:
        return 0

    if (target - start > 0 and difference < 0) or (target - start < 0 and difference > 0):
        return 0

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
