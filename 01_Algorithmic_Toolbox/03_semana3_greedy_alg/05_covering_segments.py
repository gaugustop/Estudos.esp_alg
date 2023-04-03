from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    # write your code here
    for s in segments:
        points.append(s.start)
        points.append(s.end)
    return points

class Segment():
    def __init__(self,start,end):
        self.start = start
        self.end = end

def optimal_points(segments):
    segments.sort(key = lambda s: s.end)
    points = []
    while len(segments) > 0:
        point = segments[0].end
        points.append(point)
        segments = list(filter(lambda i: i.start > point, segments))
    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
