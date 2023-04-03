from sys import stdin

def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count

def points_cover(starts, ends, points):
    assert len(starts) == len(ends)
    assert all(s <= e for s, e in zip(starts, ends))
    n = len(points)
    m = len(starts)

    # Sort the segments by their right endpoint
    sorted_segments = sorted(zip(starts, ends))

    # Iterate over the points and segments simultaneously
    i = 0
    count = [0] * n
    for j in range(n):
        while i < m and sorted_segments[i][1] < points[j]:
            i += 1
        if i < m and sorted_segments[i][0] <= points[j] <= sorted_segments[i][1]:
            count[j] = 1

    # Calculate the cumulative sum of the count array
    for j in range(1, n):
        count[j] += count[j - 1]

    return count



if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
