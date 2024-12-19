string isSubset(int arr1[], int arr2[], int n, int m){
    set<int> set;
    for (int i = 0; i < n; i++) set.insert(arr1[i]);
    for (int i = 0; i < m; i++) {
        if (set.find(arr2[i]) == set.end()) return "No";
    }
    return "Yes";

}