# Recursive function to calculate derangements
def countDerangementsHelper(n, memo):
    # Base cases
    # One way to arrange 0 items (do nothing)
    if n == 0:
        return 1
    # No way to derange 1 item
    if n == 1:
        return 0
    # If the value is already calculated, return it
    if memo[n] != -1:
        return memo[n]
    # Recursive formula: D(n) = (n-1) * (D(n-1) + D(n-2))
    memo[n] = (n - 1) * (
        countDerangementsHelper(n - 1, memo) + countDerangementsHelper(n - 2, memo)
    )
    return memo[n]


# Wrapper function for memoization
def countDerangements(n):
    # Memoization table initialized with -1
    memo = [-1] * (n + 1)
    return countDerangementsHelper(n, memo)


def main():
    n = 3
    print(f"Number of derangements for {n}:", countDerangements(n))


if __name__ == "__main__":
    main()


'''
Let n>=0 be the number of elements.
Time: O(n+1) arithmetic operations: each size is memoized once using
D(n)=(n-1)*(D(n-1)+D(n-2)).
Space: O(n+1) memo entries and O(n) recursion depth under unit-size counts.
Python counts have O(n log(n+1)) bits at size n; storing all memo values
can require O(n^2 log(n+1)) bits, and big-integer arithmetic adds time.
'''
