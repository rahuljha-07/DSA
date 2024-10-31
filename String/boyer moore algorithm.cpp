#include <bits/stdc++.h>
using namespace std;

#define NO_OF_CHARS 256  // Total number of characters in the ASCII character set

// Preprocessing function to fill the bad character array
void badCharHeuristic(string str, int size, int badchar[NO_OF_CHARS]) {
    int i;

    // Initialize all occurrences as -1
    for (i = 0; i < NO_OF_CHARS; i++)
        badchar[i] = -1;

    // Fill the actual value of the last occurrence of each character in the pattern
    for (i = 0; i < size; i++)
        badchar[(int)str[i]] = i;
}

/* 
Pattern searching function using the Bad Character Heuristic of the Boyer-Moore Algorithm
Parameters:
- txt: The text in which to search for the pattern
- pat: The pattern to search for
*/
void search(string txt, string pat) {
    int m = pat.size();  // Length of the pattern
    int n = txt.size();  // Length of the text

    int badchar[NO_OF_CHARS];  // Array to store the last occurrence of each character in the pattern

    // Fill the bad character array by calling the preprocessing function
    badCharHeuristic(pat, m, badchar);

    int s = 0;  // s is the shift of the pattern with respect to the text
    while (s <= (n - m)) {  // While there is a valid shift
        int j = m - 1;  // Start comparing from the end of the pattern

        // Keep reducing index j while characters of pattern and text are matching
        while (j >= 0 && pat[j] == txt[s + j])
            j--;

        // If the pattern is found
        if (j < 0) {
            cout << "Pattern occurs at shift = " << s << endl;

            // Shift the pattern to align with the last occurrence of the next character in the text
            s += (s + m < n) ? m - badchar[txt[s + m]] : 1;
        } else {
            // Shift the pattern so that the bad character in the text aligns with the last occurrence in the pattern
            s += max(1, j - badchar[txt[s + j]]);
        }
    }
}

/* Driver code */
int main() {
    string txt = "ABAAABCD";  // The text to search within
    string pat = "ABC";  // The pattern to search for
    search(txt, pat);  // Call the search function
    return 0;
}

// This code is contributed by rathbhupendra
