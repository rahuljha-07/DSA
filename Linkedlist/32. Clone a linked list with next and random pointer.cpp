// Define the Node structure with data, next, and random (arb) pointers
struct Node {
    int data;            // Data of the node
    Node* next;          // Pointer to the next node in the list
    Node* random;        // Random pointer (arb) pointing to any node in the list

    // Constructor to initialize the node
    Node(int val) : data(val), next(nullptr), random(nullptr) {}
};

// Function to clone a linked list with next and random pointers
Node* cloneList(Node* head) {
    // If the list is empty, return nullptr
    if (head == nullptr) return nullptr;

    // Step 1: Create a cloned linked list with data and next pointers, but random pointers are null
    Node* cloneHead = nullptr;   // Head of the cloned list
    Node* cloneCurr = nullptr;   // Current pointer for the cloned list
    Node* curr = head;           // Current pointer for the original list

    // Create the cloned list (copying nodes with data and null random pointers)
    while (curr) {
        Node* newNode = new Node(curr->data);  // Create a new node for the cloned list
        if (cloneHead == nullptr) {
            cloneHead = cloneCurr = newNode;  // Initialize the cloned list head
        } else {
            cloneCurr->next = newNode;  // Append to the cloned list
            cloneCurr->next;        // Move the clone pointer
        }
        curr = curr->next;  // Move to the next node in the original list
    }

    // Step 2: Set the next and random pointers of the cloned list
    curr = head;           // Reset the current pointer to the head of the original list
    cloneCurr = cloneHead;  // Reset the cloned current pointer to the head of the cloned list

    while (curr) {
        Node* temp = curr->next;     // Store the address of the next node in the original list
        curr->next = cloneCurr;      // Point the original node's next to the cloned node
        cloneCurr->random = curr;    // Point the cloned node's random to the original node
        curr = temp;                 // Move to the next node in the original list
        cloneCurr = cloneCurr->next; // Move to the next node in the cloned list
    }

    // Step 3: Fix the random pointers of the cloned list
    curr = head;           // Reset to the head of the original list
    cloneCurr = cloneHead;  // Reset to the head of the cloned list

    while (cloneCurr) {
         // Update the cloned node's random pointer to point to the correct cloned node
        cloneCurr->random = (cloneCurr->random->random) ? cloneCurr->random->random->next : nullptr;
        cloneCurr = cloneCurr->next; // Move to the next node in the cloned list
    }

    return cloneHead;  // Return the head of the cloned list
}
