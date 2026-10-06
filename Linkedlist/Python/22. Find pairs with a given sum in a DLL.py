class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


# Function to find pairs with a given sum and return them in a list
def findPairsWithSum(head, target):
    # list to store pairs
    result = []
    if not head:
        return result
    # Initialize pointers for the two-pointer approach
    left = head
    right = head
    # Move `right` to the last node
    while right.next is not None:
        right = right.next
    # Adjacent nodes are still a valid pair; stop only after crossing.
    while left is not right and right.next is not left:
        sum = left.data + right.data
        if sum == target:
            # Store the pair
            result.append((left.data, right.data))
            # Move left pointer forward to increase sum
            left = left.next
            # Move right pointer backward to decrease sum
            right = right.prev
        elif sum < target:
            left = left.next
        else:
            right = right.prev
    # Return the list of pairs
    return result


# Function to print the list of pairs
def printPairs(pairs):
    for p in pairs:
        print(f"({p[0]}, {p[1]})")


# Helper function to print the doubly linked list (for testing purposes)
def printList(head):
    while head is not None:
        print(head.data, end=" <-> ")
        head = head.next
    print("NULL")


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


def main():
    head = None
    head = append(head, 1)
    head = append(head, 2)
    head = append(head, 4)
    head = append(head, 5)
    head = append(head, 6)
    head = append(head, 8)
    head = append(head, 9)
    target = 7
    pairs = findPairsWithSum(head, target)
    print(f"Pairs with sum {target} are:")
    printPairs(pairs)


if __name__ == "__main__":
    main()


'''
Let n be the number of nodes in the sorted DLL and p the returned pairs.
Time: O(n): finding the tail costs O(n); each two-pointer step advances
left or retreats right, so the search also takes at most O(n) steps.
Space: O(1) auxiliary for pointers and sum; O(p) output for result tuples,
at most O(n). Repeated append calls in the demo cost O(n^2) setup separately.
'''
