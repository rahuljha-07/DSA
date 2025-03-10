#include <bits/stdc++.h>
using namespace std;

// Function to recursively find the maximum number
void findMaxNumber(string &str, int k, string &maxNum, int index) {
    if (k == 0) return;  // No swaps left

    char maxChar = str[index];

    // Find the maximum character from index to end
    for (int i = index + 1; i < str.size(); i++) {
        if (str[i] > maxChar) 
            maxChar = str[i];
    }

    // If current index already has the max digit, move to next
    if (maxChar == str[index]) {
        findMaxNumber(str, k, maxNum, index + 1);
        return;
    }

    k--;  // Swap will happen, so decrease k

    // Swap with every occurrence of maxChar from right to left
    for (int i = index; i < str.size(); i++) {
        if (str[i] == maxChar) {
            swap(str[index], str[i]);

            if (str > maxNum) 
                maxNum = str;

            findMaxNumber(str, k, maxNum, index + 1);

            swap(str[index], str[i]);  // Backtrack
        }
    }
}

// Function to get the largest number with at most K swaps
string findMaximumNum(string str, int k) {
    string maxNum = str;
    findMaxNumber(str, k, maxNum, 0);
    return maxNum;
}

// Driver code
int main() {
    int k;
    string str;

    cout << "Enter the number of swaps (K): ";
    cin >> k;

    cout << "Enter the string of digits: ";
    cin >> str;

    cout << "Largest number possible: " << findMaximumNum(str, k) << endl;

    return 0;
}
