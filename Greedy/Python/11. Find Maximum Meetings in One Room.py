def maxMeetings(start, end, n):
    meetings = []
    for i in range(n):
        meetings.append([start[i], end[i], i + 1])
    meetings.sort(key=lambda a: a[1])
    if n == 0:
        print()
        return
    selectedMeetings = [meetings[0][2]]
    timeLimit = meetings[0][1]
    for i in range(1, n):
        if meetings[i][0] > timeLimit:
            selectedMeetings.append(meetings[i][2])
            timeLimit = meetings[i][1]
    for meeting in selectedMeetings:
        print(meeting, end=" ")
    print()


def main():
    start = [1, 3, 0, 5, 8, 5]
    end = [2, 4, 6, 7, 9, 9]
    n = len(start)
    maxMeetings(start, end, n)


if __name__ == "__main__":
    main()


'''
Let n be meetings.
Time: O(n log(n+1)): sort by finish time, then scan/print at most n IDs.
Space: O(n) auxiliary triples, selectedMeetings, and sorting workspace.
IDs are 1-based and printed in selection order. Strict start>timeLimit
is retained; touching endpoints are disallowed.
'''
