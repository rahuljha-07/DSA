#include <iostream>
#include <cmath> // For ceil function
using namespace std;

// Function to determine if survival is possible and the minimum days to buy food
void survival(int S, int N, int M) {
    // Check if survival is not possible
    // Condition 1: We can't buy at least 7 days' worth of food in the first 6 days (when S > 6)
    // Condition 2: Daily food requirement exceeds the food that can be bought in a day
    if (((N * 6) < (M * 7) && S > 6) || M > N) {
        cout << "No" << endl; // Survival is not possible
    } else {
        // Survival is possible
        // Calculate the total units of food required
        int totalFoodRequired = M * S;

        // Calculate the minimum days to buy food
        // We need ceil(totalFoodRequired / N), but we use integer math for efficiency
        int days = totalFoodRequired / N;
        if (totalFoodRequired % N != 0) {
            days += 1; // Add an extra day if there's a remainder
        }

        cout << "Yes " << days << endl; // Output the result
    }
}

// Driver code
int main() {
    int S = 10; // Number of days to survive
    int N = 16; // Maximum food that can be bought in a day
    int M = 2;  // Food required per day

    // Function call to determine survival possibility and minimum days
    survival(S, N, M);

    return 0;
}
