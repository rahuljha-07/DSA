def countSetBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def sortBySetBitCount(arr):
    arr.sort(key=countSetBits, reverse=True)


arr = [5, 2, 3, 9, 4, 6, 7, 15, 32]
sortBySetBitCount(arr)

for num in arr:
    print(num, end=" ")
print()


'''
Time Complexity: O(n log n * b)

Reason:
Sorting n elements costs O(n log n) comparisons/key work. Counting set bits
for a number takes O(b), where b is the number of bits in the number.

Space Complexity: O(1) auxiliary

Reason:
The algorithm sorts the input list in place. Python sorting may use internal
temporary memory, but no explicit extra list is created by the algorithm.
'''
