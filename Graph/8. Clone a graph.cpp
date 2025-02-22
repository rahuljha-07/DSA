// Definition for a Node.
class Node {
public:
    int val;                           // Value of the node
    vector<Node*> neighbors;           // List of neighboring nodes

    Node() {                           // Default constructor
        val = 0;
        neighbors = vector<Node*>();
    }
    
    Node(int _val) {                   // Constructor with node value
        val = _val;
        neighbors = vector<Node*>();
    }
    
    Node(int _val, vector<Node*> _neighbors) {  // Constructor with value and neighbors
        val = _val;
        neighbors = _neighbors;
    }
};

//BFS
class Solution {
    public:
        Node* cloneGraph(Node* node) {
            if (node == nullptr) return nullptr;
            
            unordered_map<Node*, Node*> map;
            queue<Node*> queue;
            
            queue.push(node);
            map[node] = new Node(node->val, {});
            
            while (!queue.empty()) {
                Node* h = queue.front();
                queue.pop();
                
                for (Node* neighbor : h->neighbors) {
                    if (!map.count(neighbor)) {
                        map[neighbor] = new Node(neighbor->val, {});
                        queue.push(neighbor);
                    }
                    map[h]->neighbors.push_back(map[neighbor]);
                }
            }
            
            return map[node];
        }
    };



//DFS
class Solution {
public:
    // Helper function to perform DFS and clone the graph
    Node* dfsClone(Node* currentNode, unordered_map<Node*, Node*>& clonedNodes) {
        // Create a clone of the current node
        Node* cloneNode = new Node(currentNode->val);
        
        // Store the mapping of the current node to its clone
        clonedNodes[currentNode] = cloneNode;
        
        // Traverse all the neighbors of the current node
        for (Node* neighbor : currentNode->neighbors) {
            // If the neighbor is already cloned, add it to the current node's clone's neighbors
            if (clonedNodes.find(neighbor) != clonedNodes.end()) {
                cloneNode->neighbors.push_back(clonedNodes[neighbor]);
            } 
            // If the neighbor is not yet cloned, clone it recursively and add it
            else {
                cloneNode->neighbors.push_back(dfsClone(neighbor, clonedNodes));
            }
        }
        
        // Return the clone of the current node
        return cloneNode;
    }

    // Main function to clone the graph
    Node* cloneGraph(Node* node) {
        // Handle the edge case where the graph is empty
        if (node == nullptr) {
            return nullptr;
        }
        
        // A map to keep track of visited nodes and their clones
        unordered_map<Node*, Node*> clonedNodes;

        // Start DFS from the given node
        return dfsClone(node, clonedNodes);
    }
};
