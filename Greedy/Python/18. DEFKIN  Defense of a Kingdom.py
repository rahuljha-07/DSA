import sys


def largestUndefendedRectangle(w, h, towers):
    x_coords = [0]
    y_coords = [0]
    for tower in towers:
        x_coords.append(tower[0])
        y_coords.append(tower[1])
    x_coords.append(w + 1)
    y_coords.append(h + 1)
    x_coords.sort()
    y_coords.sort()
    max_x_gap = 0
    max_y_gap = 0
    for i in range(1, len(x_coords)):
        max_x_gap = max(max_x_gap, x_coords[i] - x_coords[i - 1] - 1)
    for i in range(1, len(y_coords)):
        max_y_gap = max(max_y_gap, y_coords[i] - y_coords[i - 1] - 1)
    return max_x_gap * max_y_gap


def main():
    tokens = iter(map(int, sys.stdin.read().split()))
    t = next(tokens)
    for _ in range(t):
        w = next(tokens)
        h = next(tokens)
        n = next(tokens)
        towers = [(next(tokens), next(tokens)) for _ in range(n)]
        print(largestUndefendedRectangle(w, h, towers))


if __name__ == "__main__":
    main()


'''
Let n be the number of towers in one test case.
Time: O(n log(n+1)): sorting the n+2 x and y coordinates dominates the
linear scans for the largest gaps. Grid cells are never enumerated.
Space: O(n) auxiliary for the coordinate lists and sorting workspace.
The main function also buffers all input tokens across test cases.
'''
