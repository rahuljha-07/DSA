def celebrity(M, n):
    s = []

    for i in range(n):
        s.append(i)

    while len(s) >= 2:
        a = s[-1]
        s.pop()
        b = s[-1]
        s.pop()

        if M[a][b] == 1:
            s.append(b)
        else:
            s.append(a)

    potential = s[-1]
    s.pop()

    for i in range(n):
        if potential != i:
            if M[potential][i] != 0 or M[i][potential] != 1:
                return -1

    return potential


M = [[0, 1, 0], [0, 0, 0], [0, 1, 0]]
print(celebrity(M, 3))


'''
Time Complexity: O(n)

Reason:
All people are pushed once. The elimination phase removes two candidates and
pushes one back until one remains, and verification scans one row/column.

Space Complexity: O(n)

Reason:
The stack initially stores all n people.
'''
