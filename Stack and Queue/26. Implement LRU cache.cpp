#include <iostream>
#include <list>
#include <unordered_map>
using namespace std;

class LRUCache {
private:
    int capacity;  
    list<int> keys;  // Stores only keys in LRU order
    unordered_map<int, pair<int, list<int>::iterator>> cache;  // Stores key-value and iterator

public:
    // Constructor with normal initialization format
    LRUCache(int cap) {
        capacity = cap;  // Initialize the capacity inside the constructor body
    }

    // Retrieve the value associated with the key
    int get(int key) {
        if (cache.find(key) == cache.end()) {
            return -1;  // Key not found
        }
        // Move accessed key to the back (MRU position)
        keys.erase(cache[key].second);  // O(1)
        keys.push_back(key);            // O(1)
        cache[key].second = prev(keys.end());  // O(1)
        return cache[key].first;
    }

    // Insert or update the value associated with the key
    void set(int key, int value) {
        if (cache.find(key) != cache.end()) {
            keys.erase(cache[key].second);  // O(1)
        } 
        else if (keys.size() == capacity) {
            int lruKey = keys.front();  // O(1)
            keys.pop_front();            // O(1)
            cache.erase(lruKey);         // O(1)
        }
        keys.push_back(key);  // O(1)
        cache[key] = {value, prev(keys.end())};  // O(1)
    }
};

// Example usage
int main() {
    cout << "Initializing LRU Cache with capacity 2" << endl;
    LRUCache cache(2);  // Create an LRU cache with capacity 2

    cout << "Set (1, 100)" << endl;
    cache.set(1, 100);
    cout << "Set (2, 200)" << endl;
    cache.set(2, 200);

    cout << "Get (1): " << cache.get(1) << endl;  // Should return 100

    cout << "Set (3, 300)" << endl;
    cache.set(3, 300);  // Evicts key 2

    cout << "Get (2): " << cache.get(2) << endl;  // Should return -1 (not found)

    cout << "Set (4, 400)" << endl;
    cache.set(4, 400);  // Evicts key 1

    cout << "Get (1): " << cache.get(1) << endl;  // Should return -1 (not found)
    cout << "Get (3): " << cache.get(3) << endl;  // Should return 300
    cout << "Get (4): " << cache.get(4) << endl;  // Should return 400

    cout << "Set (3, 350) (Update value of key 3)" << endl;
    cache.set(3, 350);  // Update the value of key 3

    cout << "Get (3): " << cache.get(3) << endl;  // Should return 350

    cout << "Set (5, 500)" << endl;
    cache.set(5, 500);  // Evicts key 4

    cout << "Get (4): " << cache.get(4) << endl;  // Should return -1 (evicted)
    cout << "Get (5): " << cache.get(5) << endl;  // Should return 500

    return 0;
}

//  doubly linklist way
// LRU Cache (no sentinels, uses head/tail pointers)
// --------------------------------------------------
// - Doubly-linked list holds nodes in LRU -> MRU order.
//   * head = LRU (front), tail = MRU (back)
// - Hash map provides O(1) access: key -> Node*
// - get(key):  return value if present and move node to MRU
// - set(key,v): update if present (move to MRU), else insert;
//               if full, evict LRU (the head)
// - All operations are O(1).
//
// Notes:
// - Works correctly for capacity = 1 (and 0 as a no-op cache).
// - No debug/asserts; safe guards on null where helpful.
// - Copying is disabled to avoid double-frees (owning raw pointers).

#include <unordered_map>
using namespace std;

struct Node {
    int key;
    int val;
    Node* prev;
    Node* next;
    Node(int k, int v) : key(k), val(v), prev(nullptr), next(nullptr) {}
};

class LRUCache {
private:
    int capacity;                        // maximum number of entries
    unordered_map<int, Node*> cache;     // key -> node*
    Node* head;                          // LRU (front of list)
    Node* tail;                          // MRU (back of list)

    // Detach a node from its current position in the list.
    // Handles all edge cases (removing head, tail, or the only node).
    void removeNode(Node* n) {
        if (!n) return;
        if (n->prev) n->prev->next = n->next;
        else         head = n->next;         // n was head

        if (n->next) n->next->prev = n->prev;
        else         tail = n->prev;         // n was tail

        n->prev = n->next = nullptr;
    }

    // Insert node at the back of the list (node becomes MRU / tail).
    // Handles empty-list case.
    void pushBack(Node* n) {
        if (!n) return;
        n->prev = tail;
        n->next = nullptr;
        if (tail) tail->next = n;            // link old tail -> n
        else      head = n;                  // list was empty
        tail = n;
    }

    // Remove and return the current LRU node (the head).
    // Returns nullptr if the list is empty.
    Node* popFront() {
        if (!head) return nullptr;
        Node* lru = head;
        removeNode(lru);
        return lru;
    }

public:
    // Construct with a fixed capacity.
    explicit LRUCache(int cap)
        : capacity(cap), head(nullptr), tail(nullptr) {}

    // Disable copying (this class manages owning raw pointers).
    LRUCache(const LRUCache&) = delete;
    LRUCache& operator=(const LRUCache&) = delete;

    // Clean up all nodes.
    ~LRUCache() {
        Node* cur = head;
        while (cur) {
            Node* nxt = cur->next;
            delete cur;
            cur = nxt;
        }
    }

    // Get the value for 'key'.
    // - If found: move node to MRU and return value.
    // - If not found: return -1 (no changes to structure).
    int get(int key) {
        auto it = cache.find(key);
        if (it == cache.end()) return -1;

        Node* n = it->second;
        // If not already MRU, move it to the back.
        if (n != tail) {
            removeNode(n);
            pushBack(n);
        }
        return n->val;
    }

    // Insert or update (key -> value).
    // - If key exists: update value and move to MRU.
    // - If new and cache full: evict current LRU, then insert as MRU.
    // - If capacity == 0: do nothing.
    void set(int key, int value) {
        if (capacity == 0) return;

        auto it = cache.find(key);
        if (it != cache.end()) {
            // Key already present: update and move to MRU
            Node* n = it->second;
            n->val = value;
            if (n != tail) {
                removeNode(n);
                pushBack(n);
            }
            return;
        }

        // New key
        if ((int)cache.size() == capacity) {
            // Evict LRU (head)
            Node* lru = popFront();
            if (lru) {
                cache.erase(lru->key);
                delete lru;
            }
        }

        // Insert as MRU
        Node* n = new Node(key, value);
        pushBack(n);
        cache[key] = n;
    }
};
