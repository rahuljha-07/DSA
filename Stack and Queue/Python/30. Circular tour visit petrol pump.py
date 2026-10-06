# Function to find the starting point where the truck can start to get through
# the complete circle without exhausting its petrol in between.
def tour(p, n):
    # Starting index for the tour
    start = 0
    # Total fuel shortfall encountered
    fuelshort = 0
    # Current fuel tank level
    fueltank = 0

    # Iterate over each petrol pump
    for i in range(n):
        # Update the fuel tank with petrol gained and petrol used
        fueltank += p[i][0] - p[i][1]

        # If the fuel tank level goes negative
        if fueltank < 0:
            # Every start from the old start through i fails here; try the next pump.
            start = i + 1
            # Add the shortfall to the total fuel shortfall
            fuelshort += fueltank
            # Reset the current fuel tank level
            fueltank = 0

    # Complete the tour only if the remaining fuel covers all earlier shortfalls.
    if fuelshort + fueltank >= 0:
        return start

    # If not possible, return -1
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
