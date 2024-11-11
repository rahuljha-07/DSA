// without trie
// Function to find unique rows in a boolean matrix
vector<vector<int>> uniqueRow(int M[MAX][MAX], int row, int col) {
    // To store the result of unique rows
    vector<vector<int>> res;

    // Set to keep track of unique rows
    set<vector<int>> s;

    // Traverse each row of the matrix
    for (int i = 0; i < row; i++) {
        // Create a vector to store the current row
        vector<int> v;

        // Push each element of the row into the vector
        for (int j = 0; j < col; j++) {
            v.push_back(M[i][j]);
        }

        // If the row is not already in the set, add it to the result and set
        if (s.find(v) == s.end()) {
            res.push_back(v);
            s.insert(v);
        }
    }

    // Return the result vector containing unique rows
    return res;
}


// with trie
class TriNode {
public:
    TriNode* children[2] = {nullptr}; // Directly initialize children array elements
    bool isEnd = false; // Directly initialize isEnd to false
};

class Trie {
public:
    TriNode* root;

    Trie() {
        root = new TriNode(); // Initialize the root node
    }

    // Insert a binary string into the Trie
    bool insert(const string& row) {
        TriNode* node = root;
        for (char c : row) {
            int index = c - '0';  // Convert character '0' or '1' to int 0 or 1
            if (node->children[index] == nullptr) {
                node->children[index] = new TriNode();
            }
            node = node->children[index];
        }

        // If the row already exists, return false
        if (node->isEnd) {
            return false;
        }

        node->isEnd = true;  // Mark the end of this row
        return true;
    }
};

void findUniqueRows(int row, int col, vector<vector<int>>& matrix) {
    Trie trie;
    vector<string> uniqueRows;  // To store the unique rows as strings

    for (int i = 0; i < row; ++i) {
        // Convert row i into a string
        string rowStr = "";
        for (int j = 0; j < col; ++j) {
            rowStr += to_string(matrix[i][j]);
        }

        // Insert the row into the Trie
        if (trie.insert(rowStr)) {
            uniqueRows.push_back(rowStr);
        }
    }

    // Output the unique rows
    for (const string& row : uniqueRows) {
        for (char c : row) {
            cout << c << " ";
        }
        cout << "$";
    }
}

int main() {
    int row = 3, col = 4;
    vector<vector<int>> matrix = {{1, 1, 0, 1}, {1, 0, 0, 1}, {1, 1, 0, 1}};

    findUniqueRows(row, col, matrix);
    return 0;
}
