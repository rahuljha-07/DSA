void reverseString(vector<char>& s) {
    int n = s.size();
    int left = 0;
    int right = n - 1;

    // Loop to swap characters from start and end
    while (left < right) {
        swap(s[left], s[right]);
        left++;
        right--;
    }
}