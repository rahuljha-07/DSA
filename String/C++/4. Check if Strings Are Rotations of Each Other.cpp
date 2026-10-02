bool areRotations(string s1,string s2){
	if(s1.size()!=s2.size())  return false;
	
    string concat = s1+s1;
	int ind = concat.find(s2);
	if(ind==-1) return false;
	return true;
}
// kmp algorithm

// Build the prefix table (LPS array) for the pattern
vector<int> buildPrefixTable(const string& pattern) {
    int n = pattern.size();
    vector<int> lps(n, 0);
    int len = 0;

    for (int i = 1; i < n; i++) {
        while (len > 0 && pattern[i] != pattern[len]) {
            len = lps[len - 1];
        }
        if (pattern[i] == pattern[len]) {
            len++;
        }
        lps[i] = len;
    }
    return lps;
}

// KMP search to find if pattern exists in text
bool kmpSearch(const string& text, const string& pattern) {
    vector<int> lps = buildPrefixTable(pattern);
    int j = 0; // for pattern

    for (int i = 0; i < text.size(); i++) {
        while (j > 0 && text[i] != pattern[j]) {
            j = lps[j - 1];
        }
        if (text[i] == pattern[j]) {
            j++;
        }
        if (j == pattern.size()) {
            return true; // Found
        }
    }
    return false; // Not found
}

// Function to check if s2 is a rotation of s1 using KMP
bool areRotations(string s1, string s2) {
    if (s1.size() != s2.size()) return false;

    string concat = s1 + s1;
    return kmpSearch(concat, s2);
}

int main() {
    string s1 = "ABACD";
    string s2 = "CDABA";

    if (areRotations(s1, s2)) {
        cout << "Strings are rotations of each other.\n";
    } else {
        cout << "Strings are NOT rotations of each other.\n";
    }

    return 0;
}
