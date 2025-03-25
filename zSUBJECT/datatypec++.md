# **C++ Data Structures: Basic Operations, Time Complexity & Common Functions**

This cheat sheet provides an **overview of basic operations**, their **time complexity**, and **common functions** for each of the major data structures in C++. It also includes additional utility functions often used in practice.

---

## **1. Array (Fixed-Size)**
An **array** in C++ has a fixed size known at compile-time (e.g., `int arr[5]`). 

### **Operations**:
- **Insert (at end):** `O(1)`  
- **Insert (at index):** `O(n)` (since elements may need to be shifted)
- **Delete (from end):** `O(1)`
- **Delete (from index):** `O(n)` (shifting elements)
- **Access (arr[i]):** `O(1)`
- **Search:** `O(n)`

### **Common Functions**:
- **`sizeof(arr) / sizeof(arr[0])`** → Get array size.
- **`memset(arr, 0, sizeof(arr))`** → Initialize array to 0 (or any byte value).
- **`fill(arr, arr + n, value)`** → Fill array with `value` (requires `<algorithm>`).
- **`copy(src, src + n, dest)`** → Copy elements from one array to another (requires `<algorithm>`).

### **Sample Syntax**:
```cpp
#include <iostream>
#include <cstring>      // For memset
#include <algorithm>    // For fill, copy
using namespace std;

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    int size = sizeof(arr) / sizeof(arr[0]); // Get array size

    memset(arr, 0, sizeof(arr)); // Initialize array to all 0s
    arr[2] = 10; // Modify element at index 2 (O(1))

    // Fill array with a specific value
    fill(arr, arr + size, 7);

    // Print array
    for(int i = 0; i < size; i++) {
        cout << arr[i] << " "; 
    }
    cout << endl;
    return 0;
}
```

---

## **2. Vector (Dynamic Array)**
A **vector** can grow and shrink dynamically. Internally uses a contiguous array for storage.

### **Operations**:
- **Insert at end (`push_back`):** `O(1)` (amortized)
- **Insert at index (`insert`):** `O(n)` (may require shifting)
- **Delete from end (`pop_back`):** `O(1)`
- **Delete from index (`erase`):** `O(n)` (shifting)
- **Access (v[i]):** `O(1)`
- **Search:** `O(n)` (linear search)

### **Common Functions**:
- **`v.size()`** → Get the current number of elements.
- **`v.clear()`** → Remove all elements.
- **`v.resize(n, val)`** → Resize vector to `n` elements (new elements initialized to `val` if specified).
- **`v.reserve(n)`** → Pre-allocate capacity for `n` elements (avoids re-allocations).
- **`v.shrink_to_fit()`** → Reduce capacity to fit the size exactly (C++11+).
- **`v.begin() / v.end()`** → Return iterators to the beginning/end.
- **`v.back()`** → Access the last element.
- **`v.assign(count, value)`** → Assign `count` copies of `value`.
- **`v.assign(first, last)`** → Assign elements from the range `[first, last)`.

### **Sample Syntax**:
```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {1, 2, 3, 4};
    v.push_back(5);              // O(1) amortized
    v.insert(v.begin() + 2, 10); // O(n) - insert at index 2
    v.pop_back();                // O(1) - remove last element
    v.erase(v.begin() + 1);      // O(n) - erase at index 1
    
    // Reserve capacity
    v.reserve(100);

    // Resize
    v.resize(10, 0);

    // Assign new values
    v.assign(5, 99);  // Fill with five 99s

    cout << "Vector size: " << v.size() << endl;
    cout << "Last element: " << v.back() << endl;

    return 0;
}
```

---

## **3. Stack (LIFO)**
A **stack** allows insertion and removal from only one end (top).

### **Operations**:
- **Push (`push`):** `O(1)`
- **Pop (`pop`):** `O(1)`
- **Top (`top`):** `O(1)`

### **Common Functions**:
- **`s.size()`** → Current size of the stack.
- **`s.empty()`** → Check if empty.
- **`s.emplace(value)`** → Construct and insert element at top (potentially more efficient than push).

