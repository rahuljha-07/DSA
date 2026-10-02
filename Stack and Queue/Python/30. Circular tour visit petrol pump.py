def tour(p, n):
    start = 0
    fuelshort = 0
    fueltank = 0

    for i in range(n):
        fueltank += p[i][0] - p[i][1]

        if fueltank < 0:
            start = i + 1
            fuelshort += fueltank
            fueltank = 0

    if fuelshort + fueltank >= 0:
        return start

    return -1


p = [[4, 6], [6, 5], [7, 3], [4, 5]]
print(tour(p, len(p)))


'''
Time Complexity: O(n)

Reason:
The petrol pumps are scanned once while tracking current tank and total
shortfall.

Space Complexity: O(1)

Reason:
Only start, fuelshort, and fueltank variables are used.
'''
