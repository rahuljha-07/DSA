import heapq


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def mergeKLists(arr, k):
    minHeap = []
    for i in range(k):
        if arr[i] is not None:
            heapq.heappush(minHeap, (arr[i].data, id(arr[i]), arr[i]))
    head = None
    curr = None
    while minHeap:
        top = heapq.heappop(minHeap)
        currNode = top[2]
        currData = top[0]
        if head is None:
            head = currNode
            curr = head
        else:
            curr.next = currNode
            curr = curr.next
        if currNode.next is not None:
            nextNode = currNode.next
            heapq.heappush(minHeap, (nextNode.data, id(nextNode), nextNode))
    return head


def printList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()


def mergesort(first, second):
    if first is None:
        return second
    if second is None:
        return first
    third = None
    last = None
    if first.data < second.data:
        third = last = first
        first = first.next
        last.next = None
    else:
        third = last = second
        second = second.next
        last.next = None
    while first is not None and second is not None:
        if first.data < second.data:
            last.next = first
            last = first
            first = first.next
            last.next = None
        else:
            last.next = second
            last = second
            second = second.next
            last.next = None
    if first is not None:
        last.next = first
    else:
        last.next = second
    return third


def mergeKListsPairwise(arr, k):
    if k <= 0:
        return None
    last = k - 1
    while last != 0:
        i = 0
        j = last
        while i < j:
            arr[i] = mergesort(arr[i], arr[j])
            i += 1
            j -= 1
            if i >= j:
                last = j
    return arr[0]


def main():
    list1 = Node(1)
    list1.next = Node(2)
    list1.next.next = Node(3)
    list2 = Node(4)
    list2.next = Node(5)
    list3 = Node(5)
    list3.next = Node(6)
    list4 = Node(7)
    list4.next = Node(8)
    arr = [list1, list2, list3, list4]
    mergedList = mergeKLists(arr, 4)
    printList(mergedList)


if __name__ == "__main__":
    main()


'''
Let N be the total node count and k the number of sorted disjoint lists.
Heap time: O(k + N log(k+1)): scan heads, then push/pop each node once.
Heap space: O(k) auxiliary for one candidate per list; id breaks equal-
value ties without comparing Python Node objects.
Pairwise time: O(N log k) for k>=2: each round halves active lists and
visits at most N nodes. Head-array overhead adds O(k) for empty lists.
Pairwise space: O(1) auxiliary beyond caller's arr, modified in place.
Both reuse existing output nodes; neither creates a new N-node list.
k=0 returns None; the pairwise k=1 case simply returns the head.
'''
