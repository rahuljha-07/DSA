class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


# Function to insert a new node at the end of the doubly linked list
def append(head, data):
    newNode = Node(data)
    if not head:
        head = newNode
        return head
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = newNode
    newNode.prev = temp
    return head


# Function to print the triplets whose sum is equal to a given value X
def printTripletsWithSum(head, X):
    if not head:
        return
    # Find tail node
    tail = head
    while tail.next:
        tail = tail.next
    found = False
    first = head
    while first and first.next and first.next.next:
        left = first.next
        right = tail
        # Data order also catches crossing after duplicate-skipping jumps.
        while (left and right and left is not right
               and right.next is not left and left.data <= right.data):
            sum = first.data + left.data + right.data
            if sum == X:
                print(f"({first.data}, {left.data}, {right.data})")
                found = True
                # Move left pointer to avoid duplicates
                tempLeft = left
                while left and left.data == tempLeft.data:
                    left = left.next
                # Move right pointer to avoid duplicates
                tempRight = right
                while right and right.data == tempRight.data:
                    # Decrease sum
                    right = right.prev
            elif sum < X:
                # Increase sum
                left = left.next
            else:
                right = right.prev
        first = first.next
    if not found:
        print(f"No triplets found with sum {X}")


# Helper function to print the doubly linked list (for testing purposes)
def printList(head):
    while head is not None:
        print(head.data, end=" <-> ")
        head = head.next
    print("NULL")


def main():
    head = None
    head = append(head, 1)
    head = append(head, 2)
    head = append(head, 4)
    head = append(head, 5)
    head = append(head, 6)
    head = append(head, 8)
    head = append(head, 9)
    target = 15
    print(f"Triplets with sum {target} are:")
    printTripletsWithSum(head, target)


if __name__ == "__main__":
    main()


'''
Let n be the number of nodes in the sorted DLL.
Time: O(n^2): for each of O(n) choices of first, left and right traverse
the remaining suffix in O(n). Duplicate-skipping only advances pointers.
Finding the tail adds O(n), which does not change the quadratic bound.
Space: O(1) auxiliary: triplets are printed immediately, not collected.
As in the source, equal left/right values are skipped after a match;
equal values of first are not skipped, so duplicate printed triplets
can remain. Demo construction costs O(n^2) due to repeated append scans.
'''
