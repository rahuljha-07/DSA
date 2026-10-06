import sys


# Recursive function to find the maximum time you can survive
def maxSurvivalTime(health, armor, currentPlace):
    # Base case: If health or armor becomes <= 0, return 0
    if health <= 0 or armor <= 0:
        return 0
    # Recursive cases
    # Current place: Fire
    if currentPlace == 0:
        return 1 + max(
            maxSurvivalTime(health + 3, armor + 2, 1),
            # Move to Water
            maxSurvivalTime(health - 5, armor - 10, 2),
        )
    if currentPlace == 1:
        return 1 + max(
            maxSurvivalTime(health - 20, armor + 5, 0),
            maxSurvivalTime(health - 5, armor - 10, 2),
        )
    return 1 + max(
        maxSurvivalTime(health - 20, armor + 5, 0),
        # Move to Air
        maxSurvivalTime(health + 3, armor + 2, 1),
    )


# Function to handle each test case
def solve(health, armor):
    return max(
        maxSurvivalTime(health - 20, armor + 5, 0),
        # Start from Air
        maxSurvivalTime(health + 3, armor + 2, 1),
        # Start from Water
        maxSurvivalTime(health - 5, armor - 10, 2),
    )


def main():
    tokens = iter(map(int, sys.stdin.read().split()))
    t = next(tokens)
    for _ in range(t):
        health = next(tokens)
        armor = next(tokens)
        print(solve(health, armor))


if __name__ == "__main__":
    main()


'''
Let D be the maximum number of surviving transitions along any branch.
Time: O(2^D), a worst-case upper bound: each surviving call tries two
different next places, and repeated states are not memoized. D is O(H)
for initial positive health H: air cannot be chosen consecutively, and
even an air/water pair decreases health by 2. Armor can end branches sooner.
Space: O(D) auxiliary for the recursion stack; branches run sequentially,
so the whole exponential recursion tree is not stored.
The source's exhaustive recursion is retained, including its practical
runtime and Python recursion-depth limits on large inputs.
'''
