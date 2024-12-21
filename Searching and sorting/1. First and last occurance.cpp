vector<int> find(int arr[], int n , int x) {
    vector<int> result(2, -1); // Initialize result vector with -1 for both positions
    
    // Binary search for the first occurrence of x
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] < x) {
            low = mid + 1;
        } else if (arr[mid] > x) {
            high = mid - 1;
        } else {
            // When arr[mid] == x, check if it's the first occurrence
            if (mid == 0 || arr[mid - 1] != x) {
                result[0] = mid;
                break;
            }
            high = mid - 1; // Continue to search in the left part
        }
    }

    // Binary search for the last occurrence of x
    low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] < x) {
            low = mid + 1;
        } else if (arr[mid] > x) {
            high = mid - 1;
        } else {
            // When arr[mid] == x, check if it's the last occurrence
            if (mid == n - 1 || arr[mid + 1] != x) {
                result[1] = mid;
                break;
            }
            low = mid + 1; // Continue to search in the right part
        }
    }

    return result;
}
