#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class NStacksInVector {
private:
    vector<int> vec;  // Fixed-size vector to store stack values
    vector<int> free_indices;  // Vector of free indices to reuse
    unordered_map<int, vector<int>> stack_map;  // Map each stack to its indices in the vector

public:
    // Constructor initializes the vector and free_indices
    NStacksInVector(int size) {
        vec.resize(size, -1);  // Resize the vector to the specified size, initialize with -1
        for (int i = 0; i < size; ++i) {
            free_indices.push_back(i);  // Add each index to the vector of free indices
        }
    }

    // Push a value onto the specified stack
    void push(int stack_num, int value) {
        if (free_indices.empty()) {
            cout << "Stack Overflow\n";
            return;
        }

        // Reuse an index from the back of free_indices
        int index = free_indices.back();  // Get the last index
        free_indices.pop_back();  // Remove the last index

        vec[index] = value;  // Store the value in the vector

        // Add the index to the map for the specified stack
        stack_map[stack_num].push_back(index);
    }

    // Pop a value from the specified stack
    int pop(int stack_num) {
        if (stack_map.find(stack_num) == stack_map.end() || stack_map[stack_num].empty()) {
            cout << "Stack Underflow\n";
            return -1;
        }

        // Get the last index for this stack
        int top_index = stack_map[stack_num].back();
        stack_map[stack_num].pop_back();

        // Retrieve the value at this index
        int value = vec[top_index];
        vec[top_index] = -1;  // Optional: reset the value

        // Mark this index as free for future pushes
        free_indices.push_back(top_index);

        return value;
    }

    // Get the top value of the specified stack
    int top(int stack_num) {
        if (stack_map.find(stack_num) == stack_map.end() || stack_map[stack_num].empty()) {
            cout << "Stack is Empty\n";
            return -1;
        }

        // Get the last index for this stack
        int top_index = stack_map[stack_num].back();
        return vec[top_index];
    }
};

// Example usage
int main() {
    NStacksInVector stacks(10);  // Create an instance with a fixed-size vector of 10

    stacks.push(1, 10);            // Push 10 to stack 1
    stacks.push(2, 20);            // Push 20 to stack 2
    stacks.push(1, 15);            // Push 15 to stack 1

    cout << "Top of stack 1: " << stacks.top(1) << endl;  // Should output 15
    cout << "Popped from stack 1: " << stacks.pop(1) << endl;  // Should output 15
    cout << "Top of stack 1: " << stacks.top(1) << endl;  // Should output 10
    cout << "Popped from stack 2: " << stacks.pop(2) << endl;  // Should output 20
    cout << "Popped from stack 2: " << stacks.pop(2) << endl;  // Should show "Stack Underflow"

    return 0;
}
