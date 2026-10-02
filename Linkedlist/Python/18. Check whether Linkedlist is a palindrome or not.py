def reverse(head):
    prev = None
    curr = head
    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    return prev


def isPalindrome(head):
    if not head or not head.next:
        return True
    slow = head
    # End the first half at the first middle for even-length lists.
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    newHead = slow.next
    slow.next = None
    revHead = reverse(newHead)
    firstHalf = head
    secondHalf = revHead
    while secondHalf:
        if firstHalf.data != secondHalf.data:
            return False
        firstHalf = firstHalf.next
        secondHalf = secondHalf.next
    return True


'''
Let n be the number of nodes.
Time: O(n): locating the midpoint takes O(n), reversing the second half
takes O(n/2), and comparing halves takes at most O(n/2). Passes add to O(n).
Space: O(1) auxiliary: all operations use a fixed number of pointers.
Like the source, this splits and reverses the list without restoring it.
'''