### **Sample Syntax**:
```cpp
#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> s;
    s.push(10);
    s.push(20);
    cout << s.top() << endl; // 20
    s.pop();
    cout << s.size() << endl; // 1
    cout << boolalpha << s.empty() << endl; // false
    s.emplace(30); // Emplace element at top
    cout << s.top() << endl; // 30
    return 0;
}
```

---

## **4. Queue (FIFO)**
A **queue** inserts elements at the back and removes them from the front.

### **Operations**:
- **Enqueue (`push`):** `O(1)`
- **Dequeue (`pop`):** `O(1)`
- **Front (`front`):** `O(1)`

### **Common Functions**:
- **`q.size()`** → Current size of the queue.
- **`q.empty()`** → Check if empty.
- **`q.back()`** → Access the last element.
- **`q.emplace(value)`** → Construct and enqueue element at the back.

### **Sample Syntax**:
```cpp
#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;
    q.push(10);
    q.push(20);
    cout << q.front() << endl; // 10
    q.pop();
    cout << q.size() << endl;  // 1
    q.emplace(30);             // Emplace element
    cout << q.back() << endl;  // 30
    return 0;
}
```

---

## **5. Deque (Double-Ended Queue)**
A **deque** allows insertion and removal at both the front and back in `O(1)` time (amortized).

### **Operations**:
- **Insert at front/back (`push_front`, `push_back`):** `O(1)`
- **Delete from front/back (`pop_front`, `pop_back`):** `O(1)`
- **Random access (`operator[]`, `at()`):** `O(1)` (amortized)
- **Insert at index, erase at index:** `O(n)` (may need shifting)

### **Common Functions**:
- **`dq.size()`**, **`dq.empty()`** → Check size and emptiness.
- **`dq.front()`, `dq.back()`** → Access front/back.
- **`dq.clear()`** → Remove all elements.
- **`dq.at(pos)`** → Safe access at position (throws exception on out-of-range).
- **`dq.insert(pos, value)`** → Insert at position (iterator-based).
- **`dq.erase(pos)`** → Erase element at position (iterator-based).

### **Sample Syntax**:
```cpp
#include <iostream>
#include <deque>
using namespace std;

int main() {
    deque<int> dq;
    dq.push_front(1); // O(1)
    dq.push_back(2);  // O(1)
    cout << dq.front() << endl; // 1
    dq.pop_front();   // O(1)
    dq.push_back(3);
    dq.push_back(4);

    dq.insert(dq.begin() + 1, 10); // O(n) - insert at index 1
    dq.erase(dq.begin());          // O(n) - erase at index 0
    
    cout << "dq.front(): " << dq.front() << endl;
    cout << "dq.back(): "  << dq.back()  << endl;
    cout << "dq[0]: "      << dq[0]      << endl;
    return 0;
}
```

---

## **6. List (Doubly Linked List)**
A **list** is a doubly linked list. Insertions and deletions with an iterator at a known position are `O(1)`.

### **Operations**:
- **Insert/Delete at front/back:** `O(1)`
- **Insert/Delete at middle (with iterator):** `O(1)`
- **Insert/Delete without iterator (need search):** `O(n)`
- **Access (no direct `operator[]`):** `O(n)` (must traverse)
- **Search:** `O(n)`

### **Common Functions**:
- **`lst.size()`**, **`lst.empty()`** → Check size and emptiness.
- **`lst.clear()`** → Remove all elements.
- **`lst.push_front(value)`, `lst.push_back(value)`** → Insert at front/back.
- **`lst.pop_front()`, `lst.pop_back()`** → Remove from front/back.
- **`lst.emplace_front(value)`, `lst.emplace_back(value)`, `lst.emplace(pos, value)`** → Construct in-place.
- **`lst.reverse()`** → Reverse the list.
- **`lst.sort()`** → Sort the list (in ascending order by default).
- **`lst.splice(pos, other_list, it)`** → Transfer element `it` from `other_list` to `lst` at `pos`.
- **`lst.remove(value)`, `lst.remove_if(pred)`** → Remove elements by value or condition.
- **`lst.unique()`** → Remove consecutive duplicates.
- **`lst.merge(other_list)`** → Merge two sorted lists.

