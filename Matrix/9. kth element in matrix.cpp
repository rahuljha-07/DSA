int kthSmallest(int A[MAX][MAX], int n, int k)
{
  //Your code here
  int m=n;
      int mini = A[0][0] , maxi= A[n-1][m-1];
         
         int desired_element =k;
         while(mini <maxi){
             int mid = mini +(maxi - mini) /2;
             int count =0;
             for(int i=0;i<n;i++) count+= upper_bound(A[i], A[i]+m, mid) - A[i];
             if(count< desired_element) mini = mid+ 1;
             else maxi = mid;
         }
        return mini;
}
// same as median in a sorted array replace desired element with k

#include <vector>
#include <queue>
#include <tuple> // For using std::tuple
using namespace std;

int kthsmallest(vector<vector<int>>& mat, int N, int K) {
    // Min-heap to store tuples of the form {value, row, col}
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> minHeap;

    // Push the first element of each row into the heap
    for (int i = 0; i < N; i++) {
        minHeap.push(make_tuple(mat[i][0], i, 0)); // {value, row, col}
    }

    int count = 0; // Counter for extracted elements
    int result = -1;

    while (!minHeap.empty()) {
        // Extract the smallest element from the heap
        auto [val, row, col] = minHeap.top(); // Decompose the tuple
        minHeap.pop();

        result = val; // Store the current smallest value
        count++;

        if (count == K) {
            break; // Stop when we find the K-th smallest element
        }

        // If there is a next element in the same row, push it into the heap
        if (col + 1 < N) {
            minHeap.push(make_tuple(mat[row][col + 1], row, col + 1));
        }
    }

    return result;
}
