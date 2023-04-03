from collections import namedtuple
from itertools import combinations
from math import sqrt

Point = namedtuple('Point', 'x y')

def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared

def merge(left_points, right_points, delta):
    merged_points = []
    j = 0
    for i, left_point in enumerate(left_points):
        while j < len(right_points) and right_points[j].y < left_point.y + delta:
            merged_points.append(right_points[j])
            j += 1
        merged_points.append(left_point)
    merged_points.extend(right_points[j:])
    return merged_points


def closest_pair(points):
    if len(points) <= 1:
        return float("inf"), None, None

    mid = len(points) // 2
    left_points = points[:mid]
    right_points = points[mid:]

    delta_left, p_left, q_left = closest_pair(left_points)
    delta_right, p_right, q_right = closest_pair(right_points)

    delta = min(delta_left, delta_right)

    merged_points = merge(left_points, right_points, delta)
    strip_points = [point for point in merged_points
                    if abs(point.x - merged_points[mid].x) < delta]

    best_distance = delta
    best_pair = (p_left, q_left)
    for i, point_i in enumerate(strip_points):
        for j in range(i + 1, min(i + 8, len(strip_points))):
            point_j = strip_points[j]
            distance = distance_squared(point_i, point_j)
            if distance < best_distance:
                best_distance = distance
                best_pair = (point_i, point_j)

    return best_distance, best_pair[0], best_pair[1]

def minimum_distance_squared(points):
    sorted_points = sorted(points)
    return closest_pair(sorted_points)[0]

if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
