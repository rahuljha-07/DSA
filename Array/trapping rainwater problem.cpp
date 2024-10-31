int trappingWater(int arr[], int n){
        int maxleft[n];
        int maxright[n];
        
        maxleft[0]=arr[0];
        for(int i=1;i<n;i++) maxleft[i]=max(maxleft[i-1],arr[i]);
        
        maxright[n-1]=arr[n-1];
        for(int i=n-2;i>=0;i--) maxright[i]=max(maxright[i+1],arr[i]);
        
        int sum=0;
        for(int i=0;i<n;i++) sum+=min(maxleft[i],maxright[i]) - arr[i];
        return sum;
    }