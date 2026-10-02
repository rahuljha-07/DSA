class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if not self.isEmpty():
            self.data.pop()
        else:
            print("Stack is empty, cannot pop.")

    def top(self):
        if not self.isEmpty():
            return self.data[-1]
        else:
            print("Stack is empty, cannot access top.")
            return -1

    def isEmpty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.top())
stack.pop()
print("Top element after pop:", stack.top())

stack.pop()
stack.pop()
stack.pop()


'''
Time Complexity: O(1) amortized for push, pop, top, isEmpty, and size

Reason:
Python list append and pop from the end are O(1) amortized. Accessing the
last element and checking length are constant-time operations.

Space Complexity: O(n)

Reason:
The internal list stores n stack elements.
'''
