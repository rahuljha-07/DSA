bool subArrayExists(int arr[], int n){
        unordered_set<int> s;
        int sum=0;
        for(int i=0;i<n;i++){
            sum+=arr[i];
            if(sum==0 or s.find(sum)!=s.end()) return true;
            s.insert(sum);
        }
        return false;
        
    }