#include <iostream>
#include <algorithm>
using namespace std;

// Recursive function to find the maximum time you can survive
int maxSurvivalTime(int health, int armor, int currentPlace) {
    // Base case: If health or armor becomes <= 0, return 0
    if (health <= 0 || armor <= 0) {
        return 0;
    }

    // Recursive cases
    if (currentPlace == 0) { // Current place: Fire
        // Move to Air or Water
        return 1 + max(maxSurvivalTime(health + 3, armor + 2, 1), // Move to Air
                       maxSurvivalTime(health - 5, armor - 10, 2)); // Move to Water
    } else if (currentPlace == 1) { // Current place: Air
        // Move to Fire or Water
        return 1 + max(maxSurvivalTime(health - 20, armor + 5, 0), // Move to Fire
                       maxSurvivalTime(health - 5, armor - 10, 2)); // Move to Water
    } else { // Current place: Water
        // Move to Fire or Air
        return 1 + max(maxSurvivalTime(health - 20, armor + 5, 0), // Move to Fire
                       maxSurvivalTime(health + 3, armor + 2, 1)); // Move to Air
    }
}

// Function to handle each test case
int solve(int health, int armor) {
    // Start from any of the three places and return the maximum survival time
    return max({maxSurvivalTime(health - 20, armor + 5, 0), // Start from Fire
                maxSurvivalTime(health + 3, armor + 2, 1), // Start from Air
                maxSurvivalTime(health - 5, armor - 10, 2)}); // Start from Water
}

int main() {
    int t;
    cin >> t; // Number of test cases

    while (t--) {
        int health, armor;
        cin >> health >> armor; // Initial health and armor

        // Solve for the given health and armor
        cout << solve(health, armor) << endl;
    }

    return 0;
}

/*
Explanation:
Recursive Function:

maxSurvivalTime(health, armor, currentPlace) calculates the maximum time you can survive given the current health, armor, and the place you're currently in (currentPlace).
Base Case:
If health or armor becomes ≤ 0 return  0 because survival ends.
Recursive Case:
Depending on the current place, calculate the survival time for the next possible places:
Fire: Move to Air or Water.
Air: Move to Fire or Water.
Water: Move to Fire or Air.
Solve Function:

Starts from any of the three places and returns the maximum survival time.
Driver Code:

Reads input and solves the problem for each test case using the solve function.
*/