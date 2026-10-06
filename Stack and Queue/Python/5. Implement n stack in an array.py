class NStacksInVector:
    # Constructor initializes the list and free_indices
    def __init__(self, size):
        # Resize the list to the specified size, initialize with -1
        self.vec = [-1] * size
        self.free_indices = []
        self.stack_map = {}

        for i in range(size):
            # Add each index to the list of free indices
            self.free_indices.append(i)

    # Push a value onto the specified stack
    def push(self, stack_num, value):
        if len(self.free_indices) == 0:
            print("Stack Overflow")
            return

        # Reuse an index from the back of free_indices
        # Get the last index
        index = self.free_indices[-1]
        self.free_indices.pop()

        # Store the value in the list
        self.vec[index] = value

        if stack_num not in self.stack_map:
            self.stack_map[stack_num] = []
        # Add the index to the map for the specified stack
        self.stack_map[stack_num].append(index)

    # Pop a value from the specified stack
    def pop(self, stack_num):
        if stack_num not in self.stack_map or len(self.stack_map[stack_num]) == 0:
            print("Stack Underflow")
            return -1

        # Get the last index for this stack
        top_index = self.stack_map[stack_num][-1]
        self.stack_map[stack_num].pop()

        # Retrieve the value at this index
        value = self.vec[top_index]
        # Optional: reset the value
        self.vec[top_index] = -1

        # Mark this index as free for future pushes
        self.free_indices.append(top_index)

        return value

    # Get the top value of the specified stack
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
