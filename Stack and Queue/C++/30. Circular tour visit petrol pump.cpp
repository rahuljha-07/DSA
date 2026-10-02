// Function to find the starting point where the truck can start to get through
// the complete circle without exhausting its petrol in between.
int tour(petrolPump p[], int n) {
    int start = 0;          // Starting index for the tour
    int fuelshort = 0;      // Total fuel shortfall encountered
    int fueltank = 0;       // Current fuel tank level

    // Iterate over each petrol pump
    for (int i = 0; i < n; i++) {
        // Update the fuel tank with petrol gained and petrol used
        fueltank += p[i].petrol - p[i].distance;

        // If the fuel tank level goes negative
        if (fueltank < 0) {
            // Move the start point to the next pump
            start = i + 1;

            // Add the shortfall to the total fuel shortfall
            fuelshort += fueltank;

            // Reset the current fuel tank level
            fueltank = 0;
        }
    }

    // If total fuel shortfall + remaining fuel in tank is non-negative, return starting index
    // This means that it's possible to complete the tour from the starting point
    if (fuelshort + fueltank >= 0) return start;

    // If not possible, return -1
    return -1;
}
