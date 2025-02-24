/*
same code like shortest common supersequence 
then same code as print LCS 
only change is in else
before going to max direction also store that value in string
now after loop is end
if i=0 then push j value unless j-- otherwise opposite
*/

// Function to print the Longest Common Supersequence (LCSupersequence)
void printLCSupersequence(string x, string y, vector<vector<int>> &t) {
    int i = x.length(); // Length of string x
    int j = y.length(); // Length of string y

    string lcsuper = ""; // To store the LCSupersequence characters

    // Backtrack from t[i][j] to t[0][0]
    while (i > 0 && j > 0) {
        if (x[i - 1] == y[j - 1]) {
            // If characters match, include it in the supersequence
            lcsuper = x[i - 1] + lcsuper;
            i--;
            j--;
        } else if (t[i - 1][j] > t[i][j - 1]) {
            // If the value above is greater, include the character from x
            lcsuper = x[i - 1] + lcsuper;
            i--;
        } else {
            // Otherwise, include the character from y
            lcsuper = y[j - 1] + lcsuper;
            j--;
        }
    }

    // If one string is exhausted, append the remaining characters of the other string
    while (i > 0) {
        lcsuper = x[i - 1] + lcsuper;
        i--;
    }
    while (j > 0) {
        lcsuper = y[j - 1] + lcsuper;
        j--;
    }

    // Print the LCSupersequence
    cout << "Longest Common Supersequence: " << lcsuper << endl;
}
