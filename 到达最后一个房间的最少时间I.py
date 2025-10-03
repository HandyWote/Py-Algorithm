import heapq

class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        
        heap = [(0, 0, 0)]
        
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while heap:
            time, i, j = heapq.heappop(heap)
            
            if i == n - 1 and j == m - 1:
                return time

            if time > dist[i][j]:
                continue

            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                
                if 0 <= ni < n and 0 <= nj < m:

                    new_time = max(time, moveTime[ni][nj]) + 1

                    if new_time < dist[ni][nj]:
                        dist[ni][nj] = new_time
                        heapq.heappush(heap, (new_time, ni, nj))
        
        return dist[n-1][m-1]
    
if __name__ == "__main__":
    s = Solution()
    print(s.minTimeToReach([[0,0,0],[0,0,0]]))
    print(s.minTimeToReach([[0,1],[1,2]]))