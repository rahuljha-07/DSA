#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> rabinKarp(string text, string pattern) {
    int n = text.size();
    int m = pattern.size();
    int prime = 101;  // A prime number for hashing
    int base = 256;   // The base for ASCII characters

    int patternHash = 0;  // Hash value for the pattern
    int windowHash = 0;   // Hash value for the current window in the text
    int h = 1;            // The value of base^(m-1) % prime

    // Result vector to store the starting indices of matched patterns
    vector<int> result;

    // Pre-compute base^(m-1) % prime
    for (int i = 0; i < m - 1; i++)
        h = (h * base) % prime;

    // Compute the hash value of the pattern and the first window of the text
    for (int i = 0; i < m; i++) {
        patternHash = (base * patternHash + pattern[i]) % prime;
        windowHash = (base * windowHash + text[i]) % prime;
    }

    // Slide the pattern over the text one character at a time
    for (int i = 0; i <= n - m; i++) {
        // Check if the current window hash matches the pattern hash
        if (patternHash == windowHash) {
            // If hash matches, check each character to avoid false positives
            bool match = true;
            for (int j = 0; j < m; j++) {
                if (text[i + j] != pattern[j]) {
                    match = false;
                    break;
                }
            }
            if (match) result.push_back(i);  // Record the starting index
        }

        // Calculate the hash of the next window
        if (i < n - m) {
            windowHash = (base * (windowHash - text[i] * h) + text[i + m]) % prime;
            if (windowHash < 0) windowHash += prime;  // Ensure non-negative hash
        }
    }

    return result;
}

int main() {
    string text = "aabacaadaba";
    string pattern = "aba";
    vector<int> indices = rabinKarp(text, pattern);

    // Output the result
    cout << "Pattern found at indices: ";
    for (int idx : indices) {
        cout << idx << " ";
    }
    cout << endl;

    return 0;
}
