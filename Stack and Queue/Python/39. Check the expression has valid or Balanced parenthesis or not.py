def ispar(x):
    s = []

    for i in range(len(x)):
        if x[i] == '(' or x[i] == '{' or x[i] == '[':
            s.append(x[i])
        else:
            if len(s) == 0:
                return False

            c = s[-1]

            if (x[i] == ')' and c != '(') or (x[i] == '}' and c != '{') or (x[i] == ']' and c != '['):
                return False

            s.pop()

    return len(s) == 0


x = "{([])}"
print(ispar(x))


'''
Time Complexity: O(n)

Reason:
The expression is scanned once. Each opening bracket is pushed once and
popped once when a matching closing bracket is found.

Space Complexity: O(n)

Reason:
The stack can store all opening brackets in the worst case.
'''
