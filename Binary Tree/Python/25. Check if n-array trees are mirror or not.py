from collections import deque


def checkMirrorTree(n, e, A, B):
    # Create stacks and queues for each node
    stacks = [[] for _ in range(n + 1)]
    queues = [deque() for _ in range(n + 1)]
    for i in range(0, 2 * e, 2):
        u = A[i]
        v = A[i + 1]
        stacks[u].append(v)
    for i in range(0, 2 * e, 2):
        u = B[i]
        v = B[i + 1]
        queues[u].append(v)
    # Compare the stack and queue for each node
    for i in range(1, n + 1):
        # While both stack and queue have elements
        while stacks[i] and queues[i]:
            # Check if the top of the stack matches the front of the queue
            if stacks[i][-1] != queues[i][0]:
                return 0
            stacks[i].pop()
            queues[i].popleft()
        # If one of them still has elements, they aren't mirrors
        if stacks[i] or queues[i]:
            return 0
    # If all nodes matched in reverse order, the trees are mirrors
    return 1


def main():
    n = 3
    e = 2
    A = [1, 2, 1, 3]
    B = [1, 3, 1, 2]
    result = checkMirrorTree(n, e, A, B)
    print(result)


if __name__ == "__main__":
    main()


'''
Let n be the node count and e the edge count in each n-ary tree.
Time: O(n + e): create n+1 containers, push both edge sets, then compare
and remove each child once. Stack/queue operations are O(1) amortized.
Space: O(n + e) auxiliary for per-parent containers and stored children.
Node labels are assumed to be in 1..n, matching the source.
'''
