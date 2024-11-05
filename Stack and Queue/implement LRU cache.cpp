#include <iostream>
#include <unordered_map>
#include <list>
using namespace std;

class LRUCache {
private:
    int capacity;  // Maximum size of the cache
    list<int> keys;  // List to store keys in the order of their usage (LRU at front, MRU at back)
    unordered_map<int, int> values;  // Map to store key-value pairs

public:
    LRUCache(int cap) : capacity(cap) {}

    int get(int key) {
        // Check if the key exists in the cache
        if (values.find(key) == values.end()) {
            return -1;  // Key is not in cache
        }

        // Move the accessed key to the back of the list to mark it as most recently used
        keys.remove(key);
        keys.push_back(key);

        return values[key];  // Return the value associated with the key
    }

    void set(int key, int value) {
        // If the key is already in cache, remove it from the current position in the list
        if (values.find(key) != values.end()) {
            keys.remove(key);
        } 
        else if (keys.size() == capacity) {
            // Cache is full; remove the least recently used item (front of the list)
            int leastRecentKey = keys.front();
            keys.pop_front();  // Remove the LRU key from the list
            values.erase(leastRecentKey);  // Remove the LRU key from the map
        }

        // Insert the key at the back of the list (most recent position)
        keys.push_back(key);
        // Update the map with the new key-value pair
        values[key] = value;
    }
};

// Example usage
int main() {
    LRUCache cache(2);  // Create an LRU cache with capacity 2

    cache.set(1, 1);
    cache.set(2, 2);
    cout << "Get 1: " << cache.get(1) << endl;  // Outputs 1

    cache.set(3, 3);  // Evicts key 2
    cout << "Get 2: " << cache.get(2) << endl;  // Outputs -1, as key 2 was evicted

    cache.set(4, 4);  // Evicts key 1
    cout << "Get 1: " << cache.get(1) << endl;  // Outputs -1, as key 1 was evicted
    cout << "Get 3: " << cache.get(3) << endl;  // Outputs 3
    cout << "Get 4: " << cache.get(4) << endl;  // Outputs 4

    return 0;
}
