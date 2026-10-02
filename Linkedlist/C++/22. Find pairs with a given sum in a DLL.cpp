#include <iostream>
#include <vector>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node* prev;
    Node(int val) : data(val), next(nullptr), prev(nullptr) {}
};

// Function to find pairs with a given sum and return them in a vector
vector<pair<int, int>> findPairsWithSum(Node* head, int target) {
    vector<pair<int, int>> result;  // Vector to store pairs

    if (!head) return result;

    // Initialize pointers for the two-pointer approach
    Node* left = head;
    Node* right = head;

    // Move `right` to the last node
    while (right->next != nullptr)
        right = right->next;

    // Two-pointer technique to find pairs
    while (left != right && left->next != right) {
        int sum = left->data + right->data;

        if (sum == target) {
            result.push_back({left->data, right->data});  // Store the pair
            left = left->next;
            right = right->prev;
        }
        else if (sum < target) {
            left = left->next;  // Move left pointer forward to increase sum
        }
        else {
            right = right->prev;  // Move right pointer backward to decrease sum
        }
    }

    return result;  // Return the vector of pairs
}

// Function to print the vector of pairs
void printPairs(const vector<pair<int, int>>& pairs) {
    for (const auto& p : pairs) {
        cout << "(" << p.first << ", " << p.second << ")" << endl;
    }
}

// Helper function to print the doubly linked list (for testing purposes)
void printList(Node* head) {
    while (head != nullptr) {
        cout << head->data << " <-> ";
        head = head->next;
    }
    cout << "NULL" << endl;
}

// Function to insert a new node at the end of the doubly linked list
void append(Node*& head, int data) {
    Node* newNode = new Node(data);
    if (!head) {
        head = newNode;
        return;
    }
    Node* temp = head;
    while (temp->next) {
        temp = temp->next;
    }
    temp->next = newNode;
    newNode->prev = temp;
}

int main() {
    // Create a doubly linked list: 1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9
    Node* head = nullptr;
    append(head, 1);
    append(head, 2);
    append(head, 4);
    append(head, 5);
    append(head, 6);
    append(head, 8);
    append(head, 9);

    int target = 7;  // Given sum

    // Find pairs with the given sum
    vector<pair<int, int>> pairs = findPairsWithSum(head, target);

    // Print the result
    cout << "Pairs with sum " << target << " are:" << endl;
    printPairs(pairs);

    return 0;
}
