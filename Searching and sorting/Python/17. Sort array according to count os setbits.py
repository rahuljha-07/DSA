# Function to count the number of set bits in an integer
def countSetBits(n):
    count = 0
    while n:
        count += n & 1
        # Right shift the number
        n >>= 1
    return count


# Function to sort the array by set bit count
def sortBySetBitCount(arr):
    # Use each number's set-bit count as the descending sort key.
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
