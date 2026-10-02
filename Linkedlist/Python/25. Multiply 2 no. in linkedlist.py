MOD = 1000000007


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


def linkedListToNumber(head):
    num = 0
    while head is not None:
        num = (num * 10 + head.data) % MOD
        head = head.next
    return num


def multiplyTwoLists(L1, L2):
    num1 = linkedListToNumber(L1)
    num2 = linkedListToNumber(L2)
    result = (num1 * num2) % MOD
    return result


def reverse(head):
    prev = None
    curr = head
    next = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def addLists(l1, l2):
    dummy = Node(0)
    temp = dummy
    carry = 0
    while l1 or l2 or carry:
        sum = carry + (l1.data if l1 else 0) + (l2.data if l2 else 0)
        carry = sum // 10
        temp.next = Node(sum % 10)
        temp = temp.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy.next


# Distinct name retains the digit-list alternative alongside modular multiplication.
def multiplyTwoListsAsList(L1, L2):
    if not L1 or not L2:
        return None
    L1 = reverse(L1)
    L2 = reverse(L2)
    result = None
    tempResult = None
    tempL1 = L1
    positionShift = 0
    while tempL1:
        tempL2 = L2
        temp = Node(0)
        current = temp
        for i in range(positionShift):
            current.next = Node(0)
            current = current.next
        carry = 0
        while tempL2:
            mul = tempL1.data * tempL2.data + carry
            carry = mul // 10
            current.next = Node(mul % 10)
            current = current.next
            tempL2 = tempL2.next
        if carry:
            current.next = Node(carry)
        result = addLists(result, temp.next)
        positionShift += 1
        tempL1 = tempL1.next
    return reverse(result)


def printList(head):
    while head is not None:
        print(head.data, end="")
        head = head.next
    print()


def createList(num):
    head = None
    tail = None
    while num > 0:
        digit = num % 10
        newNode = Node(digit)
        if head is None:
            head = tail = newNode
        else:
            tail.next = newNode
            tail = newNode
        num //= 10
    # The multiplication routine expects most-significant-digit-first inputs.
    return reverse(head)


def main():
    num1 = 329
    num2 = 46
    L1 = createList(num1)
    L2 = createList(num2)
    result = multiplyTwoListsAsList(L1, L2)
    printList(result)


if __name__ == "__main__":
    main()


'''
Let n and m be the digit counts of L1 and L2.
Modular method time: O(n + m): each input is scanned once. Space: O(1)
auxiliary: modulo keeps num1/num2 bounded, and the output is one integer.

Digit-list method time: O(n*m + n^2), NOT just O(n*m) for this implementation.
For L1's digit at shift i, it creates i zeros, processes m digits, and
adds lists of length O(m + i). Summing O(m + i) for i = 0..n-1 gives
O(n*m + n^2). Input/output reversals add only O(n + m).
Space: O(n + m) peak auxiliary for temporary products and old/new sums,
plus O(n + m) output nodes. Old intermediate lists are not retained.
Inputs are reversed in place and not restored, as in the C++ method.
'''
