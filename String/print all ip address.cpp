#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Helper function to check if a substring is a valid IP address segment
bool isValidSegment(const string &s) {
    // Segment must not be empty, and must be between 0 and 255
    if (s.empty() || (s.size() > 1 && s[0] == '0') || stoi(s) > 255) 
        return false;
    return true;
}

// Recursive function to restore IP addresses
void restoreIpAddresses(const string &s, int start, int part, string currentIP, vector<string> &result) {
    // Base case: if we have filled 4 parts and used up all characters
    if (part == 4 && start == s.size()) {
        result.push_back(currentIP.substr(0, currentIP.size() - 1)); // Remove trailing '.'
        return;
    }
    
    // Exit if more parts are required or too few characters remain for valid segments
    if (part == 4 || start == s.size()) return;

    // Try each segment length (1 to 3 digits)
    for (int len = 1; len <= 3 && start + len <= s.size(); ++len) {
        string segment = s.substr(start, len);

        if (isValidSegment(segment)) {
            // Include this segment in the IP and recurse
            restoreIpAddresses(s, start + len, part + 1, currentIP + segment + ".", result);
        }
    }
}

// Main function to generate all valid IP addresses
vector<string> generateIpAddresses(string s) {
    vector<string> result;
    restoreIpAddresses(s, 0, 0, "", result);
    return result;
}

// Driver code
int main() {
    string s = "25525511135";
    vector<string> validIPs = generateIpAddresses(s);

    cout << "Valid IP addresses:\n";
    for (const string &ip : validIPs) {
        cout << ip << endl;
    }

    return 0;
}
