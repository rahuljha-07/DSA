# Function to find the index of the person with the maximum balance (creditor)
def getMax(balance):
    maxIndex = 0
    for i in range(1, len(balance)):
        if balance[i] > balance[maxIndex]:
            maxIndex = i
    return maxIndex


# Function to find the index of the person with the minimum balance (debtor)
def getMin(balance):
    minIndex = 0
    for i in range(1, len(balance)):
        if balance[i] < balance[minIndex]:
            minIndex = i
    return minIndex


# Recursive function to minimize cash flow
def minimizeCashFlowRec(balance):
    if not balance:
        return
    # Find the most creditor and most debtor
    # Index of the most creditor
    maxCredit = getMax(balance)
    # Index of the most debtor
    maxDebit = getMin(balance)
    # Base case: If all balances are settled (0), return
    if balance[maxCredit] == 0 and balance[maxDebit] == 0:
        return
    # Settle the minimum amount between the largest credit and debt
    settleAmount = min(balance[maxCredit], -balance[maxDebit])
    # Settle the transaction
    balance[maxCredit] -= settleAmount
    balance[maxDebit] += settleAmount
    # Output the transaction
    print(f"Person {maxDebit} pays {settleAmount} to Person {maxCredit}.")
    # Recur for the remaining balances
    minimizeCashFlowRec(balance)


def minimizeCashFlow(graph):
    # Number of people
    N = len(graph)
    balance = [0] * N
    # Step 1: Calculate net balances for each person
    for i in range(N):
        for j in range(N):
            balance[i] += graph[j][i] - graph[i][j]
    # Step 2: Recursively minimize cash flow using net balances
    minimizeCashFlowRec(balance)


def main():
    graph = [[0, 50, 0], [0, 0, 30], [40, 0, 0]]
    print("Transactions to minimize cash flow:")
    minimizeCashFlow(graph)


if __name__ == "__main__":
    main()


'''
Let N be people count.
Time: O(N^2): compute net balances from N^2 entries; each settlement
scans N balances for extremes and clears at least one nonzero balance,
so at most N-1 settlements also cost O(N^2).
Space: O(N) auxiliary balance array and recursive depth; transactions
are printed directly. This preserves the greedy settlement heuristic,
which is not guaranteed to minimize the number of transactions globally.
'''
