#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Function to count the number of set bits in an integer
int countSetBits(int n) {
    int count = 0;
    while (n) {
        count += (n & 1);
        n >>= 1; // Right shift the number
    }
    return count;
}

// Custom comparator for sorting
bool compare(int a, int b) {
    int setBitsA = countSetBits(a);
    int setBitsB = countSetBits(b);
    // Sort by set bit count (descending)
    return (setBitsA > setBitsB);
}

// Function to sort the array by set bit count
void sortBySetBitCount(vector<int>& arr) {
    sort(arr.begin(), arr.end(), compare);
}

int main() {
    vector<int> arr = {5, 2, 3, 9, 4, 6, 7, 15, 32};
    
    // Sort the array by set bit count
    sortBySetBitCount(arr);
    
    // Print the sorted array
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
