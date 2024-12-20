#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int runCustomerSimulation(int n, const string &seq) {
    unordered_map<char, bool> customerStatus; // Tracks if a customer is using a computer
    int occupied = 0; // Tracks the number of computers currently in use
    int result = 0;   // Tracks customers who couldn't get a computer

    for (char customer : seq) {
        if (customerStatus.find(customer) == customerStatus.end()) {
            // Customer arrives for the first time
            if (occupied < n) {
                // Assign a computer
                customerStatus[customer] = true;
                occupied++;
            } else {
                // No computers available
                customerStatus[customer] = false;
                result++;
            }
        } else {
            // Customer is departing
            if (customerStatus[customer]) {
                // Free up the computer
                occupied--;
            }
            customerStatus.erase(customer); // Remove the customer record
        }
    }

    return result; // Return the count of customers who couldn't get a computer
}

// Example usage
int main() {
    cout << runCustomerSimulation(2, "ABBAJJKZKZ") << endl; // Output: 0
    cout << runCustomerSimulation(3, "GACCBDDBAGEE") << endl; // Output: 1
    cout << runCustomerSimulation(3, "GACCBGDDBAEE") << endl; // Output: 0
    cout << runCustomerSimulation(1, "ABCBCA") << endl; // Output: 2
    cout << runCustomerSimulation(1, "ABCBCADEED") << endl; // Output: 3

    return 0;
}
