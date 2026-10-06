import sys


# Function to calculate the minimum cost of wine buying and selling
def wineSelling(arr, n):
    # Buyer and seller pointers
    buyer = 0
    seller = 0
    # Total cost
    cost = 0
    # Iterate until all buying and selling are complete
    while buyer < n and seller < n:
        while buyer < n and arr[buyer] <= 0:
            buyer += 1
        while seller < n and arr[seller] >= 0:
            seller += 1
        # Break if no buyers or sellers are left
        if buyer == n or seller == n:
            break
        # Calculate the transaction
        # Max wine that can be transferred
        transaction = min(arr[buyer], -arr[seller])
        # Add cost based on distance
        cost += abs(buyer - seller) * transaction
        # Reduce the buyer's demand
        arr[buyer] -= transaction
        # Reduce the seller's supply
        arr[seller] += transaction
    # Return the total cost
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