### **Sample Syntax**:
```cpp
#include <iostream>
#include <list>
using namespace std;

int main() {
    list<int> lst = {1, 2, 3};
    lst.push_front(0);   // O(1)
    lst.push_back(4);    // O(1)
    lst.reverse();       // Reverse the list

    // Emplace example
    auto it = lst.begin();
    ++it; // Move iterator to 2nd position
    lst.emplace(it, 10); // Insert 10 at that position in O(1)

    // Remove all occurrences of 2
    lst.remove(2);

    // Print list
    for (int val : lst) {
        cout << val << " ";
    }
    cout << endl;
    return 0;
}
```

---

## **7. Priority Queue (Heap-based)**
A **priority queue** always gives access to the largest (or smallest if using a custom comparator) element in `O(1)` time.

### **Operations**:
- **Insert (`push`):** `O(log n)`
- **Remove top (`pop`):** `O(log n)`
- **Get top (`top`):** `O(1)`

### **Common Functions**:
- **`pq.size()`**, **`pq.empty()`** → Current size / emptiness.
- **`pq.top()`** → Returns the top (max or min depending on comparator).
- **`pq.emplace(value)`** → Construct and insert element (potentially more efficient).

### **Sample Syntax**:
```cpp
#include <iostream>
#include <queue>
using namespace std;

int main() {
    priority_queue<int> pq;
    pq.push(10);
    pq.push(5);
    pq.push(20);
    cout << pq.top() << endl; // 20
    pq.pop();                 // Remove the top element (20)
    cout << pq.top() << endl; // 10
    pq.emplace(15);           // Insert 15
    cout << pq.top() << endl; // 15
    return 0;
}
```

---

## **8. Map and Unordered Map**
### **8.1 Map (`map`)**
Implemented typically as a **red-black tree**. Keys are always sorted.

#### **Operations**:
- **Insert/Delete/Search:** `O(log n)`

#### **Common Functions**:
- **`m.size()`**, **`m.empty()`** → Size and emptiness.
- **`m.find(key)`** → Returns iterator to element or `m.end()` if not found.
- **`m.count(key)`** → Returns number of matches for `key` (0 or 1 in `map`).
- **`m.emplace(key, value)`** → Construct key-value in place if not existing.
- **`m.erase(key)`** → Erase element by key/iterator.
- **`m.lower_bound(key)`, `m.upper_bound(key)`, `m.equal_range(key)`** → Range queries based on sorted order.

#### **Sample Syntax**:
```cpp
#include <iostream>
#include <map>
using namespace std;

int main() {
    map<int, string> m;
    m[1] = "One";         // Insert
    m.emplace(2, "Two");  // Emplace
    cout << m[1] << endl; // Access

    auto it = m.find(2);
    if (it != m.end()) {
        cout << "Key 2 found with value: " << it->second << endl;
    }

    m.erase(1);           // Erase key = 1

    // lower_bound / upper_bound
    auto lb = m.lower_bound(2);
    if (lb != m.end()) {
        cout << "Lower bound of 2: " << lb->first << endl;
    }

    return 0;
}
```

### **8.2 Unordered Map (`unordered_map`)**
Implemented as a **hash table**. Order is not guaranteed.

#### **Operations**:
- **Insert/Delete/Search:** `O(1)` average case

#### **Common Functions**:
- **`um.size()`**, **`um.empty()`** → Size and emptiness.
- **`um.find(key)`**, **`um.count(key)`** → Find or count elements by key.
- **`um.emplace(key, value)`** → Construct key-value in place if not existing.
- **`um.erase(key)`** → Erase element.
- **`um.bucket_count()`**, **`um.load_factor()`** → Hash-bucket statistics.
- **`um.rehash(n)`** → Rehash the container to have at least `n` buckets.

#### **Sample Syntax**:
```cpp
#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    unordered_map<int, string> um;
    um[1] = "One";
    um.emplace(2, "Two");

    // Access and check
    if (um.find(1) != um.end()) {
        cout << "Key 1 found with value: " << um[1] << endl;
    }

    // Erase
    um.erase(2);

    // Bucket info
    cout << "Bucket count: " << um.bucket_count() << endl;
    cout << "Load factor: " << um.load_factor() << endl;

    return 0;
}
```

---

## **9. Set and Unordered Set**
### **9.1 Set (`set`)**
Implemented typically as a **red-black tree**. Elements are unique and always sorted.

