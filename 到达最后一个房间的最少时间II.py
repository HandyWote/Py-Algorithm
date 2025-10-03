import heapq

class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        # 优先队列：(time, i, j, move_count)
        # move_count 用于跟踪移动次数，决定移动时间
        heap = [(0, 0, 0, 0)]
        
        # 记录到达每个房间的最小时间
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        
        # 四个方向：上、下、左、右
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while heap:
            time, i, j, move_count = heapq.heappop(heap)
            
            # 到达终点
            if i == n - 1 and j == m - 1:
                return time
            
            # 如果当前时间不是最优，跳过
            if time > dist[i][j]:
                continue
            
            # 探索四个方向
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                
                if 0 <= ni < n and 0 <= nj < m:
                    # 计算移动时间：奇数次移动花费1秒，偶数次移动花费2秒
                    move_cost = 1 if (move_count + 1) % 2 == 1 else 2
                    
                    # 计算新时间
                    new_time = max(time, moveTime[ni][nj]) + move_cost
                    
                    # 如果找到更优解，更新
                    if new_time < dist[ni][nj]:
                        dist[ni][nj] = new_time
                        heapq.heappush(heap, (new_time, ni, nj, move_count + 1))
        
        return dist[n-1][m-1]
    
if __name__ == "__main__":
    s = Solution()
    print(s.minTimeToReach([[0,0,0],[0,0,0]]))
    print(s.minTimeToReach([[0,1],[1,2]]))