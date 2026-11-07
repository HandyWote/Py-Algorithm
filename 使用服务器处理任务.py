import heapq

class Solution:
    def __init__(self) -> None:
        self.servers: list[int] = []
        self.tasks: list[int] = []
        self.ans: list[int] = []
        self.idle_servers: list[tuple[int, int]] = []
        self.busy_servers: list[tuple[int, int]] = []
        self.cur_time: int = 0

    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        self._reset(servers, tasks)
        self._solve()
        return self.ans

    def _reset(self, servers: list[int], tasks: list[int]) -> None:
        self.servers = servers
        self.tasks = tasks
        self.ans = [0] * len(tasks)
        
        self.idle_servers = [(weight, idx) for idx, weight in enumerate(servers)]
        heapq.heapify(self.idle_servers)
        
        self.busy_servers = []
        self.cur_time = 0

    def _solve(self) -> None:
        for arrival_time, duration in enumerate(self.tasks):
            self.cur_time = max(self.cur_time, arrival_time)
            self._release()
            
            if not self.idle_servers:
                self.cur_time = self.busy_servers[0][0]
                self._release()
                
            _, server_idx = heapq.heappop(self.idle_servers)
            finish_time = self.cur_time + duration
            heapq.heappush(self.busy_servers, (finish_time, server_idx))
            self.ans[arrival_time] = server_idx

    def _release(self) -> None:
        while self.busy_servers and self.busy_servers[0][0] <= self.cur_time:
            _, server_idx = heapq.heappop(self.busy_servers)
            weight = self.servers[server_idx]
            heapq.heappush(self.idle_servers, (weight, server_idx))
