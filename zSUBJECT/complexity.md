# 📌 **C++ Data Types, Time Complexity & Data Structures**

## 🛠 **1. Choosing the Right Data Type in C++**
C++ provides different integer types to store values. Choosing the right one is important to **avoid overflow** and **optimize memory**.

### ✅ **Integer Data Types**
| Data Type | Size (bytes) | Range | Signed/Unsigned | Use Case |
|-----------|------------|----------------------|---------------|-------------|
| `int` | 4 | -2,147,483,648 to 2,147,483,647 | Signed | General use, loops, array indices |
| `unsigned int` | 4 | 0 to 4,294,967,295 | Unsigned | When negative values are not needed (e.g., counting) |
| `long` | 4 or 8 (depends on system) | Same as `int` (in 32-bit) or larger (64-bit systems) | Signed | Larger numbers in 64-bit systems |
| `unsigned long` | 4 or 8 | Positive only (double range of `long`) | Unsigned | Large positive values |
| `long long` | 8 | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 | Signed | Very large numbers (competitive programming) |
| `unsigned long long` | 8 | 0 to 18,446,744,073,709,551,615 | Unsigned | Large positive values (hashing, IDs) |
| `short` | 2 | -32,768 to 32,767 | Signed | Memory-efficient small numbers |
| `unsigned short` | 2 | 0 to 65,535 | Unsigned | Small positive numbers |
| `char` | 1 | -128 to 127 (`signed`), 0 to 255 (`unsigned`) | Signed/Unsigned | Storing characters, small numbers |

💡 **Rules of Thumb for Choosing Integers**:
- **If N ≤ 10⁹** → Use `int`
- **If N ≤ 10¹⁸** → Use `long long`
- **If only positive values are needed** → Use `unsigned int/long`
- **For very large numbers (≥ 10²⁰)** → Use `BigInteger` (not built-in in C++, use `__int128` or external libraries)

---

## 📊 **2. Time Complexity of Common C++ Data Structures**
Understanding time complexity helps you choose the best **data structure** for the problem.

### ✅ **Array (`vector<int> arr`)**
| Operation | Time Complexity |
|-----------|----------------|
| Access (`arr[i]`) | **O(1)** |
| Insert at end (`push_back()`) | **O(1)** (Amortized) |
| Insert at middle | **O(N)** |
| Delete at end (`pop_back()`) | **O(1)** |
| Delete at middle | **O(N)** |
| Search (Linear Search) | **O(N)** |
| Search (Binary Search - Sorted) | **O(log N)** |

---

### ✅ **Linked List (`list<int>` or custom `struct Node` in C++)**
| Operation | Time Complexity |
|-----------|----------------|
| Access (`list[i]`) | **O(N)** |
| Insert at front (`push_front()`) | **O(1)** |
| Insert at end (`push_back()`) | **O(1)** |
| Insert in middle | **O(N)** |
| Delete first element | **O(1)** |
| Delete last element | **O(1)** |
| Delete middle element | **O(N)** |
| Search | **O(N)** |

💡 **When to Use Linked List?**
- When **frequent insertions/deletions** are required.
- When **random access** is **not** needed (since arrays are faster for that).

---

### ✅ **Stack (`stack<int>`)**
| Operation | Time Complexity |
|-----------|----------------|
| Push (`push()`) | **O(1)** |
| Pop (`pop()`) | **O(1)** |
| Top (`top()`) | **O(1)** |
| Search | **O(N)** |

💡 **Use Stack When:**
- **LIFO (Last In, First Out)** is needed (e.g., backtracking, function calls).

---

### ✅ **Queue (`queue<int>`)**
| Operation | Time Complexity |
|-----------|----------------|
| Enqueue (`push()`) | **O(1)** |
| Dequeue (`pop()`) | **O(1)** |
| Front (`front()`) | **O(1)** |
| Search | **O(N)** |

💡 **Use Queue When:**
- **FIFO (First In, First Out)** is needed (e.g., BFS traversal).

---

### ✅ **Priority Queue (Min/Max Heap) (`priority_queue<int>`)**
| Operation | Time Complexity |
|-----------|----------------|
| Insert (`push()`) | **O(log N)** |
| Get Max/Min (`top()`) | **O(1)** |
| Delete Max/Min (`pop()`) | **O(log N)** |

💡 **Use Priority Queue When:**
- **Finding max/min efficiently** is needed (e.g., Dijkstra’s Algorithm).

---

### ✅ **Set (`set<int>`, `unordered_set<int>`)**
| Operation | `set` (Ordered) | `unordered_set` |
|-----------|---------------|----------------|
| Insert (`insert()`) | **O(log N)** | **O(1) (avg), O(N) (worst)** |
| Delete (`erase()`) | **O(log N)** | **O(1) (avg), O(N) (worst)** |
| Search (`find()`) | **O(log N)** | **O(1) (avg), O(N) (worst)** |

