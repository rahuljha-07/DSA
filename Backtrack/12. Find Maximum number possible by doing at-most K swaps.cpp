#include <bits/stdc++.h>
using namespace std;

// Function to find the maximum number
void findMaximum(string str, int k, string &maxNum, int currentIndex) {
    // If no swaps are left, return
    if (k == 0) 
        return;

    // Store the current character for comparison
    char maxChar = str[currentIndex];

    // Find the maximum character from the current index to the end of the string
    for (int i = currentIndex + 1; i < str.size(); i++) {
        if (str[i] > maxChar) 
            maxChar = str[i];
    }

    // If the maximum character is the current character, no swaps are needed
    if (maxChar != str[currentIndex]) 
        k--;

    // Explore all positions with the maximum character
    for (int i = currentIndex; i < str.size(); i++) {
        if (str[i] == maxChar) {
            // Swap the current character with the maximum character
            swap(str[currentIndex], str[i]);

            // If the swapped string is greater than the current maxNum, update it
            if (str > maxNum) 
                maxNum = str;

            // Recursively call for the next index with the remaining swaps
            findMaximum(str, k, maxNum, currentIndex + 1);

            // Backtrack: Restore the original state of the string
            swap(str[currentIndex], str[i]);
        }
    }
}

// Function to find the largest number with at most K swaps
string findMaximumNum(string str, int k) {
    string maxNum = str;

    // Start the recursion
    findMaximum(str, k, maxNum, 0);

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

    // Get the largest number possible with K swaps
    string result = findMaximumNum(str, k);

    cout << "Largest number possible: " << result << endl;

    return 0;
}
