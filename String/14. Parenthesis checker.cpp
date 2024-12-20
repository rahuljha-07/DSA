#include <stack>
#include <string>
using namespace std;

// Function to check if brackets are balanced
bool ispar(string x) {
    stack<char> s;

    for (int i = 0; i < x.size(); i++) {
        char ch = x[i];

        // If the character is an opening bracket, push it onto the stack
        if (ch == '(' || ch == '{' || ch == '[') {
            s.push(ch);
        } else {
            // If the stack is empty and a closing bracket is found, it's unbalanced
            if (s.empty()) {
                return false;
            }

            // Check for matching pairs
            char top = s.top();
            if ((ch == ')' && top != '(') ||
                (ch == '}' && top != '{') ||
                (ch == ']' && top != '[')) {
                return false;
            }

            // Pop the matched opening bracket
            s.pop();
        }
    }

    // If the stack is empty, all brackets are balanced
    return s.empty();
}
