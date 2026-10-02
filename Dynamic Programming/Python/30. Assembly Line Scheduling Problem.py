def carAssembly(stationTime, transferTime, entryTime, exitTime):
    N = 4
    bestLine1 = [0] * N
    bestLine2 = [0] * N
    bestLine1[0] = entryTime[0] + stationTime[0][0]
    bestLine2[0] = entryTime[1] + stationTime[1][0]
    for i in range(1, N):
        bestLine1[i] = min(
            bestLine1[i - 1] + stationTime[0][i],
            bestLine2[i - 1] + transferTime[1][i] + stationTime[0][i],
        )
        bestLine2[i] = min(
            bestLine2[i - 1] + stationTime[1][i],
            bestLine1[i - 1] + transferTime[0][i] + stationTime[1][i],
        )
    return min(bestLine1[N - 1] + exitTime[0], bestLine2[N - 1] + exitTime[1])


def main():
    stationTime = [[4, 5, 3, 2], [2, 10, 1, 4]]
    transferTime = [[0, 7, 4, 5], [0, 9, 2, 8]]
    entryTime = [10, 12]
    exitTime = [18, 7]
    print("Minimum time to assemble the car:",
          carAssembly(stationTime, transferTime, entryTime, exitTime))


if __name__ == "__main__":
    main()


'''
Time: O(N): each station computes two best times from staying or switching
lines in constant work. The source fixes N=4, so this implementation is O(1).
Space: O(N) auxiliary for bestLine1/bestLine2; with N=4 this is O(1).
Input arrays must contain exactly the four stations expected by the source.
'''
