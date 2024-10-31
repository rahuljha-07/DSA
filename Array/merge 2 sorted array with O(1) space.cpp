//gap method 
// Function to calculate the next gap
int nextGap(int gap) {
    if (gap <= 1) return 0; // When gap becomes 0 or 1, return 0.
    return (gap / 2) + (gap % 2); // For odd gaps, use ceiling value
}

void mergeUsingGap(std::vector<int>& arr1, int m, std::vector<int>& arr2, int n) {
    int gap = m + n;
    gap = nextGap(gap);

    while (gap > 0) {
        // Compare elements in arr1
        for (int i = 0; i + gap < m; i++) {
            if (arr1[i] > arr1[i + gap]) {
                swap(arr1[i], arr1[i + gap]);
            }
        }

        // Compare elements between arr1 and arr2
        for (int i = 0; i < m && i + gap < n; i++) {
            if (arr1[i] > arr2[i + gap]) {
                swap(arr1[i], arr2[i + gap]);
            }
        }

        // Compare elements in arr2
        for (int i = 0; i + gap < n; i++) {
            if (arr2[i] > arr2[i + gap]) {
                swap(arr2[i], arr2[i + gap]);
            }
        }

        gap = nextGap(gap); // Update the gap
    }
}