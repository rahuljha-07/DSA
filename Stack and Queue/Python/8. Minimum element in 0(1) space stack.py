class MinStack:
    def __init__(self):
        self.s = []
        self.minElement = None

    def push(self, x):
        if len(self.s) == 0:
            self.s.append(x)
            self.minElement = x
        else:
            if x < self.minElement:
                self.s.append(2 * x - self.minElement)
                self.minElement = x
            else:
                self.s.append(x)

    def pop(self):
        if len(self.s) == 0:
            print("Stack Underflow")
            return

        topValue = self.s[-1]
        self.s.pop()

        if topValue < self.minElement:
            self.minElement = 2 * self.minElement - topValue

    def top(self):
        if len(self.s) == 0:
            print("Stack is empty")
            return -1

        topValue = self.s[-1]
        return self.minElement if topValue < self.minElement else topValue

    def getMin(self):
        if len(self.s) == 0:
            print("Stack is empty")
            return -1
        return self.minElement


minStack = MinStack()
minStack.push(5)
print("Current Min:", minStack.getMin())
minStack.push(3)
print("Current Min:", minStack.getMin())
minStack.push(7)
print("Current Min:", minStack.getMin())
minStack.pop()
print("Current Min:", minStack.getMin())
minStack.pop()
print("Current Min:", minStack.getMin())


'''
Time Complexity: O(1) for push, pop, top, and getMin

Reason:
The encoded value technique stores previous minimum information inside the
stack value, so no traversal is needed for minimum lookup.

Space Complexity: O(n)

Reason:
The stack stores n encoded or normal values. No extra minimum stack is used.
'''
