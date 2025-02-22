#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// Function to find the index of the person with the maximum balance (creditor)
int getMax(const vector<int>& balance) {
    int maxIndex = 0;
    for (int i = 1; i < balance.size(); i++) {
        if (balance[i] > balance[maxIndex]) {
            maxIndex = i;
        }
    }
    return maxIndex;
}

// Function to find the index of the person with the minimum balance (debtor)
int getMin(const vector<int>& balance) {
    int minIndex = 0;
    for (int i = 1; i < balance.size(); i++) {
        if (balance[i] < balance[minIndex]) {
            minIndex = i;
        }
    }
    return minIndex;
}

// Recursive function to minimize cash flow
void minimizeCashFlowRec(vector<int>& balance) {
    // Find the most creditor and most debtor
    int maxCredit = getMax(balance); // Index of the most creditor
    int maxDebit = getMin(balance);  // Index of the most debtor

    // Base case: If all balances are settled (0), return
    if (balance[maxCredit] == 0 && balance[maxDebit] == 0) {
        return;
    }

    // Settle the minimum amount between the largest credit and debt
    int settleAmount = min(balance[maxCredit], -balance[maxDebit]);

    // Settle the transaction
    balance[maxCredit] -= settleAmount;
    balance[maxDebit] += settleAmount;

    // Output the transaction
    cout << "Person " << maxDebit << " pays " << settleAmount << " to Person " << maxCredit << "." << endl;

    // Recur for the remaining balances
    minimizeCashFlowRec(balance);
}

// Main function to minimize cash flow among friends
void minimizeCashFlow(vector<vector<int>>& graph) {
    int N = graph.size(); // Number of people
    vector<int> balance(N, 0);

    // Step 1: Calculate net balances for each person
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            balance[i] += (graph[j][i] - graph[i][j]);
        }
    }

    // Step 2: Recursively minimize cash flow using net balances
    minimizeCashFlowRec(balance);
}

int main() {
    // Example graph: graph[i][j] indicates the amount person i owes to person j
    vector<vector<int>> graph = {
        {0, 50, 0},
        {0, 0, 30},
        {40, 0, 0}
    };

    cout << "Transactions to minimize cash flow:" << endl;
    minimizeCashFlow(graph);

    return 0;
}

/*
This program minimizes the number of transactions required to settle debts among friends.

### How It Works:
1. **Input Representation**:
   - The debts are represented as a graph using an adjacency matrix `graph[i][j]`.
   - `graph[i][j]` indicates how much Person `i` owes to Person `j`.

2. **Step 1: Calculate Net Balances**:
   - Compute the net balance for each person:
     - Positive balance means the person is a **creditor** (money owed to them).
     - Negative balance means the person is a **debtor** (they owe money).
   - This is done by iterating over the graph and calculating:
     `balance[i] = total_received_by_i - total_given_by_i`.

3. **Step 2: Recursive Settlement**:
   - Find the most creditor (maximum positive balance) and the most debtor (maximum negative balance).
   - Settle the debt between them:
     - Transfer the minimum amount of money between their balances.
     - Update their balances.
   - Repeat this step until all balances are settled (all are zero).

4. **Step 3: Output the Transactions**:
   - For each settlement, a transaction is printed in the format:
     `Person X pays Y to Person Z.`

### Example:
Input:
    Person 0 owes $50 to Person 1.
    Person 1 owes $30 to Person 2.
    Person 2 owes $40 to Person 0.

Net Balances:
    Person 0: -10
    Person 1: +20
    Person 2: -10

Transactions:
    1. Person 0 pays $10 to Person 1.
    2. Person 2 pays $10 to Person 1.

### Complexity:
1. **Net Balance Calculation**:
   - \(O(N^2)\) for traversing the adjacency matrix.
2. **Recursive Settlement**:
   - In the worst case, there are \(O(N)\) recursive calls, and each requires \(O(N)\) to find max/min.
   - Total: \(O(N^2)\).

Overall Complexity: \(O(N^2)\).

### Use Case:
This program is ideal for settling debts among a group of people with minimal transactions.
*/
