def runCustomerSimulation(n, seq):
    inUse = {}
    inCafe = set()
    occupied = 0
    result = 0

    for customer in seq:
        if customer not in inCafe:
            inCafe.add(customer)
            if occupied < n:
                inUse[customer] = True
                occupied += 1
            else:
                inUse[customer] = False
        else:
            if inUse[customer]:
                occupied -= 1
            else:
                result += 1
            inCafe.remove(customer)
            del inUse[customer]

    return result


print(runCustomerSimulation(2, "ABBAJJKZKZ"))
print(runCustomerSimulation(3, "GACCBDDBAGEE"))
print(runCustomerSimulation(3, "GACCBGDDBAEE"))
print(runCustomerSimulation(1, "ABCBCA"))
print(runCustomerSimulation(1, "ABCBCADEED"))


'''
Time Complexity: O(n), where n is sequence length.

Reason:
The sequence is scanned once.
For each customer character, set and dictionary operations take
constant average time.

Space Complexity: O(k)

Reason:
The inCafe set and inUse dictionary store customers currently tracked.
In the worst case, this can include k distinct customers.
'''
