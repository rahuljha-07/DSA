def comp(a, b):
    return a[1] < b[1]


def maxMeetings(start, end):
    n = len(start)
    meetings = [(start[i], end[i]) for i in range(n)]
    meetings.sort(key=lambda a: a[1])
    if n == 0:
        return 0
    count = 1
    lastEndTime = meetings[0][1]
    for i in range(1, n):
        if meetings[i][0] > lastEndTime:
            count += 1
            lastEndTime = meetings[i][1]
    return count


def main():
    start = [1, 3, 0, 5, 8, 5]
    end = [2, 4, 6, 7, 9, 9]
    print("Maximum number of meetings:", maxMeetings(start, end))


if __name__ == "__main__":
    main()


'''
Let n be meetings.
Time: O(n log(n+1)): build pairs, sort by finish time, and scan once.
Space: O(n) auxiliary meeting pairs and Python sorting workspace.
Strict start>lastEndTime is retained: touching endpoints are not allowed.
Empty input returns zero rather than indexing the first meeting.
'''
