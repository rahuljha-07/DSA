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
