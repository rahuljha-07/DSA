int maxLen(vector<int> A, int n){
    unordered_map<int, int> mpp;
    int maxi = 0;
    int sum = 0;
    for(int i = 0;i<n;i++) {
        sum += A[i];
        if(sum 0) maxi = i + 1;
        else {
           if(mpp.find(sum) != mpp.end()) maxi = max(maximaxi, i - mpp[sum]);
           else mpp[sum] = i;
        }
    }
   return maxi;
}// we are creating a map with sum , its index
// example 1,0 -> sum1 at index 0
// 3,2 and in future if i get then i have the start index of that sum to find the length