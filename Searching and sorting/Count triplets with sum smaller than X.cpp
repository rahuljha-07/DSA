#include <algorithm> // for std::sort
using namespace std;

// Function to count the number of triplets in the array such that their sum is less than a given value x
long long countTriplets(long long arr[], int n, long long x) {
    // Sort the array to enable the two-pointer technique
    sort(arr, arr + n);
    long long count = 0; // Variable to store the count of valid triplets

    // Iterate through the array with the first element of the triplet
    for (int i = 0; i < n - 2; i++) {
        int left = i + 1; // Pointer for the second element
        int right = n - 1; // Pointer for the third element

        // Use the two-pointer technique to find pairs of elements that sum with arr[i] to less than x
        while (left < right) {
            // Check if the sum of the triplet is less than x
            if ((arr[i] + arr[left] + arr[right]) < x) {
                // If the sum is less than x, all elements between left and right are valid pairs
                count += (right - left); // Count all pairs (left,...,right-1 ,right) 
                // 1,2,3,4,5,6 -> 1+2+6 <10 so 1+2+5, 1+2+4... all are smaller 
                left++; // Move the left pointer to the right
            } else {
                // If the sum is greater than or equal to x, move the right pointer to the left
                right--;
            }
        }
    }
    
    return count; // Return the total count of valid triplets
}

// Example usage

int main() {
    long long arr[] = {5, 1, 3, 4, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    long long x = 12;
    
    long long result = countTriplets(arr, n, x);
    cout << "Count of triplets: " << result << endl; // Should output the count of valid triplets
    
    return 0;
}
