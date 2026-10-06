# Function to check if it's possible to allocate books to students
# such that the maximum number of pages allocated to any student is <= maxPages
def isValidAllocation(books, numStudents, maxPages):
    # Start with one student
    studentsRequired = 1
    # Sum of pages allocated to the current student
    pagesAllocated = 0

    # Iterate through each book using a traditional for loop
    for i in range(len(books)):
        # Add current book's pages to the total for the current student
        # Start with the current book for the new student
        pagesAllocated += books[i]

        # If the total exceeds maxPages, allocate to the next student
        if pagesAllocated > maxPages:
            studentsRequired += 1
            pagesAllocated = books[i]

        # If we need more students than available, return false
        if studentsRequired > numStudents:
            return False

    # If allocation is valid, return true
    return True


# Function to find the minimum number of pages that can be allocated
def findMinimumPages(books, numBooks, numStudents):
    # If there are more students than books, allocation is impossible
    if numBooks < numStudents:
        return -1

    # Sum of all pages
    totalPages = 0
    # Maximum pages in a single book
    maxPages = 0

    # Calculate total pages and find the maximum pages in a single book using a traditional
    # for loop
    for i in range(numBooks):
        totalPages += books[i]
        maxPages = max(maxPages, books[i])

    # Binary search to find the minimum possible maximum pages
    # Start from the book with the maximum pages
    start = maxPages
    # End at the total number of pages
    end = totalPages
    # Variable to store the result
    result = -1

    # Perform binary search
    while start <= end:
        # Middle value for current max pages
        mid = start + (end - start) // 2

        # Check if allocation is possible with mid as the maximum pages
        if isValidAllocation(books, numStudents, mid):
            # Update result with the valid mid value
            result = mid
            # Try for a smaller max pages
            end = mid - 1
        else:
            # Increase the minimum max pages required
            start = mid + 1

    # Return the minimum pages required
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
