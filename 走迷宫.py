def get_input():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    x1,y1,x2,y2 = map(int, input().split())
    return n, m, grid, x1-1, y1-1, x2-1, y2-1

def bfs(n, m, grid, x1, y1, x2, y2):
    from collections import deque
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False] * m for _ in range(n)]
    queue = deque([(x1, y1, 0)])
    visited[x1][y1] = True

    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == (x2, y2):
            return dist
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    return -1

if __name__ == "__main__":
    n, m, grid, x1, y1, x2, y2 = get_input()
    result = bfs(n, m, grid, x1, y1, x2, y2)
    print(result)