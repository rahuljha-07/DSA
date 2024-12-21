// Function to determine if B can be reached from A by adding C repeatedly.
// A: starting number, B: target number, C: common difference
int isInArithmeticSequence(int start, int target, int difference) {
    // If the starting number is equal to the target number, return true (1)
    if (start == target) return 1;

    // If the common difference is 0, we cannot reach the target unless they are the same
    if (difference == 0) return 0;

    // Check if moving from start to target is possible with the given difference
    // If the difference in numbers is of opposite sign to the common difference, return false (0)
    if ((target - start > 0 && difference < 0) || (target - start < 0 && difference > 0)) return 0;

    // Return true (1) if the difference between target and start is a multiple of the common difference
    return !((target - start) % difference);
}
