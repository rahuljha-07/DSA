#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int maxProfit(int k, vector<int>& prices) {
    int n = prices.size();
    if (n == 0) return 0;

    vector<vector<int>> dp(k + 1, vector<int>(n, 0));

    for (int t = 1; t <= k; t++) {
        int maxVal = INT_MIN;

        for (int d = 1; d < n; d++) {
            if (dp[t - 1][d - 1] - prices[d - 1] > maxVal) {
                maxVal = dp[t - 1][d - 1] - prices[d - 1]; // Update maxVal
            }

            if (maxVal + prices[d] > dp[t][d - 1]) {
                dp[t][d] = maxVal + prices[d]; // Take the best profit
            } else {
                dp[t][d] = dp[t][d - 1]; // Keep previous max profit
            }
        }
    }

    return dp[k][n - 1]; // Final answer
}

int main() {
    int n, k;
    cout << "Enter number of days: ";
    cin >> n;

    vector<int> prices(n);
    cout << "Enter stock prices: ";
    for (int i = 0; i < n; i++) {
        cin >> prices[i];
    }

    cout << "Enter max transactions allowed: ";
    cin >> k;

    cout << "Maximum Profit: " << maxProfit(k, prices) << endl;
    return 0;
}
