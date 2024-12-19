vector<int> commonElements(const vector<int>& A, const vector<int>& B, const vector<int>& C) {
    unordered_set<int> temp; // Set to hold common elements
    vector<int> result; // Vector to hold the final result
    int i = 0, j = 0, k = 0;
    int n1=A.size(), n2=B.size(), n3=C.size();
    while (i < n1 && j < n2 && k < n3) {
        if (A[i] == B[j] && B[j] == C[k]) {
            temp.insert(A[i]); // Add the common element to the set
            i++;
            j++;
            k++;
        } else {
             // Determine the smallest of the three elements
            if (A[i] <= B[j] && A[i] <= C[k])      i++; // Increment pointer for A
            else if (B[j] <= A[i] && B[j] <= C[k]) j++; // Increment pointer for B
            else                                   k++; // Increment pointer for C
        }
        }
    }

    // Copy the unique common elements from the set to the result vector
    for (const auto& elem : temp) {
        result.push_back(elem);
    }

    // Sort the result vector before returning (optional, depending on requirements)
    sort(result.begin(), result.end());

    return result;
}