#include <climits>

class Solution {
public:
    int index = 0;  // Track the current index in the preorder array

    // Recursive helper function to verify BST preorder condition
    void solve(int arr[], int& N, int minVal, int maxVal) {
        // If all elements are processed, return
        if (index >= N) return;

        // Check if the current element falls within the allowed range
        if (arr[index] < minVal || arr[index] > maxVal) return;

        // Set current element as root for this subtree
        int curr = arr[index];
        index++;  // Move to the next element

        // Recursively check left subtree with updated max bound
        solve(arr, N, minVal, curr);

        // Recursively check right subtree with updated min bound
        solve(arr, N, curr, maxVal);
    }

    // Main function to verify if array represents a valid BST preorder traversal
    int canRepresentBST(int arr[], int N) {
        int minVal = INT_MIN;  // Initial minimum boundary
        int maxVal = INT_MAX;  // Initial maximum boundary

        // Begin recursive validation of BST conditions
        solve(arr, N, minVal, maxVal);

        // Check if all elements in the array were processed correctly
        return (index == N) ? 1 : 0;
    }
};
// kashish mahendatta video
 int canRepresentBST(int arr[], int n) {
       stack<int> s;
       int parent=0;
       for(int i=0;i<n;i++){
           if(s.empty() || arr[i]<s.top()){
                if(parent>arr[i]){
                   return 0;
               }
               s.push(arr[i]);
           } else{
               while(!s.empty() && s.top()<arr[i]){
                   parent=s.top();
                   s.pop();
               }
               s.push(arr[i]);
           }
       }
    return 1;
}