💡 **Use `set` When:**
- **Unique elements** are needed, and order matters.

💡 **Use `unordered_set` When:**
- **Fast lookups (O(1) avg)** are required.

---

### ✅ **Map (`map<int, int>`, `unordered_map<int, int>`)**
| Operation | `map` (Ordered) | `unordered_map` |
|-----------|---------------|----------------|
| Insert (`insert()`) | **O(log N)** | **O(1) (avg), O(N) (worst)** |
| Delete (`erase()`) | **O(log N)** | **O(1) (avg), O(N) (worst)** |
| Search (`find()`) | **O(log N)** | **O(1) (avg), O(N) (worst)** |

💡 **Use `map` When:**
- **Keys should be sorted** (e.g., leaderboard rankings).

💡 **Use `unordered_map` When:**
- **Faster access (`O(1)`) is needed**.

---

## 🚀 **3. Quick Cheatsheet for Competitive Programming**
- **Sorting**: Use `sort()` (**O(N log N)**)
- **Searching**: Use `binary_search()` (**O(log N)**)
- **Graph Traversal**:
  - BFS → **O(V + E)**
  - DFS → **O(V + E)**
- **Dynamic Programming**: 
  - Memoization → **O(N)**
  - Tabulation → **O(N)**
- **Greedy Algorithms**: Usually **O(N log N)**
- **Tree Traversals**: **O(N)**

---

## 🎯 **Final Takeaways**
- **Choose the right data type** (use `long long` for large values).
- **Understand time complexity** (avoid O(N²) for large N).
- **Use the best data structure** (maps, sets, priority queues when needed).
- **Optimize loops and avoid unnecessary memory allocation.**

---
# 🚀 **How to Determine the Required Time Complexity?**
When solving a problem, follow these steps:

### **Step 1: Check Input Constraints**
- **The first thing you do is check the maximum value of `N` (size of input)**.
- This helps determine **how fast your solution must be**.

| **Max Value of N** | **Allowed Time Complexity** | **Why?** |
|----------------|------------------|-------------------|
| **N ≤ 10** | O(N!), O(2^N) | Brute-force and backtracking work fine. |
| **N ≤ 100** | O(N²) | Quadratic solutions (nested loops) are okay. |
| **N ≤ 10⁴ (10,000)** | O(N log N) | Sorting and log-based solutions work. |
| **N ≤ 10⁶ (1,000,000)** | O(N) or O(N log N) | Linear or near-linear required. |
| **N ≥ 10⁸ (100,000,000)** | O(log N) or O(1) | Must be very optimized. |

💡 **Rule of Thumb:**
- **10⁶ operations run in ~1 second** on a standard system.
- **10⁸ operations take too long → use O(log N) or O(1).**

---

### **Step 2: Identify Your Approach Based on Constraints**
Once you know the constraints, **pick the best approach**:

| **Problem Type** | **Best Time Complexity** | **Approach** |
|----------------|----------------|----------------|
| **Brute Force** | O(N²) or worse | Try everything (e.g., nested loops). |
| **Sorting** | O(N log N) | Use `sort()`, QuickSort, MergeSort. |
| **Searching** | O(log N) | Use **Binary Search** for sorted data. |
| **Graph Traversal** | O(V + E) | Use **BFS/DFS** for trees and graphs. |
| **DP (Memoization)** | O(N) | Store intermediate results to optimize. |
| **Greedy** | O(N log N) | Sorting + greedy choice (e.g., Huffman coding). |
| **Hashing** | O(1) avg | Use `unordered_map`, `unordered_set` for fast lookup. |

---

### **Step 3: Common Patterns to Optimize**
Here are common optimizations:

| **Brute Force** | **Optimized Approach** |
|----------------|----------------------|
| Loop inside loop (O(N²)) | **Sorting + Binary Search (O(N log N))** |
| Checking pairs one by one | **Use HashSet (O(N))** |
| Recursion (O(2^N)) | **Use DP (O(N))** |
| Searching in sorted array (O(N)) | **Use Binary Search (O(log N))** |

---

### **Step 4: Recognizing Time Complexity in Code**
**How to analyze a function's time complexity?**
- **Loops → O(N), O(N²) for nested**
- **Recursion → Count function calls**
- **Sorting → O(N log N)**
- **Binary Search → O(log N)**
- **Hashing → O(1) avg, O(N) worst**
- **Graph Traversal → O(V + E)**

---

