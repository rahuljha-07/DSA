class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


# Function to reverse the linked list
def reverse(head):
    prev = None
    curr = head
    nextNode = None
    while curr is not None:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    # New head after reversing
    return prev


# Function to add two numbers represented by linked lists
def addTwoLists(first, second):
    # Step 1: Reverse both the linked lists
    first = reverse(first)
    second = reverse(second)
    # Variable to store the sum of two digits
    sum = 0
    # Variable to store the carry for the next digit
    carry = 0
    # The result linked list (initialized as None)
    res = None
    # Step 2: Traverse both lists and add corresponding digits
    while first is not None or second is not None:
        # Add corresponding digits along with the carry (if any)
        sum = carry + (first.data if first else 0) + (second.data if second else 0)
        # Calculate the carry for the next iteration
        carry = sum // 10
        # The new digit (ones place of the sum)
        sum = sum % 10
        # Create a new node with the sum and add it to the result list
        temp = Node(sum)
        # If the result list is not empty, set the new node's next to the current result
        # list
        if res is not None:
            temp.next = res
        # The new node becomes the result list's head
        res = temp
        if first:
            first = first.next
        if second:
            second = second.next
    # Step 3: If there's a carry left, create a new node with the carry
    if carry > 0:
        temp = Node(carry)
        temp.next = res
        res = temp
    # Step 4: Return the result list (the sum of the two numbers)
    return res


'''
Let n and m be the lengths of the most-significant-digit-first input lists.
Time: O(n + m): reversing both lists costs n + m steps; addition processes
at most max(n, m) digit positions, plus one possible final carry.
Space: O(1) auxiliary for pointers and carry; O(max(n, m)) output space
for newly created sum nodes. Like the C++ version, input links are reversed
and are not restored.
'''
