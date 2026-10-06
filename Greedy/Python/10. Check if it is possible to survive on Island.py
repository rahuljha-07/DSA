# Function to determine if survival is possible and the minimum days to buy food
def survival(S, N, M):
    if S <= 0 or M == 0:
        print("Yes 0")
    # Check if survival is not possible
    # Condition 1: We can't buy at least 7 days' worth of food in the first 6 days (when S >
    # 6)
    # Condition 2: Daily food requirement exceeds the food that can be bought in a day
    elif N <= 0 or ((N * 6 < M * 7 and S > 6) or M > N):
        # Survival is not possible
        print("No")
    else:
        # Survival is possible
        # Calculate the total units of food required
        totalFoodRequired = M * S
        # Calculate the minimum days to buy food
        # We need ceil(totalFoodRequired / N), but we use integer math for efficiency
        days = totalFoodRequired // N
        if totalFoodRequired % N != 0:
            # Add an extra day if there's a remainder
            days += 1
        print("Yes", days)


def main():
    S = 10
    N = 16
    M = 2
    survival(S, N, M)


if __name__ == "__main__":
    main()


'''
Time: O(1) under fixed-size integer arithmetic: feasibility and the
ceiling purchase-day count use a fixed number of operations, no day loop.
Space: O(1) auxiliary numeric variables. Very large Python integers add
bit-length-dependent arithmetic/storage.
S/N/M are nonnegative; day 1 is Monday and shops close on Sundays.
Six purchase days must cover seven consumption days for weeks to be feasible.
'''
