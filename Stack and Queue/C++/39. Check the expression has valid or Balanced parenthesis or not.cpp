// Function to check if the brackets in a given string are balanced
bool ispar(string x) {
    // Stack to keep track of opening brackets
    stack<char> s;

    // Loop through each character in the string
    for (int i = 0; i < x.size(); i++) {
        // If the character is an opening bracket, push it onto the stack
        if (x[i] == '(' || x[i] == '{' || x[i] == '[') {
            s.push(x[i]);
        }
        // If the character is a closing bracket
        else {
            // If the stack is empty, there's no matching opening bracket
            if (s.empty()) {
                return false;
            }

            // Get the top element of the stack (the most recent opening bracket)
            char c = s.top();

            // Check if the closing bracket matches the top opening bracket
            if ((x[i] == ')' && c != '(') ||
                (x[i] == '}' && c != '{') ||
                (x[i] == ']' && c != '[')) {
                return false; // Mismatch found
            }

            // Pop the matching opening bracket from the stack
            s.pop();
        }
    }

    // If the stack is empty, all brackets were balanced; otherwise, return false
    return s.empty();
}
