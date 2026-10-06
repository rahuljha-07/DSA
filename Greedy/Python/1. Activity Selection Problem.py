# Comparator function to sort meetings by their end time
def comp(a, b):
    return a[1] < b[1]


def maxMeetings(start, end):
    n = len(start)
    meetings = [(start[i], end[i]) for i in range(n)]
    meetings.sort(key=lambda a: a[1])
    if n == 0:
        return 0
    # Initialize variables
    # Count of meetings that can be held (start with the first meeting)
    count = 1
    # End time of the last selected meeting
    lastEndTime = meetings[0][1]
    # Iterate through the sorted meetings to select non-overlapping meetings
    for i in range(1, n):
        # If the current meeting starts after the last selected meeting ends
        if meetings[i][0] > lastEndTime:
            # Increment count of meetings
            count += 1
            # Update the last end time
            lastEndTime = meetings[i][1]
    # Return the maximum number of meetings
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
