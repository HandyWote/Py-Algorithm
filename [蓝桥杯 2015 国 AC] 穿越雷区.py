def find(n:int, c:str, g:list[list[str]])->list[int]:
    for y,b in enumerate(g):
        try:
            x = b.index(c)
            return y, x
        except ValueError:
            pass

from collections import deque

n = int(input())
grid = [input().split() for _ in range(n)]

start_x, start_y = find(n, 'A', grid)

# 初始化队列和访问数组
sign_to_index = {'A': 0, '+': 1, '-': 2}
visited = [[[False] * 3 for _ in range(n)] for _ in range(n)]
queue = deque()
queue.append((start_x, start_y, None, 0))
visited[start_x][start_y][sign_to_index['A']] = True

# 四个方向
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    x, y, prev_sign, steps = queue.popleft()
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] == 'B':
                print(steps + 1)
                exit()
            current_sign = grid[nx][ny]
            # 判断符号条件
            valid = False
            if prev_sign is None:
                valid = True
            else:
                if current_sign != prev_sign:
                    valid = True
            if valid:
                new_prev = current_sign
                k = sign_to_index[new_prev]
                if not visited[nx][ny][k]:
                    visited[nx][ny][k] = True
                    queue.append((nx, ny, new_prev, steps + 1))
print(-1)