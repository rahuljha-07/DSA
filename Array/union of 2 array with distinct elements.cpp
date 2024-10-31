int findUnion(vector<int>& a, vector<int>& b) {
        unordered_set<int> set;
        for(int i = 0, j = a.size()-1; i <= j; i++,j--){
            set.insert(a[i]);
            set.insert(a[j]);
        }
        for(int i = 0, j = b.size()-1; i <= j; i++,j--){
            set.insert(b[i]);
            set.insert(b[j]);
        }
        return set.size();
    }