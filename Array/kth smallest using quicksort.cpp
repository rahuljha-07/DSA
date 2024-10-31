    int partition(vector<int> &arr, int low, int high) {
    int pivot_index = (high + low) / 2;
    int pivot = arr[pivot_index]; 
    swap(arr[pivot_index], arr[high]); // Move pivot to the end
    int left = low;     
    int right = high - 1;  
    
    while (true) {
        // Move the left pointer to the right until we find an element >= pivot
        while (left <= right && arr[left] < pivot) {
            left++;
        }

        // Move the right pointer to the left until we find an element <= pivot
        while (left <= right && arr[right] > pivot) {
            right--;
        }
        
        if (left < right) {
            swap(arr[left], arr[right]);  // Swap elements out of order
        } else {
            swap(arr[left], arr[high]);  // Move pivot to its final place
            return left;  // Return the index of the pivot
        }
    }
}

int kthSmallest(vector<int> arr, int k) {
    int l = 0, r = arr.size() - 1; // Change r to size - 1
    int p_index;
    while (l <= r) {
        p_index = partition(arr, l, r);
        if (p_index == k - 1) {
            return arr[p_index]; // Return the k-th smallest element
        } else if (p_index > k - 1) {
            r = p_index - 1; // Search in the left part
        } else {
            l = p_index + 1; // Search in the right part
        }
    }
    return -1; // Return -1 if k is out of bounds
}