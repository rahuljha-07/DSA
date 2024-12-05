// exaclty same as subset sum partiion just check this condition
int equalPartition(int n, int arr[]){
        int sum=0;
        for(int i=0;i<n;i++) sum+=arr[i];
        if(sum%2!=0 or sum==0) return 0;
         return subset(arr,n,sum/2);
    }
  // call subset function   