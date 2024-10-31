    int findLongestConseqSubseq(int arr[], int n){
      unordered_set<int> s;
      int maxi=INT_MIN;
      int mini=INT_MAX;
      for(int i=0;i<n;i++){
          maxi=max(maxi,arr[i]);
          mini=min(mini,arr[i]);
          s.insert(arr[i]);
      }
      int count=0,ans=0;
      for(int i=mini;i<=maxi;i++){
          if(s.find(i)!=s.end()) count++;
          else{
              ans=max(ans,count);
              count=0;
          }
              
      }
       ans=max(ans,count);
      return ans;
    }