#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

    int n;
    cin >> n; // Number of elements in the array
    vector<int> arr(n);
    int countOnes = 0; // Counter for the number of 1s

    // Input array and count the number of 1s
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        if (arr[i] == 1) {
            countOnes++;
        }
    }

    // Sort the array in descending order
    sort(arr.begin(), arr.end(), greater<int>());

    // Output all 1s first
    for (int i = 0; i < countOnes; i++) {
        cout << "1 ";
    }

    // Special case: If there are exactly two elements left and they are 3 and 2
    if ((n - countOnes) == 2 && arr[0] == 3 && arr[1] == 2) {
        cout << "2 3" << endl;
    } else {
        // Output the remaining elements
        for (int i = 0; i < (n - countOnes); i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }

    return 0;
}