#### **Operations**:
- **Insert/Delete/Search:** `O(log n)`

#### **Common Functions**:
- **`s.size()`**, **`s.empty()`** → Size and emptiness.
- **`s.insert(value)`**, **`s.erase(value)`** → Insert, erase.
- **`s.find(value)`**, **`s.count(value)`** → Find or count elements.
- **`s.lower_bound(value)`, `s.upper_bound(value)`, `s.equal_range(value)`** → Range queries based on sorted order.

#### **Sample Syntax**:
```cpp
#include <iostream>
#include <set>
using namespace std;

int main() {
    set<int> s;
    s.insert(10);
    s.insert(5);
    s.erase(10);

    if(s.find(5) != s.end()) {
        cout << "Found 5" << endl;
    }

    cout << "Count of 5: " << s.count(5) << endl;
    cout << "Set size: " << s.size() << endl;

    return 0;
}
```

### **9.2 Unordered Set (`unordered_set`)**
Implemented as a **hash table**. Elements are unique and order is not guaranteed.

#### **Operations**:
- **Insert/Delete/Search:** `O(1)` average case

#### **Common Functions**:
- **`us.size()`**, **`us.empty()`** → Size and emptiness.
- **`us.insert(value)`**, **`us.erase(value)`** → Insert, erase.
- **`us.find(value)`**, **`us.count(value)`** → Find or count elements.
- **`us.bucket_count()`**, **`us.load_factor()`** → Hash-bucket statistics.
- **`us.rehash(n)`** → Rehash to have at least `n` buckets.

#### **Sample Syntax**:
```cpp
#include <iostream>
#include <unordered_set>
using namespace std;

int main() {
    unordered_set<int> us;
    us.insert(10);
    us.insert(5);

    if(us.find(5) != us.end()) {
        cout << "Found 5" << endl;
    }

    cout << "Count of 10: " << us.count(10) << endl;
    us.erase(10);

    cout << "Bucket count: " << us.bucket_count() << endl;
    cout << "Load factor: " << us.load_factor() << endl;

    return 0;
}
```

---

## **🔥 Summary Table: Time Complexities**

| Data Structure                          | Insert / Push        | Delete / Pop        | Access        | Search      |
|----------------------------------------|-----------------------|----------------------|--------------|-------------|
| **Array** (`int arr[]`)                | `O(n)`               | `O(n)`              | `O(1)`        | `O(n)`       |
| **Vector** (`vector`)             | `O(1)*` (amortized)  | `O(n)`              | `O(1)`        | `O(n)`       |
| **Stack** (`stack`)               | `O(1)`               | `O(1)`              | `O(1)` (top)  | `O(n)`       |
| **Queue** (`queue`)               | `O(1)`               | `O(1)`              | `O(1)` (front)| `O(n)`       |
| **Deque** (`deque`)               | `O(1)`               | `O(1)`              | `O(1)`        | `O(n)`       |
| **List** (`list`)                 | `O(1)`               | `O(1)`              | `O(n)`        | `O(n)`       |
| **Priority Queue** (`priority_queue`) | `O(log n)`        | `O(log n)`          | `O(1)` (top)  | `O(n)`       |
| **Map** (`map`)                   | `O(log n)`           | `O(log n)`          | `O(log n)`    | `O(log n)`   |
| **Unordered Map** (`unordered_map`)| `O(1)` (avg)         | `O(1)` (avg)        | `O(1)`        | `O(1)` (avg) |
| **Set** (`set`)                   | `O(log n)`           | `O(log n)`          | `O(log n)`    | `O(log n)`   |
| **Unordered Set** (`unordered_set`)| `O(1)` (avg)         | `O(1)` (avg)        | `O(1)`        | `O(1)` (avg) |

> **Note:**  
> - For **Vector**, insertion at end is amortized `O(1)`, but can be `O(n)` in the worst case when reallocation happens.  
> - For **List**, insert/delete at middle is `O(1)` **only if** you already have an iterator pointing to the target position. Otherwise, finding that position costs `O(n)`.  
> - For **Map/Set** (tree-based), operations are `O(log n)`; for **Unordered Map/Set** (hash-based), operations are `O(1)` average case but can degrade to `O(n)` in the worst case.

---
