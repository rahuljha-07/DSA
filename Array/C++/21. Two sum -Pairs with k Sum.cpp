 int getPairsCount(int arr[], int n, int k) {
        // code here
        int c=0;
        unordered_map<int,int> m;
    for(int i=0;i<n;i++){
        if(m.find(k-arr[i])!=m.end())  c+=m[k-arr[i]]; 
        m[arr[i]]++;
        }
    return c;
    }