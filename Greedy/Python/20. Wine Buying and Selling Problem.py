import sys


def wineSelling(arr, n):
    buyer = 0
    seller = 0
    cost = 0
    while buyer < n and seller < n:
        while buyer < n and arr[buyer] <= 0:
            buyer += 1
        while seller < n and arr[seller] >= 0:
            seller += 1
        if buyer == n or seller == n:
            break
        transaction = min(arr[buyer], -arr[seller])
        cost += abs(buyer - seller) * transaction
        arr[buyer] -= transaction
        arr[seller] += transaction
    return cost


def main():
    tokens = iter(map(int, sys.stdin.read().split()))
    n = next(tokens)
    arr = [next(tokens) for _ in range(n)]
    print(wineSelling(arr, n))


if __name__ == "__main__":
    main()


'''
Let n be the number of houses, with balanced total supply and demand.
Time: O(n): buyer and seller only move forward. Each transaction exhausts
at least one house, so there are at most O(n) transactions despite the
nested while loops.
Space: O(1) auxiliary inside wineSelling: transactions update arr in place
and only indices and totals are stored. Main stores O(n) input data.
Unbalanced inputs retain the source's behavior of returning a partial cost.
'''
