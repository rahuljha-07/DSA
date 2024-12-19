#include <iostream>
#include <vector>
#include <algorithm> // For reverse
using namespace std;

// Helper function to multiply a number with the result stored in a vector
void multiply(int x, vector<int>& res) {
    int carry = 0; // Initialize carry to 0

    // Multiply x with every digit in the vector
    for (int i = 0; i < res.size(); i++) {
        int prod = res[i] * x + carry; // Calculate the product plus carry
        res[i] = prod % 10;            // Store the last digit in the current position
        carry = prod / 10;             // Update carry with the remaining digits
    }

    // If carry is left, add it to the result vector
    while (carry) {
        res.push_back(carry % 10); // Add the last digit of the carry to the vector
        carry = carry / 10;        // Remove the last digit from carry
    }
}

// Function to compute factorial of N
vector<int> factorial(int N) {
    vector<int> res; // Vector to store the result
    res.push_back(1); // Initialize the result with 1

    // Multiply numbers from 2 to N with the result
    for (int x = 2; x <= N; x++) {
        multiply(x, res);
    }

    // The result is stored in reverse order, so reverse it before returning
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    int N = 100; // Example: Find factorial of 100
    vector<int> result = factorial(N);

    cout << "Factorial of " << N << " is: ";
    for (int digit : result) {
        cout << digit;
    }
    cout << endl;

    return 0;
}
