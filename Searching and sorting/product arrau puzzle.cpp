#include <vector>
using namespace std;

// Function to calculate the product of array elements except itself
vector<long long int> productExceptSelf(vector<long long int>& nums, int n) {
    // Create two vectors to store the left and right products
    vector<long long int> l(n), r(n);
    
    // Initialize the first element of the left product vector to 1
    l[0] = 1; 
    
    // Initialize the last element of the right product vector to 1
    r[n - 1] = 1; 

    // Fill the left product vector
    for (int i = 1; i < n; i++) {
        // Each position l[i] contains the product of all elements to the left of nums[i]
        l[i] = l[i - 1] * nums[i - 1];
    }
    
    // Fill the right product vector
    for (int i = n - 2; i >= 0; i--) {
        // Each position r[i] contains the product of all elements to the right of nums[i]
        r[i] = r[i + 1] * nums[i + 1];
    }
    
    // Calculate the final result by multiplying left and right products
    for (int i = 0; i < n; i++) {
        // Each position nums[i] now contains the product of all elements except nums[i]
        nums[i] = l[i] * r[i];
    }
    
    // Return the modified nums vector which contains the result
    return nums;    
}
