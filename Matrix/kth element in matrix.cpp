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