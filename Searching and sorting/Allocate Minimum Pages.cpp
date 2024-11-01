#include <vector>
#include <algorithm>
using namespace std;

// Function to check if it's possible to allocate books to students
// such that the maximum number of pages allocated to any student is <= maxPages
bool isValidAllocation(const vector<int>& books, int numStudents, int maxPages) {
    int studentsRequired = 1; // Start with one student
    int pagesAllocated = 0; // Sum of pages allocated to the current student

    // Iterate through each book using a traditional for loop
    for (int i = 0; i < books.size(); i++) {
        pagesAllocated += books[i]; // Add current book's pages to the total for the current student

        // If the total exceeds maxPages, allocate to the next student
        if (pagesAllocated > maxPages) {
            studentsRequired++;
            pagesAllocated = books[i]; // Start with the current book for the new student
        }

        // If we need more students than available, return false
        if (studentsRequired > numStudents) {
            return false;
        }
    }

    // If allocation is valid, return true
    return true;
}

// Function to find the minimum number of pages that can be allocated
int findMinimumPages(const vector<int>& books, int numBooks, int numStudents) {
    // If there are more students than books, allocation is impossible
    if (numBooks < numStudents) {
        return -1;
    }

    int totalPages = 0; // Sum of all pages
    int maxPages = 0; // Maximum pages in a single book

    // Calculate total pages and find the maximum pages in a single book using a traditional for loop
    for (int i = 0; i < numBooks; i++) {
        totalPages += books[i];
        maxPages = max(maxPages, books[i]);
    }

    // Binary search to find the minimum possible maximum pages
    int start = maxPages; // Start from the book with the maximum pages
    int end = totalPages; // End at the total number of pages
    int result = -1; // Variable to store the result

    // Perform binary search
    while (start <= end) {
        int mid = start + (end - start) / 2; // Middle value for current max pages

        // Check if allocation is possible with mid as the maximum pages
        if (isValidAllocation(books, numStudents, mid)) {
            result = mid; // Update result with the valid mid value
            end = mid - 1; // Try for a smaller max pages
        } else {
            start = mid + 1; // Increase the minimum max pages required
        }
    }

    return result; // Return the minimum pages required
}
