#include <iostream>
#include <vector>
#include <stack>
#include <queue>
using namespace std;

int checkMirrorTree(int n, int e, int A[], int B[]) {
    // Create stacks and queues for each node
    vector<stack<int>> stacks(n + 1);
    vector<queue<int>> queues(n + 1);

    // Populate the stack for Tree A
    for (int i = 0; i < 2 * e; i += 2) {
        int u = A[i];
        int v = A[i + 1];
        stacks[u].push(v);
    }

    // Populate the queue for Tree B
    for (int i = 0; i < 2 * e; i += 2) {
        int u = B[i];
        int v = B[i + 1];
        queues[u].push(v);
    }

    // Compare the stack and queue for each node
    for (int i = 1; i <= n; i++) {
        // While both stack and queue have elements
        while (!stacks[i].empty() && !queues[i].empty()) {
            // Check if the top of the stack matches the front of the queue
            if (stacks[i].top() != queues[i].front()) return 0;
            stacks[i].pop();
            queues[i].pop();
        }

        // If one of them still has elements, they aren't mirrors
        if (!stacks[i].empty() || !queues[i].empty()) return 0;
    }

    // If all nodes matched in reverse order, the trees are mirrors
    return 1;
}

// Example usage
int main() {
    int n = 3, e = 2;
    int A[] = {1, 2, 1, 3};
    int B[] = {1, 3, 1, 2};

    int result = checkMirrorTree(n, e, A, B);
    cout << result << endl; // Output should be 1 (true)

    return 0;
}
