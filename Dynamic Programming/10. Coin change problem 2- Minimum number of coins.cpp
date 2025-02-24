/*
ek twist hai baaki me nhi
array size 0 , sum chcaiye 1
toh infinite coin chaiye 1 pouchne me, similar for other sum 0 to ... 
thus store INT_MAX -1 , -1 isliye +1 krke overflow na ho

2nd row bhi khud se initlize krni pdegi
jaise arr[0] me 2 hai
toh 2 - 1, 4-2,...
jaha divide nhi hua udhar INT_MAX-1 krdo

code me max ko min krdo
1+ kro jb coin lia 
baaki exact same
*/

#include <climits> // For INT_MAX

int coinChangeMinCoins(int coins[], int n, int sum) {
    // Create a DP table `t` with dimensions (n+1) x (sum+1)
    int t[n + 1][sum + 1];

    // Initialize the table
    // If the array size is 0 and sum is greater than 0, we need "infinite" coins (INT_MAX - 1)
    for (int j = 0; j < sum + 1; j++) 
        t[0][j] = INT_MAX - 1; // Use INT_MAX - 1 to prevent overflow when adding 1

    // If the sum is 0, we need 0 coins
    for (int i = 0; i < n + 1; i++) 
        t[i][0] = 0;

    // Special initialization for the second row (only one coin type)
    for (int j = 1; j < sum + 1; j++) {
        if (j % coins[0] == 0) 
            t[1][j] = j / coins[0]; // If divisible, calculate the number of coins
        else 
            t[1][j] = INT_MAX - 1; // Otherwise, set to "infinite"
    }

    // Fill the DP table iteratively
    for (int i = 2; i < n + 1; i++) {         // Loop through coin types
        for (int j = 1; j < sum + 1; j++) {   // Loop through sums
            if (coins[i - 1] <= j) {
                // Include the coin or exclude it
                t[i][j] = min(
                    1 + t[i][j - coins[i - 1]], // Include the coin
                    t[i - 1][j]                // Exclude the coin
                );
            } else {
                // Exclude the coin
                t[i][j] = t[i - 1][j];
            }
        }
    }

    // If no solution exists, return -1
    return (t[n][sum] == INT_MAX - 1) ? -1 : t[n][sum];
}
