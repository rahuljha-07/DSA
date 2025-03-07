#define MOD 1000000007

// Function to convert the linked list to an integer
long long linkedListToNumber(Node* head) {
    long long num = 0;
    
    while (head != NULL) {
        num = (num * 10 + head->data) % MOD;  // Build the number and take modulo to avoid overflow
        head = head->next;
    }
    
    return num;
}

// Function to multiply two linked lists
long long multiplyTwoLists(Node* L1, Node* L2) {
    // Convert both linked lists to numbers
    long long num1 = linkedListToNumber(L1);
    long long num2 = linkedListToNumber(L2);
    
    // Multiply the numbers and take modulo
    long long result = (num1 * num2) % MOD;
    
    return result;
}

// creating a linklist
#include <iostream>
#include <vector>

#define MOD 1000000007

using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

// Reverse the linked list
Node* reverse(Node *head) {
    Node *prev = nullptr, *curr = head, *next = nullptr;
    while (curr != nullptr) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

// Function to add two numbers represented by linked lists
Node* addLists(Node* l1, Node* l2) {
    Node* dummy = new Node(0);
    Node* temp = dummy;
    int carry = 0;

    while (l1 || l2 || carry) {
        int sum = carry + (l1 ? l1->data : 0) + (l2 ? l2->data : 0);
        carry = sum / 10;
        temp->next = new Node(sum % 10);
        temp = temp->next;

        if (l1) l1 = l1->next;
        if (l2) l2 = l2->next;
    }

    return dummy->next;
}

// Function to multiply two linked lists
Node* multiplyTwoLists(Node* L1, Node* L2) {
    if (!L1 || !L2) return nullptr;

    // Reverse both lists to make multiplication easier
    L1 = reverse(L1);
    L2 = reverse(L2);

    Node* result = nullptr;
    Node* tempResult = nullptr;
    Node* tempL1 = L1;

    int positionShift = 0;

    // Multiply each digit of L1 with entire L2
    while (tempL1) {
        Node* tempL2 = L2;
        Node* temp = new Node(0); // Dummy node for intermediate sum
        Node* current = temp;
        
        // Add position shift (multiply by 10)
        for (int i = 0; i < positionShift; i++) {
            current->next = new Node(0);
            current = current->next;
        }

        int carry = 0;
        while (tempL2) {
            int mul = tempL1->data * tempL2->data + carry;
            carry = mul / 10;
            current->next = new Node(mul % 10);
            current = current->next;
            tempL2 = tempL2->next;
        }

        if (carry) {
            current->next = new Node(carry);
        }

        // Add intermediate result to final result
        result = addLists(result, temp->next);

        positionShift++;
        tempL1 = tempL1->next;
    }

    // Reverse the result list to correct the order
    return reverse(result);
}

// Function to print the linked list
void printList(Node* head) {
    while (head != nullptr) {
        cout << head->data;
        head = head->next;
    }
    cout << endl;
}

// Helper function to create a linked list from a number
Node* createList(int num) {
    Node* head = nullptr;
    Node* tail = nullptr;
    while (num > 0) {
        int digit = num % 10;
        Node* newNode = new Node(digit);
        if (head == nullptr) {
            head = tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
        num /= 10;
    }
    return head;
}

int main() {
    int num1 = 329, num2 = 46;
    
    // Create the linked lists for the numbers
    Node* L1 = createList(num1);
    Node* L2 = createList(num2);
    
    // Multiply the linked lists
    Node* result = multiplyTwoLists(L1, L2);
    
    // Print the result
    printList(result);
    
    return 0;
}
/*
Problem:
L1 (Linked List 1) represents the number **329**:  
`3 -> 2 -> 9`

L2 (Linked List 2) represents the number **46**:  
`4 -> 6`

We need to multiply these two numbers and return the result in the form of a linked list. The result of **329 * 46** is **15134**.

### Steps to Multiply the Linked Lists:

1. **Reverse both linked lists**:  
   Reversing helps in processing from the least significant digit (i.e., starting from the head).

   - **L1 reversed**: `9 -> 2 -> 3`
   - **L2 reversed**: `6 -> 4`

2. **Multiply digit by digit**:  
   We multiply each digit of the reversed linked lists and store the result in the new linked list, handling the carry properly.

### Step-by-Step Multiplication:

1. **Multiply 9 (from L1) and 6 (from L2):**

   - \( 9 \times 6 = 54 \)
   - Store `54 % 10 = 4` in the result linked list, and carry `54 / 10 = 5`.
   - **Current result**: `4`, carry = `5`.

2. **Multiply 9 (from L1) and 4 (from L2):**

   - \( 9 \times 4 = 36 \)
   - Add the carry: \( 36 + 5 = 41 \)
   - Store `41 % 10 = 1` in the result linked list, and carry `41 / 10 = 4`.
   - **Current result**: `1 -> 4`, carry = `4`.

3. **Multiply 2 (from L1) and 6 (from L2):**

   - \( 2 \times 6 = 12 \)
   - Add the carry: \( 12 + 4 = 16 \)
   - Store `16 % 10 = 6` in the result linked list, and carry `16 / 10 = 1`.
   - **Current result**: `6 -> 1 -> 4`, carry = `1`.

4. **Multiply 2 (from L1) and 4 (from L2):**

   - \( 2 \times 4 = 8 \)
   - Add the carry: \( 8 + 1 = 9 \)
   - Store `9` in the result linked list.
   - **Current result**: `9 -> 6 -> 1 -> 4`, carry = `0`.

5. **Multiply 3 (from L1) and 6 (from L2):**

   - \( 3 \times 6 = 18 \)
   - Store `18` in the result linked list (there’s no carry to propagate).
   - **Current result**: `18 -> 9 -> 6 -> 1 -> 4`

### Reversing the Result:
The result linked list is in reverse order, so we reverse it to get the final result in the correct order.

- **Reversed result**: `1 -> 5 -> 1 -> 3 -> 4`

This is the final result, which is **15134**.
