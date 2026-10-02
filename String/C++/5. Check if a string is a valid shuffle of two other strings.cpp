#include <iostream>
#include <string>
using namespace std;

bool isValidShuffle(string s1, string s2, string shuffled) {
    // Check if the lengths match
    if (shuffled.length() != s1.length() + s2.length()) {
        return false;
    }

    // Pointers for s1 and s2
    int i = 0, j = 0;

    // Iterate through each character in the shuffled string
    for (char c : shuffled) {
        // Check if the character can come from s1
        if (i < s1.length() && c == s1[i]) {
            i++;
        }
        // Check if the character can come from s2
        else if (j < s2.length() && c == s2[j]) {
            j++;
        } 
        // If the character does not match either, it's not a valid shuffle
        else {
            return false;
        }
    }

    // Check if we have exhausted both strings
    return (i == s1.length() && j == s2.length());
}

int main() {
    string s1 = "abc";
    string s2 = "123";
    string shuffled = "a1b2c3"; // Example of a valid shuffle

    if (isValidShuffle(s1, s2, shuffled)) {
        cout << "The string is a valid shuffle of the two strings." << endl;
    } else {
        cout << "The string is not a valid shuffle of the two strings." << endl;
    }

    return 0;
}
