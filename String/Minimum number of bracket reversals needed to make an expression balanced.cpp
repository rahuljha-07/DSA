#include <iostream>
#include <stack>
#include <string>
using namespace std;

// Function to count the minimum number of reversals to balance a given string of brackets
int countRev(string s) {
    // If the length of the string is odd, it can't be balanced
    if (s.length() & 1) return -1;
    
    // Stack to store unmatched opening brackets
    stack<char> st;
    int unmatchedClosing = 0; // Count of unmatched closing brackets
    int unmatchedOpening = 0; // Count of unmatched opening brackets

    // Traverse each character in the string
    for (char ch : s) {
        // If it's an opening bracket, push it to the stack and increment unmatched opening count
        if (ch == '{') {
            st.push(ch);
            unmatchedOpening++;
        } 
        // If it's a closing bracket
        else if (ch == '}' && !st.empty() && st.top() == '{') {
            // If it matches with the top of the stack, pop the stack and decrement unmatched opening count
            st.pop();
            unmatchedOpening--;
        } 
        // If there's no matching opening bracket, increment unmatched closing count
        else {
            unmatchedClosing++;
        }
    }

    // Calculate the minimum reversals for unmatched closing brackets
    int reversalsForClosing = (unmatchedClosing % 2 == 0) ? (unmatchedClosing / 2) : (unmatchedClosing / 2 + 1);

    // Calculate the minimum reversals for unmatched opening brackets
    int reversalsForOpening = (unmatchedOpening % 2 == 0) ? (unmatchedOpening / 2) : (unmatchedOpening / 2 + 1);

    // Return the total reversals required
    return reversalsForClosing + reversalsForOpening;
}

// Example usage
int main() {
    string s = "{{{{}}";
    cout << "Minimum reversals needed: " << countRev(s) << endl;
    return 0;
}
