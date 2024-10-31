int maxSubarraySum(vector<int>& arr) {
        int maxi = INT_MIN, sum = 0, ansStart=-1, ansEnd=-1, start=-1;
        for(int i = 0; i < arr.size(); i++) {
            if(sum==0) start=i // initialize initial index whenever the sum is 0 as we find sum in subarray
            sum += arr[i];
            if(sum> maxi){
                maxi=sum;
                ansStart=start;
                ansEnd=i;
            }
            
            if (sum < 0) sum = 0;
        }
        return maxi;
    }
    