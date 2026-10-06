class Node:
    def __init__(self, val):
        self.data = val
        self.prev = None
        self.next = None


class StackWithMiddle:
    def __init__(self):
        self.head = None
        self.mid = None
        self.count = 0

    # Push an element onto the stack
    def push(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.mid = self.head
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

        self.count += 1

        # Update mid pointer
        if self.count == 1:
            self.mid = self.head
        elif self.count % 2 == 0:
            self.mid = self.mid.prev

    # Pop the top element from the stack
    def pop(self):
        if self.count == 0:
            print("Stack is empty.")
            return -1

        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None

        self.count -= 1

        if self.count == 0:
            self.mid = None
        elif self.count % 2 != 0:
            self.mid = self.mid.next

        return data

    # Find the middle element of the stack
    def findMiddle(self):
        if self.count == 0:
            print("Stack is empty.")
            return -1
        return self.mid.data

    def deleteMiddle(self):
        if self.count == 0:
            print("Stack is empty.")
            return

        temp = self.mid
        midData = self.mid.data

        # Case 1: Only one element in the stack
        if self.count == 1:
            self.head = None
            self.mid = None
        # Case 2: Middle node has both prev and next
        else:
            if self.mid.prev:
                self.mid.prev.next = self.mid.next
            if self.mid.next:
                self.mid.next.prev = self.mid.prev

        # Move `mid` correctly after deletion
        if self.count > 1:
            if self.count % 2 == 0:
                # Move forward when count is even
                self.mid = temp.next
            else:
                # Move backward when count is odd
                self.mid = temp.prev

        self.count -= 1
        print("Deleted middle element:", midData)


stack = StackWithMiddle()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

print("Middle element:", stack.findMiddle())
stack.deleteMiddle()
print("Middle element after deletion:", stack.findMiddle())
stack.push(60)
print("Middle element after push:", stack.findMiddle())
stack.pop()
print("Middle element after pop:", stack.findMiddle())


'''
Time Complexity: O(1) for push, pop, findMiddle, and deleteMiddle

Reason:
The stack keeps direct head and middle pointers in a doubly linked list, so
middle access and deletion do not require traversal.

Space Complexity: O(n)

Reason:
One linked-list node is stored for each stack element.
'''
