int sb(int arr[], int n, int x){
        int i=0;
        int j=0;
        int sum=0;
        int sz=INT_MAX;
        while(j<n){
            while(sum<=x and j<n){
                sum+=arr[j];
                j++;
            }
            while(sum>x and i<n){
                sz=min(sz,j-i);
                sum-=arr[i];
                i++;
            }
            
        }
        return sz;
    }