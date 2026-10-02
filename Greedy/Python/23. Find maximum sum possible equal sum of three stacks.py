def maxSum(stack1, stack2, stack3, n1, n2, n3):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in range(n1):
        sum1 += stack1[i]
    for i in range(n2):
        sum2 += stack2[i]
    for i in range(n3):
        sum3 += stack3[i]
    top1 = 0
    top2 = 0
    top3 = 0
    while True:
        if top1 == n1 or top2 == n2 or top3 == n3:
            return 0
        if sum1 == sum2 == sum3:
            return sum1
        if sum1 >= sum2 and sum1 >= sum3:
            sum1 -= stack1[top1]
            top1 += 1
        elif sum2 >= sum1 and sum2 >= sum3:
            sum2 -= stack2[top2]
            top2 += 1
        elif sum3 >= sum1 and sum3 >= sum2:
            sum3 -= stack3[top3]
            top3 += 1


def main():
    stack1 = [3, 2, 1, 1, 1]
    stack2 = [4, 3, 2]
    stack3 = [1, 1, 4, 1]
    n1 = len(stack1)
    n2 = len(stack2)
    n3 = len(stack3)
    print(maxSum(stack1, stack2, stack3, n1, n2, n3))


if __name__ == "__main__":
    main()


'''
Let n1, n2, and n3 be the sizes of stacks of positive elements.
Time: O(n1+n2+n3): initial summation visits every element once, and each
while-loop iteration advances one top index. No index ever moves back.
Space: O(1) auxiliary: only three sums and three indices are maintained.
Index 0 represents the top; index increments simulate pops without copying
or modifying the input stacks.
'''
