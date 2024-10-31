#include <iostream>
#include <unordered_set>
#include <string>

using namespace std;

int runCustomerSimulation(int n, const string &seq) {
    unordered_set<char> occupied; // Set to keep track of customers using computers
    unordered_set<char> unseated; // Set to keep track of customers who could not get a computer
    int result = 0; // Counter for customers who couldn't get a computer

    for (char customer : seq) {
        // Check if customer is arriving
        if (occupied.find(customer) == occupied.end() && unseated.find(customer) == unseated.end()) {
            // Customer is trying to occupy a computer
            if (occupied.size() < n) {
                // There is an available computer
                occupied.insert(customer); // Mark the customer as using a computer
            } else {
                // No available computers
                unseated.insert(customer); // Mark the customer as unable to get a computer
                result++;
            }
        } else {
            // Customer is departing
            if (occupied.find(customer) != occupied.end()) {
                // Remove the customer from the occupied set
                occupied.erase(customer);
            }
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
