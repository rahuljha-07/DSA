#include <iostream>
#include <vector>
#include <limits>

using namespace std;

class TwoStacks {
private:
    vector<int> arr; // Vector to hold stack elements
    int top1;        // Index for Stack 1 (front)
    int top2;        // Index for Stack 2 (back)
    static const int NULL_VALUE = std::numeric_limits<int>::min(); // A value to indicate a "null" or empty slot

public:
    // Constructor to initialize the two stacks
    TwoStacks(int size) {
        arr.resize(size, NULL_VALUE); // Initialize vector with NULL_VALUE
        top1 = -1;                     // Stack 1 starts empty
        top2 = size;                   // Stack 2 starts empty
    }

    // Push operation for Stack 1
    void pushStack1(int value) {
        if (top1 + 1 == top2) { // Check if there is no space between stacks
            cout << "Stack 1 is full, cannot push " << value << "." << endl;
            return;
        }
        arr[++top1] = value; // Increment top1 and push value
    }

    // Push operation for Stack 2
    void pushStack2(int value) {
        if (top2 - 1 == top1) { // Check if there is no space between stacks
            cout << "Stack 2 is full, cannot push " << value << "." << endl;
            return;
        }
        arr[--top2] = value; // Decrement top2 and push value
    }

    // Pop operation for Stack 1
    void popStack1() {
        if (isEmptyStack1()) { // Check if Stack 1 is empty
            cout << "Stack 1 is empty, cannot pop." << endl;
            return;
        }
        arr[top1--] = NULL_VALUE; // Pop the top element and set it to NULL_VALUE
    }

    // Pop operation for Stack 2
    void popStack2() {
        if (isEmptyStack2()) { // Check if Stack 2 is empty
            cout << "Stack 2 is empty, cannot pop." << endl;
            return;
        }
        arr[top2++] = NULL_VALUE; // Pop the top element and set it to NULL_VALUE
    }

    // Get the top element of Stack 1
    int topStack1() {
        if (isEmptyStack1()) {
            cout << "Stack 1 is empty." << endl;
            return NULL_VALUE; // or throw an exception
        }
        return arr[top1];
    }

    // Get the top element of Stack 2
    int topStack2() {
        if (isEmptyStack2()) {
            cout << "Stack 2 is empty." << endl;
            return NULL_VALUE; // or throw an exception
        }
        return arr[top2];
    }

    // Check if Stack 1 is empty
    bool isEmptyStack1() {
        return top1 < 0;
    }

    // Check if Stack 2 is empty
    bool isEmptyStack2() {
        return top2 >= arr.size();
    }
};

int main() {
    TwoStacks stacks(5); // Create two stacks with a total size of 5

    stacks.pushStack1(10);
    stacks.pushStack1(20);
    stacks.pushStack2(30);
    stacks.pushStack2(40);

    cout << "Top of Stack 1: " << stacks.topStack1() << endl; // Outputs: 20
    cout << "Top of Stack 2: " << stacks.topStack2() << endl; // Outputs: 40

    stacks.popStack1();
    cout << "Top of Stack 1 after pop: " << stacks.topStack1() << endl; // Outputs: 10

    stacks.popStack2();
    cout << "Top of Stack 2 after pop: " << stacks.topStack2() << endl; // Outputs: 30

    stacks.pushStack1(50);
    stacks.pushStack2(60); // This will show that Stack 2 is full

    stacks.pushStack1(70); // This will push normally
    stacks.pushStack1(80); // This will show that Stack 1 is full

    return 0;
}
