string longestCommonPrefix(vector<string>& v) {
    string ans = "";  // Variable to store the longest common prefix
    sort(v.begin(), v.end());  // Sort the vector of strings

    int n = v.size();  // Get the number of strings in the vector
    string first = v[0];  // The first string in the sorted order
    string last = v[n - 1];  // The last string in the sorted order

    // Compare characters of the first and last string to find the common prefix
    for (int i = 0; i < min(first.size(), last.size()); i++) {
        if (first[i] != last[i]) {
            return ans;  // Return the common prefix found so far if characters differ
        }
        ans += first[i];  // Append the matching character to ans
    }
    return ans;  // Return the longest common prefix
}