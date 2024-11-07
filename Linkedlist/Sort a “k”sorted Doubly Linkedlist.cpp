// Function to sort a nearly sorted doubly linked list
Node* sortNearlySortedDLL(Node* head, int k) {
    if (!head) return nullptr;

    // Min-heap to store the nodes by data values
    priority_queue<int, vector<int>, greater<int>> minHeap;
    Node* newHead = nullptr;
    Node* lastSorted = nullptr;

    Node* curr = head;
    
    // Traverse the list and maintain the min-heap with a max size of `k+1`
    while (curr) {
        minHeap.push(curr->data);

        // If heap size exceeds `k`, pop the minimum element and add it to the sorted list
        if (minHeap.size() > k) {
            int minData = minHeap.top();
            minHeap.pop();

            // Create new node and add to sorted list
            Node* newNode = new Node(minData);
            if (!newHead) {
                newHead = newNode;
                lastSorted = newHead;
            } else {
                lastSorted->next = newNode;
                newNode->prev = lastSorted;
                lastSorted = newNode;
            }
        }
        
        curr = curr->next;
    }

    // Empty the remaining elements in the heap
    while (!minHeap.empty()) {
        int minData = minHeap.top();
        minHeap.pop();

        // Create new node and add to sorted list
        Node* newNode = new Node(minData);
        if (!newHead) {
            newHead = newNode;
            lastSorted = newHead;
        } else {
            lastSorted->next = newNode;
            newNode->prev = lastSorted;
            lastSorted = newNode;
        }
    }

    return newHead;
}