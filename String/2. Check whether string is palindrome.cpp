int isPalindrome(string S) {
    int i = 0, j = S.size() - 1;

    // Check characters from both ends
    while (i < j) {
        if (S[i] != S[j]) 
            return 0; // Not a palindrome
        i++;
        j--;
    }
    return 1; // It's a palindrome
}