### **Step 5: Example Problems**
1️⃣ **Given an array of size `N ≤ 10⁵`, find if a sum exists.**
   - **Brute Force:** O(N²) (Check all pairs)
   - **Better:** O(N log N) (Sort + Binary Search)
   - **Best:** O(N) (Use `unordered_set` for lookup)

2️⃣ **Find the Kth largest element in an array (`N ≤ 10⁶`).**
   - **Sorting Approach:** O(N log N)
   - **Heap Approach:** O(N log K) (better for large `N`)

3️⃣ **Check if a number is prime (`N ≤ 10⁹`).**
   - **Brute Force:** O(N) (Check all numbers)
   - **Optimized:** O(√N) (Check only divisors up to √N)

---

### 🔥 **Final Strategy for Coding Challenges**
1. **Check Constraints** → Determines required complexity.
2. **Identify Problem Type** → Choose the best approach.
3. **Optimize Step by Step** → Use hashing, sorting, or binary search.
4. **Test on Large Inputs** → See if your code runs within 1 second.
---
# 🚀 **How to Determine the Required Time & Space Complexity in Coding**
When solving a coding problem, **always analyze two things**:
1. **Time Complexity** → To check how fast the code runs.
2. **Space Complexity** → To check how much extra memory it needs.

---

## 🔥 **1. The `10⁸ Rule` to Estimate Time Complexity**
**🔹 How many operations can we perform in 1 second?**  
- A normal processor can do about **10⁸ (100 million) operations per second**.  
- So, if **N ≤ 10⁶ (1 million)**, an **O(N log N)** solution is usually fine.  
- If **N ≈ 10⁸**, your algorithm **must be O(N) or faster** (O(log N) or O(1)).  

| **Max `N` Given in Problem** | **Best Allowed Complexity** |
|----------------|------------------|
| `N ≤ 10` | **O(N!) or O(2^N)** (Brute force works) |
| `N ≤ 100` | **O(N²)** (Nested loops are okay) |
| `N ≤ 10⁴ (10,000)` | **O(N log N)** (Sorting, Binary Search) |
| `N ≤ 10⁶ (1,000,000)` | **O(N) or O(N log N)** (Efficient loops, segment trees) |
| `N ≥ 10⁸ (100,000,000)` | **O(log N) or O(1)** (Binary search, hash maps) |

💡 **Quick trick**:  
- If `N = 10⁸`, you must **avoid nested loops (`O(N²)`)** because it will take **too long to run**.
- If `N = 10⁶`, you **can't use O(N²)** but **O(N log N) works fine**.

---

## 📦 **2. Space Complexity: How to Choose the Right Approach?**
Space complexity tells you **how much extra memory your program needs**.

| **Max N** | **Best Space Complexity** | **Allowed Approach** |
|-----------|------------------|----------------|
| **N ≤ 10⁴** | **O(N²) is okay** | DP tables, adjacency matrices |
| **N ≤ 10⁶** | **O(N) is okay** | Arrays, hash maps, vectors |
| **N ≥ 10⁸** | **O(1) or O(log N)** | Bit manipulation, in-place sorting |

### 🔥 **How to Determine Space Complexity?**
- **If you only use a few variables** → **O(1)** (Best case).
- **If you use an array of size `N`** → **O(N)**.
- **If you use a 2D array (matrix)** → **O(N²)**.
- **If you use recursion** → Watch out for **stack space** (`O(N)` for deep recursion).

---

## 🔍 **3. How to Decide Complexity for Your Code?**
When writing code, ask yourself:
1. **What is `N` in the problem?**  
   - If `N ≤ 100`, `O(N²)` is okay.
   - If `N = 10⁶`, `O(N log N)` is the max allowed.
   - If `N = 10⁸`, you need **O(N) or better**.

2. **Do I need extra memory?**  
   - If the problem says **"optimize space"**, avoid `O(N)` solutions.
   - Try to use **in-place modifications** (e.g., two-pointer method).

3. **Are nested loops needed?**  
   - If `N = 10⁶`, **avoid `O(N²)`**.
   - Try **sorting + binary search** (`O(N log N)`) instead.

---

## 🚀 **4. Cheat Sheet: What Complexity Do You Need?**
| **Problem Type** | **Best Time Complexity** | **Best Space Complexity** | **Approach** |
|----------------|----------------|----------------|----------------|
| **Sorting** | **O(N log N)** | **O(1) or O(N)** | `sort()`, Merge Sort |
| **Searching** | **O(log N)** | **O(1)** | Binary Search |
| **Graph Traversal** | **O(V + E)** | **O(V + E)** | BFS, DFS |
| **DP (Memoization)** | **O(N)** | **O(N)** | Fibonacci, Subset Sum |
| **Brute Force** | **O(N²) or O(2^N)** | **O(1) or O(N)** | Recursion, Backtracking |
| **Greedy Algorithms** | **O(N log N)** | **O(1) or O(N)** | Activity Selection |
| **Hashing (Lookup)** | **O(1) (avg), O(N) (worst)** | **O(N)** | `unordered_map` |

