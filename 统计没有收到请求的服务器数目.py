from collections import defaultdict

class Solution:
    def __init__(self) -> None:
        self.time_to_servers: defaultdict[int, set[int]] = defaultdict(set[int])
        self.server_counts: defaultdict[int, int] = defaultdict(int)
        self.active_cnt: int = 0

    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        self._reset()
        self._build(logs)

        sorted_times = sorted(self.time_to_servers.keys())
        sorted_queries = sorted((time, idx) for idx, time in enumerate(queries))

        return self._sliding_window(n, x, sorted_times, sorted_queries)

    def _reset(self) -> None:
        self.time_to_servers.clear()
        self.server_counts.clear()
        self.active_cnt = 0

    def _build(self, logs: list[list[int]]) -> None:
        for server, time in logs:
            self.time_to_servers[time].add(server)

    def _sliding_window(self, n: int, x: int, sorted_times: list[int], sorted_queries: list[tuple[int, int]]) -> list[int]:
        ans: list[int] = [0] * len(sorted_queries)
        left, right = 0, 0

        for time, idx in sorted_queries:
            while right < len(sorted_times) and sorted_times[right] <= time:
                self._add(sorted_times[right])
                right += 1

            while left < len(sorted_times) and sorted_times[left] < time - x:
                self._remove(sorted_times[left])
                left += 1

            ans[idx] = n - self.active_cnt

        return ans

    def _add(self, time: int) -> None:
        for server in self.time_to_servers[time]:
            if self.server_counts[server] == 0:
                self.active_cnt += 1
            self.server_counts[server] += 1

    def _remove(self, time: int) -> None:
        for server in self.time_to_servers[time]:
            self.server_counts[server] -= 1
            if self.server_counts[server] == 0:
                self.active_cnt -= 1
