def minimumPlatforms(arr, dep, n):
    arr[:n] = sorted(arr[:n])
    dep[:n] = sorted(dep[:n])
    if n == 0:
        return 0
    platforms_needed = 1
    result = 1
    i, j = 1, 0
    while i < n and j < n:
        if arr[i] <= dep[j]:
            platforms_needed += 1
            i += 1
        else:
            platforms_needed -= 1
            j += 1
        result = max(result, platforms_needed)
    return result


def main():
    arr1 = [900, 940, 950, 1100, 1500, 1800]
    dep1 = [910, 1200, 1120, 1130, 1900, 2000]
    n1 = len(arr1)
    print("Minimum Platforms Required:", minimumPlatforms(arr1, dep1, n1))
    arr2 = [900, 1235, 1100]
    dep2 = [1000, 1240, 1200]
    n2 = len(arr2)
    print("Minimum Platforms Required:", minimumPlatforms(arr2, dep2, n2))
    arr3 = [1000, 935, 1100]
    dep3 = [1200, 1240, 1130]
    n3 = len(arr3)
    print("Minimum Platforms Required:", minimumPlatforms(arr3, dep3, n3))


if __name__ == "__main__":
    main()


'''
Let n be element count.
Time: O(n log(n+1)): sorting dominates the subsequent O(n) scan.
Space: O(n) auxiliary worst case for Python's sorting workspace, even
when the input list is sorted in place; no full result array is returned.
Both first-n prefixes are reordered. Each sweep step advances i or j,
so the two-pointer loop is O(n), not O(n^2).
Arrivals at an equal departure time are counted first and need an extra
platform. Arrival/departure arrays must represent valid train intervals.
'''
