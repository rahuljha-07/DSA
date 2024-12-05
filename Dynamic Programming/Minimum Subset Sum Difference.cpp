/*
S2-S1=minimum
S2+S1=Range
S2=range -S1
thus Range -S1 -S1 = minimum
minimum = Range - 2S1

do the same subset code with sum=sum or array value // this way we get all the range

then 
take the last row which has all the element and sum T/F whther that sum exist or not
then take T value which show arr with sum x exist
take only half because s1+s2 is sum and we consider s1 at this moment that why half
then = index of true
for loop 
mini=min(mini, Range-2v[i])
then return mini
*/

int minSubsetSumDifference(int arr[], int n) {
    // Calculate the total sum of the array
    int sum = 0;
    for (int i = 0; i < n; i++) 
        sum += arr[i];

    // Create a DP table `t` with dimensions (n+1) x (sum+1)
    bool t[n + 1][sum + 1];

    // Base case: Initialize table
    for (int i = 0; i < sum + 1; i++) 
        t[0][i] = false; // No items => no subset for sum > 0
    for (int i = 0; i < n + 1; i++) 
        t[i][0] = true;  // Subset with sum 0 always exists (empty subset)

    // Fill the table iteratively
    for (int i = 1; i < n + 1; i++) {
        for (int j = 1; j < sum + 1; j++) {
            if (arr[i - 1] <= j) {
                // Include or exclude the current element
                t[i][j] = t[i - 1][j - arr[i - 1]] || t[i - 1][j];
            } else {
                // Exclude the current element
                t[i][j] = t[i - 1][j];
            }
        }
    }

    // Find all subset sums possible for the last row
    vector<int> validSums;
    for (int j = 0; j <= sum / 2; j++) {
        if (t[n][j]) {
            validSums.push_back(j); // Store all reachable subset sums
        }
    }

    // Calculate the minimum subset sum difference
    int mini = INT_MAX;
    for (int s1 : validSums) {
        int s2 = sum - s1;          // Complementary subset sum
        mini = min(mini, abs(s2 - s1)); // Minimize the difference
    }

    return mini;
}
