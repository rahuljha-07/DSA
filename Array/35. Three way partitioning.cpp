void threeWayPartition(vector<int>& array, int a, int b) {
    int low = 0, high = array.size() - 1, mid = 0;

    // Loop through the array
    while (mid <= high) {
        if (array[mid] < a) {
            swap(array[mid], array[low]); // Move elements less than `a` to the left
            low++;
            mid++;
        } else if (array[mid] > b) {
            swap(array[mid], array[high]); // Move elements greater than `b` to the right
            high--;
        } else {
            mid++; // Elements in the range `[a, b]` remain in place
        }
    }
}
