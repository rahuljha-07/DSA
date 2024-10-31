int findMinOps(vector<int> arr) {
    int ans = 0, n=arr.size();
    for (int i=0,j=n-1; i<=j;){
        if (arr[i] == arr[j]){
            i++;
            j--;
        } else if (arr[i] > arr[j]){
            j--;
            arr[j] += arr[j+1] ;
            ans++;
        } else{
            i++;
            arr[i] += arr[i-1];
            ans++;
        }
    }
    return ans;
}            