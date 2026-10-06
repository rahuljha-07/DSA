class MinStack:
    def __init__(self):
        self.s = []
        self.minElement = None

    # Push function to add an element to the stack
    def push(self, x):
        # If the stack is empty, set minElement to the new element
        if len(self.s) == 0:
            self.s.append(x)
            # Initialize minElement
            self.minElement = x
        else:
            # If the new element is less than or equal to the current min,
            # push a modified value to track the new minimum.
            if x < self.minElement:
                # Store a value that can help recover the new min
                self.s.append(2 * x - self.minElement)
                # Update the minElement
                self.minElement = x
            else:
                # Just push the new element
                self.s.append(x)

    # Pop function to remove the top element from the stack
    def pop(self):
        if len(self.s) == 0:
            # Handle underflow condition
            print("Stack Underflow")
            return

        topValue = self.s[-1]
        # Remove the top element
        self.s.pop()

        # If the popped value is less than the current minElement,
        # it means we are removing the minimum value.
        if topValue < self.minElement:
            # Recover the previous minElement
            self.minElement = 2 * self.minElement - topValue

    # Function to get the current top element of the stack
    def top(self):
        if len(self.s) == 0:
            print("Stack is empty")
            # Stack is empty
            return -1

        topValue = self.s[-1]
        # If topValue is less than the current minElement,
        # it indicates that this was a special value to track the minimum.
        return self.minElement if topValue < self.minElement else topValue

    # Function to get the minimum element in the stack
    def getMin(self):
        if len(self.s) == 0:
            print("Stack is empty")
            return -1
        # Return the minimum element
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
