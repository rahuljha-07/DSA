# Helper function to print the Kth node from the end
def findKthFromEnd(head, k):
    # Base case: if we reach the end of the list, return None
    if head is None:
        return None
    # Recursive call to go to the end of the list
    node = findKthFromEnd(head.next, k)
    # When coming back from the recursive call, decrement k
    k[0] -= 1
    # When k is 0, we have found the Kth node from the end
    if k[0] == 0:
        # Return the node that is Kth from the end
        return head
    # Return the node found in the previous recursive calls
    return node


# Function to get the Kth node from the end
def getKthFromEnd(head, k):
    return findKthFromEnd(head, [k])


# iterative
# Function to find the Nth node from the end of the list
def getNthFromLast(head, n):
    if head is None or n <= 0:
        return -1
    # Initialize two pointers: 'primary' and 'follower' both pointing to the head
    primary = head
    follower = head
    # Step 1: Move 'primary' n nodes ahead
    count = 1
    while count < n:
        if primary.next is None:
            return -1
        primary = primary.next
        count += 1
    # Step 2: Move both 'primary' and 'follower' one step at a time until 'primary' reaches
    # the end
    while primary.next is not None:
        primary = primary.next
        follower = follower.next
    # 'follower' is now at the Nth node from the end
    return follower.data


'''
Let L be the number of nodes and k/n the requested position from the end.
Recursive time: O(L): reaches the tail and decrements k once per returning
call. Space: O(L) auxiliary for the stack; [k] is a constant-size reference
holder so all calls share the same counter, like C++ int&.
Iterative time: O(L): primary advances at most L-1 times overall, first
to create the gap and then alongside follower. Space: O(1) auxiliary.
Neither method allocates result nodes.
'''
