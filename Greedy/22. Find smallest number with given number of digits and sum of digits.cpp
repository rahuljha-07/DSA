#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Function to find the smallest number with the given sum of digits and number of digits
string findSmallest(int s, int d) {
    // Case 1: If the sum of digits is 0 and we need only 1 digit, the answer is "0"
    if (s == 0) {
        if (d == 1) {
            return "0";
        } else {
            return "-1"; // Not possible
        }
    }

    // Case 2: If the sum of digits exceeds the maximum possible sum for d digits, return -1
    if (s > 9 * d) {
        return "-1"; // Not possible
    }

    // Array to store digits of the result
    vector<int> result(d, 0);

    // Subtract 1 from the sum to ensure the most significant digit is not zero
    s -= 1;

    // Fill the digits from the least significant position
    for (int i = d - 1; i > 0; i--) {
        if (s > 9) {
            result[i] = 9;
            s -= 9;
        } else {
            result[i] = s;
            s = 0;
        }
    }

    // Assign the remaining sum to the most significant digit
    result[0] = s + 1;

    // Convert the result to a string
    string smallestNumber = "";
    for (int digit : result) {
        smallestNumber += to_string(digit);
    }

    return smallestNumber;
}

// Driver code
int main() {
    int s, d;

    cout << "Enter the sum of digits (s): ";
    cin >> s;
    cout << "Enter the number of digits (d): ";
    cin >> d;

    string result = findSmallest(s, d);
    if (result == "-1") {
        cout << "Not possible" << endl;
    } else {
        cout << "Smallest number is: " << result << endl;
    }

    return 0;
}
