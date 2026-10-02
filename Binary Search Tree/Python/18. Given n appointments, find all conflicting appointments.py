from bisect import bisect_left, insort


class Interval:
    def __init__(self, low, high, id=None):
        self.low = low
        self.high = high
        self.id = id


class Event:
    def __init__(self, time, isStart, interval):
        self.time = time
        self.isStart = isStart
        self.interval = interval

    def __lt__(self, other):
        if self.time == other.time:
            # End before start matches doOverlap's non-touching semantics.
            return self.isStart < other.isStart
        return self.time < other.time


def doOverlap(i1, i2):
    return not (i1.high <= i2.low or i2.high <= i1.low)


def printConflicting(intervals):
    n = len(intervals)
    for i in range(n):
        for j in range(i + 1, n):
            if doOverlap(intervals[i], intervals[j]):
                print(f"[{intervals[i].low}, {intervals[i].high}] Conflicts with "
                      f"[{intervals[j].low}, {intervals[j].high}]")


def printConflictingSweep(intervals):
    events = []
    for i in range(len(intervals)):
        intervals[i].id = i
        events.append(Event(intervals[i].low, True, intervals[i]))
        events.append(Event(intervals[i].high, False, intervals[i]))
    events.sort()
    active = []
    for event in events:
        if event.isStart:
            for id in active:
                other = intervals[id]
                print(f"[{event.interval.low}, {event.interval.high}]"
                      f" conflicts with [{other.low}, {other.high}]")
            insort(active, event.interval.id)
        else:
            active.pop(bisect_left(active, event.interval.id))


def main():
    appointments = [Interval(1, 5), Interval(3, 7), Interval(2, 6),
                    Interval(10, 15), Interval(5, 6), Interval(4, 100)]
    print("Following are conflicting intervals:")
    printConflicting(appointments)


if __name__ == "__main__":
    main()


'''
Let n be the number of positive-length intervals and C the conflicts.
Pairwise time: O(n^2): every pair is checked. Space: O(1) auxiliary;
conflicts are printed, not collected.
Sweep time: O(n log n + n^2 + C) worst case in Python: sorting 2n events
costs O(n log n), printing costs O(C), and ordered active-list insertions/
deletions can shift O(n) entries per event. A balanced C++ set instead
gives O(n log n + C), not O(n log n) when there are many conflicts.
Sweep space: O(n) auxiliary for events/active IDs. Touching ends do not
overlap; end events are therefore processed before starts at equal times.
'''
