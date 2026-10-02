class NStacksInVector:
    def __init__(self, size):
        self.vec = [-1] * size
        self.free_indices = []
        self.stack_map = {}

        for i in range(size):
            self.free_indices.append(i)

    def push(self, stack_num, value):
        if len(self.free_indices) == 0:
            print("Stack Overflow")
            return

        index = self.free_indices[-1]
        self.free_indices.pop()

        self.vec[index] = value

        if stack_num not in self.stack_map:
            self.stack_map[stack_num] = []
        self.stack_map[stack_num].append(index)

    def pop(self, stack_num):
        if stack_num not in self.stack_map or len(self.stack_map[stack_num]) == 0:
            print("Stack Underflow")
            return -1

        top_index = self.stack_map[stack_num][-1]
        self.stack_map[stack_num].pop()

        value = self.vec[top_index]
        self.vec[top_index] = -1

        self.free_indices.append(top_index)

        return value

    def top(self, stack_num):
        if stack_num not in self.stack_map or len(self.stack_map[stack_num]) == 0:
            print("Stack is Empty")
            return -1

        top_index = self.stack_map[stack_num][-1]
        return self.vec[top_index]


stacks = NStacksInVector(10)
stacks.push(1, 10)
stacks.push(2, 20)
stacks.push(1, 15)

print("Top of stack 1:", stacks.top(1))
print("Popped from stack 1:", stacks.pop(1))
print("Top of stack 1:", stacks.top(1))
print("Popped from stack 2:", stacks.pop(2))
print("Popped from stack 2:", stacks.pop(2))


'''
Time Complexity: O(1) average for push, pop, and top

Reason:
Each operation uses list append/pop from the end and dictionary lookup,
which are O(1) on average.

Space Complexity: O(size)

Reason:
The fixed vector and free index list together store information for the
available array slots, and stack_map stores used indices.
'''
