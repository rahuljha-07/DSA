#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <string>

using namespace std;

int runCustomerSimulation(int n, const string &seq) {
    unordered_map<char, bool> inUse; // whether customer has a computer
    unordered_set<char> inCafe;      // who is currently in the cafe
    int occupied = 0, result = 0;

    for (char customer : seq) {
        if (inCafe.find(customer) == inCafe.end()) {
            // Customer arrives
            inCafe.insert(customer);
            if (occupied < n) {
                inUse[customer] = true; // got a computer
                occupied++;
            } else {
                inUse[customer] = false; // couldn't get a computer
            }
        } else {
            // Customer leaves
            if (inUse[customer]) {
                occupied--; // free the computer
            } else {
                result++; // they never got a computer
            }
            inCafe.erase(customer);
            inUse.erase(customer);
        }
    }

    return result;
}

// Example usage
int main() {
    cout << runCustomerSimulation(2, "ABBAJJKZKZ") << endl;    // Output: 0
    cout << runCustomerSimulation(3, "GACCBDDBAGEE") << endl;  // Output: 1
    cout << runCustomerSimulation(3, "GACCBGDDBAEE") << endl;  // Output: 0
    cout << runCustomerSimulation(1, "ABCBCA") << endl;        // Output: 2
    cout << runCustomerSimulation(1, "ABCBCADEED") << endl;    // Output: 3
    return 0;
}
