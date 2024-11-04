// Function to find if there is a celebrity in the party or not
// A celebrity is defined as someone who is known by everyone but knows no one else
int celebrity(vector<vector<int>>& M, int n) {
    stack<int> s;

    // Push all people onto the stack
    for (int i = 0; i < n; i++) {
        s.push(i);
    }

    // Narrow down to one potential celebrity
    while (s.size() >= 2) {
        int a = s.top();  // Get the top person 'a' from the stack
        s.pop();
        int b = s.top();  // Get the next top person 'b' from the stack
        s.pop();

        // If person 'a' knows person 'b', 'a' cannot be a celebrity
        if (M[a][b] == 1) {
            s.push(b);
        }
        // If person 'a' does not know person 'b', 'b' cannot be a celebrity
        else {
            s.push(a);
        }
    }

    // Potential candidate for celebrity
    int potential = s.top();
    s.pop();

    // Verify if the potential candidate is a real celebrity
    for (int i = 0; i < n; i++) {
        if (potential != i) { // Skip self-check for potential
            // Check if the potential celebrity knows anyone or if not everyone knows them
            if (M[potential][i] != 0 || M[i][potential] != 1) {
                return -1; // Not a celebrity
            }
        }
    }

    return potential; // Return the index of the celebrity
}
