def isValidAllocation(books, numStudents, maxPages):
    studentsRequired = 1
    pagesAllocated = 0

    for i in range(len(books)):
        pagesAllocated += books[i]

        if pagesAllocated > maxPages:
            studentsRequired += 1
            pagesAllocated = books[i]

        if studentsRequired > numStudents:
            return False

    return True


def findMinimumPages(books, numBooks, numStudents):
    if numBooks < numStudents:
        return -1

    totalPages = 0
    maxPages = 0

    for i in range(numBooks):
        totalPages += books[i]
        maxPages = max(maxPages, books[i])

    start = maxPages
    end = totalPages
    result = -1

    while start <= end:
        mid = start + (end - start) // 2

        if isValidAllocation(books, numStudents, mid):
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    return result


books = [12, 34, 67, 90]
numStudents = 2
print(findMinimumPages(books, len(books), numStudents))


'''
Time Complexity: O(n * log(sum - max))

Reason:
Binary search is performed between the largest single book and total pages.
For each mid value, isValidAllocation scans all n books once.

Space Complexity: O(1)

Reason:
Only counters and binary-search variables are used.
'''
