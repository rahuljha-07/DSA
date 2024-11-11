#include <iostream>
#include <queue>
#include <vector>
using namespace std;

// Definition for singly-linked list
struct Node {
    int data;
    Node* next;
    Node(int x) : data(x), next(nullptr) {}
};

// Type alias for the pair (value, node)
typedef pair<int, Node*> p;

// Merge K Sorted Linked Lists
Node* mergeKLists(Node* arr[], int k) {
    // Priority queue to store the nodes, ordered by their values
    priority_queue<p, vector<p>, greater<p>> minHeap;

    // Step 1: Push the head of each list into the min-heap
    for (int i = 0; i < k; i++) {
        if (arr[i] != nullptr) {
            minHeap.push({arr[i]->data, arr[i]});
        }
    }

    // Dummy node to serve as the head of the result list
    Node* head = nullptr;
    Node* curr = nullptr;

    // Step 2: Pop the smallest node from the heap and push its next node into the heap
    while (!minHeap.empty()) {
        // Get the smallest node (based on value)
        p top = minHeap.top();
        minHeap.pop();
        
        Node* currNode = top.second;  // Node reference
        int currData = top.first;      // Value of the node
        
        // If the result list is empty, initialize it
        if (head == nullptr) {
            head = currNode;
            curr = head;
        } else {
            // Append the smallest node to the result list
            curr->next = currNode;
            curr = curr->next;
        }

        // If the smallest node has a next node, push it into the heap
        if (currNode->next != nullptr) {
            Node* nextNode = currNode->next;
            minHeap.push({nextNode->data, nextNode});
        }
    }

    // Step 3: Return the head of the merged linked list
    return head;
}

// Helper function to print the linked list
void printList(Node* head) {
    while (head != nullptr) {
        cout << head->data << " ";
        head = head->next;
    }
    cout << endl;
}

int main() {
    // Create the input linked lists
    Node* list1 = new Node(1);
    list1->next = new Node(2);
    list1->next->next = new Node(3);
    
    Node* list2 = new Node(4);
    list2->next = new Node(5);
    
    Node* list3 = new Node(5);
    list3->next = new Node(6);
    
    Node* list4 = new Node(7);
    list4->next = new Node(8);
    
    // Store the lists in an array
    Node* arr[] = {list1, list2, list3, list4};
    
    // Merge the k sorted linked lists
    Node* mergedList = mergeKLists(arr, 4);
    
    // Print the merged linked list
    printList(mergedList);
    
    return 0;
}

// merge in pair of 2 and then reutrn 
 Node* mergesort(Node* first,Node* second){
    Node* third=NULL;
    Node* last=NULL;
    if(first->data <second->data){
        third=last=first;
        first=first->next;
        last->next=NULL;
    }
    else{
        third=last=second;
        second=second->next;
        last->next=NULL;
    }
    while(first!=NULL and second!=NULL){
        if(first->data < second->data){
            last->next=first;
            last=first;
            first=first->next;
            last->next=NULL;
        }
        else{
            last->next=second;
            last=second;
            second=second->next;
            last->next=NULL;
        }
    }
    if(first!=NULL) last->next=first;
    else last->next=second;
    return third;
}
    //Function to merge K sorted linked list.
    Node * mergeKLists(Node *arr[], int k){
        int last=k-1;
        while(last!=0){
          int  i=0;
          int  j=last;
            while(i<j){
                arr[i]=mergesort(arr[i],arr[j]);
                i++;
                j--;
                if(i>=j) last=j;
            }
        }
        return arr[0];
    }