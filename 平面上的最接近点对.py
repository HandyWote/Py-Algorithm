import math

def dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def closest_pair(points):
    n = len(points)
    if n <= 3:
        return min((dist(points[i], points[j]) for i in range(n) for j in range(i + 1, n)), key=lambda x: x) ** 0.5

    mid = n // 2
    p1 = points[:mid]
    p2 = points[mid:]

    dist1 = closest_pair(p1)
    dist2 = closest_pair(p2)
    d = min(dist1, dist2)

    delta = d ** 2
    mid_line = [p for p in points if abs(p[0] - points[mid][0]) < d]

    mid_line.sort(key=lambda x: x[1])
    for i in range(len(mid_line)):
        for j in range(i + 1, len(mid_line)):
            if (mid_line[j][1] - mid_line[i][1]) ** 2 < delta:
                d = min(d, math.sqrt(dist(mid_line[i], mid_line[j])))

    return d

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

# 对点按照x坐标排序
points.sort(key=lambda x: x[0])

# 计算并打印最接近点对的距离
print("%.4f" % closest_pair(points))