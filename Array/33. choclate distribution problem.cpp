int cdp(int *a,int n,int m){
    sort(a,a+n);
    int mdiff=INT_MAX;
    for(int i=0;i+m-1<n;i++){
        int diff=a[i+m-1]-a[i];
        if(diff<mdiff) mdiff=diff;
    }
    return mdiff;
}  