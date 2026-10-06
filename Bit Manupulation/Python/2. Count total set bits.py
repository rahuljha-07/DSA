# Function to count the number of set bits in numbers from 0 to num
def countBits(num):
    # list to store results for numbers 0 to num
    ans = [0] * (num + 1)
    for i in range(num + 1):
        # Calculate the number of set bits for each number
        ans[i] = rec(i)
    # Return the list
    return ans


# Recursive function to count the number of set bits for a single number
def rec(num):
    # Base case: 0 has 0 set bits
    if num == 0:
        return 0
    # Base case: 1 has 1 set bit
    if num == 1:
        return 1
    # If even, use the result of num / 2
    if num % 2 == 0:
        return rec(num // 2)
    # If odd, use 1 + result of num / 2
    return 1 + rec(num // 2)


def main():
    num = 5
    result = countBits(num)
    print(f"Number of set bits from 0 to {num}:")
    for i in range(num + 1):
        print(f"Number: {i}, Set Bits: {result[i]}")


if __name__ == "__main__":
    main()


'''
Let N=num>=0.
Time: O((N+1) log(N+2)): every number from 0 to N is counted separately,
and rec halves its argument at each level. No memoization is added.
Space: O(log(N+2)) auxiliary recursion depth plus O(N+1) output in ans.
Bit-operation costs assume the source's fixed-width integer domain.
'''
