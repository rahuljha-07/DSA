#include <iostream>
#include <algorithm> // std::min

using namespace std;

// Returns the minimum total time to assemble the car.
int carAssembly(int stationTime[][4], int transferTime[][4],
                int entryTime[2], int exitTime[2]) {
    const int N = 4;          // number of stations per line
    int bestLine1[N], bestLine2[N]; // DP arrays: best time to finish station i on line 1 / line 2

    // Base case: first station includes entry time
    bestLine1[0] = entryTime[0] + stationTime[0][0];
    bestLine2[0] = entryTime[1] + stationTime[1][0];

    // Fill DP for remaining stations
    for (int i = 1; i < N; ++i) {
        // To be at station i on line 1: either stay on line 1, or switch from line 2
        bestLine1[i] = min(bestLine1[i - 1] + stationTime[0][i],
                           bestLine2[i - 1] + transferTime[1][i] + stationTime[0][i]);

        // To be at station i on line 2: either stay on line 2, or switch from line 1
        bestLine2[i] = min(bestLine2[i - 1] + stationTime[1][i],
                           bestLine1[i - 1] + transferTime[0][i] + stationTime[1][i]);
    }

    // Add exit time at the last station and take the minimum
    return min(bestLine1[N - 1] + exitTime[0],
               bestLine2[N - 1] + exitTime[1]);
}

int main() {
    // Processing time at each station: stationTime[line][station]
    int stationTime[2][4] = {
        { 4, 5, 3, 2 },   // line 1
        { 2, 10, 1, 4 }   // line 2
    };

    // Transfer time to switch lines before station i:
    // transferTime[0][i] = from line 1 to line 2 at station i
    // transferTime[1][i] = from line 2 to line 1 at station i
    int transferTime[2][4] = {
        { 0, 7, 4, 5 },
        { 0, 9, 2, 8 }
    };

    int entryTime[2] = { 10, 12 };
    int exitTime [2] = { 18,  7 };

    cout << "Minimum time to assemble the car: "
         << carAssembly(stationTime, transferTime, entryTime, exitTime)
         << endl;
    return 0;
}
