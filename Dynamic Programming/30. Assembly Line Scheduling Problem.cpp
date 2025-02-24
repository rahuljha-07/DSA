#include <iostream>
#include <algorithm> // For std::min
using namespace std;

// Function to calculate the minimum time to assemble a car
int carAssembly(int a[][4], int t[][4], int e[], int x[]) {
    int T1[4], T2[4]; // Arrays to store the minimum time at each station for each line

    // Initialize the first station times with entry times
    T1[0] = e[0] + a[0][0];
    T2[0] = e[1] + a[1][0];

    // Compute the minimum times for each station
    for (int i = 1; i < 4; ++i) {
        T1[i] = min(T1[i - 1] + a[0][i], T2[i - 1] + t[1][i] + a[0][i]);
        T2[i] = min(T2[i - 1] + a[1][i], T1[i - 1] + t[0][i] + a[1][i]);
    }

    // Add the exit times and return the overall minimum time
    return min(T1[3] + x[0], T2[3] + x[1]);
}

int main() {
    // Station processing times
    int a[2][4] = { 
        { 4, 5, 3, 2 },
        { 2, 10, 1, 4 } 
    };

    // Line switching times
    int t[2][4] = { 
        { 0, 7, 4, 5 },
        { 0, 9, 2, 8 } 
    };

    // Entry and exit times for each line
    int e[] = { 10, 12 }; // Entry times
    int x[] = { 18, 7 };  // Exit times

    // Calculate and print the result
    cout << "Minimum time to assemble the car: " << carAssembly(a, t, e, x) << endl;

    return 0;
}
