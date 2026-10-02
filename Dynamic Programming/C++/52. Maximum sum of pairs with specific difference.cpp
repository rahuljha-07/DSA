#include <bits/stdc++.h>
using namespace std;

long long maxSumOfPairsWithDiffLessThanK(vector<int> a, int K) {
    sort(a.begin(), a.end());
    long long ans = 0;
    for (int i = (int)a.size() - 1; i > 0; ) {
        if (a[i] - a[i-1] < K) {
            ans += a[i] + a[i-1];
            i -= 2;            // use both
        } else {
            --i;               // skip the larger one
        }
    }
    return ans;
}

// Demo
int main() {
    vector<int> arr1 = {3, 5, 10, 15, 17, 12, 9};
    int K1 = 4;
    cout << maxSumOfPairsWithDiffLessThanK(arr1, K1) << "\n"; // 62

    vector<int> arr2 = {5, 15, 10, 300};
    int K2 = 12;
    cout << maxSumOfPairsWithDiffLessThanK(arr2, K2) << "\n"; // 25
    return 0;
}
