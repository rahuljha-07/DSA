def getMax(balance):
    maxIndex = 0
    for i in range(1, len(balance)):
        if balance[i] > balance[maxIndex]:
            maxIndex = i
    return maxIndex


def getMin(balance):
    minIndex = 0
    for i in range(1, len(balance)):
        if balance[i] < balance[minIndex]:
            minIndex = i
    return minIndex


def minimizeCashFlowRec(balance):
    if not balance:
        return
    maxCredit = getMax(balance)
    maxDebit = getMin(balance)
    if balance[maxCredit] == 0 and balance[maxDebit] == 0:
        return
    settleAmount = min(balance[maxCredit], -balance[maxDebit])
    balance[maxCredit] -= settleAmount
    balance[maxDebit] += settleAmount
    print(f"Person {maxDebit} pays {settleAmount} to Person {maxCredit}.")
    minimizeCashFlowRec(balance)


def minimizeCashFlow(graph):
    N = len(graph)
    balance = [0] * N
    for i in range(N):
        for j in range(N):
            balance[i] += graph[j][i] - graph[i][j]
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
