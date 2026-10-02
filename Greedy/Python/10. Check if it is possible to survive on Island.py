def survival(S, N, M):
    if S <= 0 or M == 0:
        print("Yes 0")
    elif N <= 0 or ((N * 6 < M * 7 and S > 6) or M > N):
        print("No")
    else:
        totalFoodRequired = M * S
        days = totalFoodRequired // N
        if totalFoodRequired % N != 0:
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