---

## 🔥 **5. Example Questions & How to Decide Complexity**
### **Example 1: Find a Pair That Sums to `X` (`N ≤ 10⁶`)**
1. **Brute Force**: O(N²) (Check all pairs) ❌ (Too slow)
2. **Sorting + Binary Search**: O(N log N) ✅ (Works)
3. **Hashing (`unordered_set`)**: O(N) ✅ (Best solution)

### **Example 2: Find the Kth Largest Element (`N ≤ 10⁶`)**
1. **Sorting**: O(N log N) ✅ (Works)
2. **Heap (`priority_queue`)**: O(N log K) ✅ (Better)

### **Example 3: Check If a Number is Prime (`N ≤ 10⁹`)**
1. **Brute Force**: O(N) ❌ (Too slow)
2. **Optimized Check**: O(√N) ✅ (Best approach)

---

## 🎯 **Final Takeaways**
- **Always check `N` before choosing an approach**.
- **Use the `10⁸ rule`** to estimate required complexity.
- **Optimize space if needed** (avoid `O(N)` when `N` is large).
- **Binary search, DP, greedy, and hash maps** are your best friends.
---

# 📌 **Aditya Table: Complexity Decision Guide**
### 🔥 **Baseline: If `N = 10⁸`, you must have O(N) complexity or better (O(log N) or O(1))**

| **Max `N` Given in Problem** | **Best Allowed Complexity** | **Typical Approach** | **Avoid** |
|----------------|------------------|----------------|----------------|
| **N ≈ 10¹⁸** | **O(log N) or O(1)** | Bitwise ops, Mathematical formulas, Modular arithmetic | Anything above O(log N) |
| **N = 10⁸** | **O(N) or better** | Hashing, Two-pointer, Binary search | O(N log N), O(N²) |
| **N = 10⁶** | **O(N log N) or O(N)** | Sorting, Segment Trees, DP | O(N²) (nested loops) |
| **N = 10⁴** | **O(N²) or better** | DP (2D), Floyd Warshall | O(N³) or more |
| **N = 500** | **O(N³) is acceptable** | Graph algorithms like Floyd-Warshall, Matrix operations | O(N⁴) |
| **N = 100** | **O(N⁴) is acceptable** | Brute-force DP, Matrix Exponentiation | O(2^N) (Exponential) |
| **N = 20** | **O(2^N) or better** | Backtracking, Bitmask DP | O(N!) (Factorial growth) |
| **N ≤ 10** | **O(N!) is okay** | Complete brute force | None (any method works) |

---

### 🔥 **Key Takeaways from Aditya Table**
1. **`10⁸ means O(N)`** → If `N = 10⁸`, avoid O(N log N) or worse.
2. **`10⁶ allows O(N log N)`** → Sorting is fine, but avoid nested loops.
3. **`N = 500` allows O(N³)`** → Floyd Warshall, Matrix operations are fine.
4. **`N ≤ 20` allows O(2^N)`** → You can use recursion, but factorial (`O(N!)`) is very slow.
5. **Brute force (O(N!)) works for `N ≤ 10`**, but avoid for larger values.

---

### 🚀 **Example Scenarios Using the Table**
#### **1️⃣ Problem: Find the Kth smallest element in an array of `N = 10⁶`**
- **Allowed Complexity:** O(N log N) ✅
- **Best Approach:** Use Sorting (`O(N log N)`) or QuickSelect (`O(N)`).
- **Avoid:** Brute force (`O(N²)`) ❌

#### **2️⃣ Problem: Find the shortest path in a graph with `N = 500` nodes**
- **Allowed Complexity:** O(N³) ✅
- **Best Approach:** Floyd-Warshall (`O(N³)`)
- **Avoid:** Dijkstra with adjacency matrix (`O(N² log N)`) for large `N`

#### **3️⃣ Problem: Find all permutations of a set where `N = 15`**
- **Allowed Complexity:** O(2^N) ✅
- **Best Approach:** Backtracking.
- **Avoid:** Factorial (`O(N!)`) for larger `N` ❌

---

## 🎯 **Final Strategy for Coding Challenges**
1. **Find `N` in the problem statement**.
2. **Check the Aditya Table to get the expected complexity**.
3. **Choose an approach that fits within the complexity limit**.
4. **Optimize using Binary Search, Hashing, or DP if needed**.

---