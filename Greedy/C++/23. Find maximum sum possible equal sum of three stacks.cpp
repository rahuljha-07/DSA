#include <iostream>
#include <vector>
using namespace std;

// Function to find the maximum possible sum of three stacks
int maxSum(vector<int>& stack1, vector<int>& stack2, vector<int>& stack3, int n1, int n2, int n3) {
    // Calculate the initial sums of the three stacks
    int sum1 = 0, sum2 = 0, sum3 = 0;

    for (int i = 0; i < n1; i++) {
        sum1 += stack1[i];
    }
    for (int i = 0; i < n2; i++) {
        sum2 += stack2[i];
    }
    for (int i = 0; i < n3; i++) {
        sum3 += stack3[i];
    }

    // Pointers to the tops of the stacks
    int top1 = 0, top2 = 0, top3 = 0;

    // Loop until we find the maximum possible equal sum
    while (true) {
        // If any stack becomes empty, return 0
        if (top1 == n1 || top2 == n2 || top3 == n3) {
            return 0;
        }

        // If the sums of all three stacks are equal, return the sum
        if (sum1 == sum2 && sum2 == sum3) {
            return sum1;
        }

        // Remove the top element from the stack with the largest sum
        if (sum1 >= sum2 && sum1 >= sum3) {
            sum1 -= stack1[top1++];
        } else if (sum2 >= sum1 && sum2 >= sum3) {
            sum2 -= stack2[top2++];
        } else if (sum3 >= sum1 && sum3 >= sum2) {
            sum3 -= stack3[top3++];
        }
    }
}

int main() {
    // Example stacks
    vector<int> stack1 = {3, 2, 1, 1, 1};
    vector<int> stack2 = {4, 3, 2};
    vector<int> stack3 = {1, 1, 4, 1};

    int n1 = stack1.size();
    int n2 = stack2.size();
    int n3 = stack3.size();

    // Call the function and display the result
    cout << "Maximum possible sum: " << maxSum(stack1, stack2, stack3, n1, n2, n3) << endl;

    return 0;
}
