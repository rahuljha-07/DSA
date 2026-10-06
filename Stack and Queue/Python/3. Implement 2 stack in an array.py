class TwoStacks:
    NULL_VALUE = -10**18

    # Constructor to initialize the two stacks
    def __init__(self, size):
        # Initialize list with NULL_VALUE
        self.arr = [self.NULL_VALUE] * size
        # Stack 1 starts empty
        self.top1 = -1
        # Stack 2 starts empty
        self.top2 = size

    # Push operation for Stack 1
    def pushStack1(self, value):
        # Check if there is no space between stacks
        if self.top1 + 1 == self.top2:
            print("Stack 1 is full, cannot push", str(value) + ".")
            return
        self.top1 += 1
        # Increment top1 and push value
        self.arr[self.top1] = value

    # Push operation for Stack 2
    def pushStack2(self, value):
        if self.top2 - 1 == self.top1:
            print("Stack 2 is full, cannot push", str(value) + ".")
            return
        self.top2 -= 1
        # Decrement top2 and push value
        self.arr[self.top2] = value

    # Pop operation for Stack 1
    def popStack1(self):
        # Check if Stack 1 is empty
        if self.isEmptyStack1():
            print("Stack 1 is empty, cannot pop.")
            return
        # Pop the top element and set it to NULL_VALUE
        self.arr[self.top1] = self.NULL_VALUE
        self.top1 -= 1

    # Pop operation for Stack 2
    def popStack2(self):
        # Check if Stack 2 is empty
        if self.isEmptyStack2():
            print("Stack 2 is empty, cannot pop.")
            return
        self.arr[self.top2] = self.NULL_VALUE
        self.top2 += 1

    # Get the top element of Stack 1
    def topStack1(self):
        if self.isEmptyStack1():
            print("Stack 1 is empty.")
            # or throw an exception
            return self.NULL_VALUE
        return self.arr[self.top1]

    # Get the top element of Stack 2
    def topStack2(self):
        if self.isEmptyStack2():
            print("Stack 2 is empty.")
            return self.NULL_VALUE
        return self.arr[self.top2]

    def isEmptyStack1(self):
        return self.top1 < 0

    def isEmptyStack2(self):
        return self.top2 >= len(self.arr)


stacks = TwoStacks(5)
stacks.pushStack1(10)
stacks.pushStack1(20)
stacks.pushStack2(30)
stacks.pushStack2(40)

print("Top of Stack 1:", stacks.topStack1())
print("Top of Stack 2:", stacks.topStack2())

stacks.popStack1()
print("Top of Stack 1 after pop:", stacks.topStack1())

stacks.popStack2()
print("Top of Stack 2 after pop:", stacks.topStack2())

stacks.pushStack1(50)
stacks.pushStack2(60)
stacks.pushStack1(70)
stacks.pushStack1(80)


'''
Time Complexity: O(1) for all stack operations

Reason:
Each push, pop, top, and empty check only changes or reads one index in the
shared array.

Space Complexity: O(n)

Reason:
The shared array stores at most n elements across both stacks.
'''
