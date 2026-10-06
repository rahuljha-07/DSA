# Comparator function to sort trains by departure time
def comp(a, b):
    # Sort by departure time
    return a[1] < b[1]


# Function to find the maximum number of trains that can be stopped
def maxStops(trains, n, m):
    trains.sort(key=lambda a: a[1])
    # Step 2: Track the last departure time for each platform
    # Platforms are 1-based
    lastDeparture = [-1] * (n + 1)
    # To count the number of accommodated trains
    count = 0
    # Step 3: Process each train
    for i in range(m):
        # Platform number
        platform = trains[i][2]
        arrival = trains[i][0]
        departure = trains[i][1]
        # If platform is empty or the train can fit after the last train
        if lastDeparture[platform] == -1 or lastDeparture[platform] <= arrival:
            # Train is accommodated
            count += 1
            # Update the last departure time for the platform
            lastDeparture[platform] = departure
    print("Maximum Stopped Trains =", count)


def main():
    n = 3
    m = 6
    trains = [[1000,1030,1], [1010,1030,1], [1000,1020,2],
              [1030,1200,2], [1200,1230,3], [900,1005,1]]
    maxStops(trains, n, m)
    n = 1
    m = 3
    trains = [[1000,1030,1], [1110,1130,1], [1200,1220,1]]
    maxStops(trains, n, m)


if __name__ == "__main__":
    main()


'''
Let n be platforms and m=len(trains) trains.
Time: O(n + m log(m+1)): initialize platform times, sort all departures,
then scan each train once.
Space: O(n+m) auxiliary lastDeparture and Python sorting workspace.
trains is reordered in place; touching departure/arrival times are allowed.
Platform labels must be 1..n.
'''
