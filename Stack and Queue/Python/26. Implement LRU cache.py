from collections import OrderedDict


class LRUCache:
    def __init__(self, cap):
        self.capacity = cap
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def set(self, key, value):
        if self.capacity == 0:
            return
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value


cache = LRUCache(2)
cache.set(1, 100)
cache.set(2, 200)
print("Get (1):", cache.get(1))
cache.set(3, 300)
print("Get (2):", cache.get(2))
cache.set(4, 400)
print("Get (1):", cache.get(1))
print("Get (3):", cache.get(3))
print("Get (4):", cache.get(4))
cache.set(3, 350)
print("Get (3):", cache.get(3))
cache.set(5, 500)
print("Get (4):", cache.get(4))
print("Get (5):", cache.get(5))


'''
Time Complexity: O(1) average for get and set

Reason:
The cache combines hash-map lookup with an ordered doubly linked structure.
Moving, inserting, and evicting keys are constant-time operations on average.

Space Complexity: O(capacity)

Reason:
The cache stores at most capacity key-value pairs.
'''
