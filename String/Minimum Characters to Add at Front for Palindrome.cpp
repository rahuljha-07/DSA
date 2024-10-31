int minInsertionsToMakePalindrome(const string &str) {
    // Reverse the input string
    string rev = str;
    reverse(rev.begin(), rev.end());

    // Calculate the length of the original string
    int len = str.length();

    // Call the LCS function (assumed to be defined elsewhere)
    int lcsLength = LCS(str, rev); // calling the LPS actually in LPS we reverse the 2nd string and everything is same as LCS

    // Calculate the number of insertions needed
    int numInsertions = len - lcsLength;

    return numInsertions;
}
